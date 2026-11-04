/* Shield Tech motion layer: progressive enhancement only, no dependencies.
   Runs only when html.fx is set (no reduced-motion request, animations not paused). Page content never depends on it. */
(function () {
  "use strict";
  var win = window, doc = document, root = doc.documentElement;
  if (!win.requestAnimationFrame || !doc.body) return;

  var KEY = "shieldtech-motion";
  var mq = function (q) { return win.matchMedia ? win.matchMedia(q) : { matches: false }; };
  var reduced = mq("(prefers-reduced-motion: reduce)").matches;
  var fine = mq("(hover: hover) and (pointer: fine)").matches;
  var isBot = /googlebot|bingbot|yandex|baiduspider|duckduckbot|slurp|crawler|spider|lighthouse|pagespeed|gtmetrix|prerender/i.test(navigator.userAgent || "");
  var HAS_IO = "IntersectionObserver" in win;

  function $(s, c) { return (c || doc).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); }
  function el(tag, cls, html) { var n = doc.createElement(tag); if (cls) n.className = cls; if (html) n.innerHTML = html; return n; }
  function on() { return root.classList.contains("fx"); }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function rand(a, b) { return a + Math.random() * (b - a); }

  var fields = [];          // canvas signal fields
  var revealables = [];     // elements still waiting to be revealed

  /* ================================================================
     1. Floating interface: progress bar, back to top, motion toggle, mobile quote bar
     ================================================================ */
  var header = $(".site-header");
  var bar = el("div", "fx-progress", "<i></i>"); bar.setAttribute("aria-hidden", "true");
  var barFill = bar.firstChild;
  doc.body.appendChild(bar);

  var toTop = el("button", "fx-top",
    '<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false"><circle class="fx-top__track" cx="24" cy="24" r="21"/><circle class="fx-top__ring" cx="24" cy="24" r="21"/></svg>' +
    '<svg class="fx-top__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 19V5M5 12l7-7 7 7"/></svg>');
  toTop.type = "button"; toTop.setAttribute("aria-label", "Back to top");
  var ring = $(".fx-top__ring", toTop);
  toTop.addEventListener("click", function () { win.scrollTo({ top: 0, behavior: on() ? "smooth" : "auto" }); });
  doc.body.appendChild(toTop);

  var quoteLink = $(".nav__cta");
  var mcta = null;
  if (quoteLink) {
    mcta = el("div", "fx-mcta");
    var mb = el("a", "btn btn--primary", "<span>" + quoteLink.textContent.trim() + "</span>");
    mb.href = quoteLink.getAttribute("href");
    mcta.appendChild(mb);
    doc.body.appendChild(mcta);
  }
  var onContact = !!$('.nav-link[aria-current="page"][href*="contact"]');

  /* Visible controls to pause and resume animation (shown unless the visitor's system asks for reduced motion) */
  var toggle = null, toggleLbl = null;
  if (!reduced) {
    toggle = el("button", "fx-toggle",
      '<svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg>' +
      '<svg class="i-play" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5v14l11-7z"/></svg>');
    toggle.type = "button";
    toggle.setAttribute("title", "Pause or resume animations");
    toggle.setAttribute("aria-pressed", String(!on()));
    toggle.setAttribute("aria-label", on() ? "Pause animations" : "Play animations");
    toggleLbl = el("span", "fx-toggle__lbl", on() ? "Pause animations" : "Play animations");
    toggle.appendChild(toggleLbl);
    toggle.addEventListener("click", function () { setMotion(!on()); });
    // floating button on larger screens; on phones it sits in the footer so it never covers content
    var phone = mq("(max-width: 700px)"), foot = $(".foot__bottom");
    var place = function () {
      if (phone.matches && foot) { foot.appendChild(toggle); toggle.classList.add("fx-toggle--foot"); }
      else { doc.body.appendChild(toggle); toggle.classList.remove("fx-toggle--foot"); }
    };
    place();
    if (phone.addEventListener) phone.addEventListener("change", place);
  }

  function setMotion(enable) {
    root.classList.toggle("fx", enable);
    root.classList.toggle("fx-off", !enable);
    try { win.localStorage.setItem(KEY, enable ? "on" : "off"); } catch (e) { /* storage may be blocked */ }
    if (toggle) {
      toggle.setAttribute("aria-pressed", String(!enable));
      toggle.setAttribute("aria-label", enable ? "Pause animations" : "Play animations");
      if (toggleLbl) toggleLbl.textContent = enable ? "Pause animations" : "Play animations";
    }
    if (!enable) revealAll();
    fields.forEach(function (f) { f.refresh(); });
  }

  /* near the end of the page the mobile bar steps aside */
  var endCount = 0;
  if (HAS_IO) {
    var endIO = new IntersectionObserver(function (es) {
      es.forEach(function (e) { endCount += e.isIntersecting ? 1 : -1; });
      endCount = Math.max(0, endCount);
      requestUpdate();
    }, { threshold: 0.05 });
    $$(".cta-band, .site-footer, #enquiry").forEach(function (n) { endIO.observe(n); });
  }

  /* ================================================================
     2. Scroll loop: progress, header state, parallax, back to top
     ================================================================ */
  var heroEl = $(".hero");
  var heroBg = heroEl && $(".hero__bg", heroEl);
  var heroArt = heroEl && $(".hero__art", heroEl);
  var artPX = 0, artPY = 0, scrollY = 0, ticking = false;

  function requestUpdate() { if (!ticking) { ticking = true; win.requestAnimationFrame(update); } }
  function applyArt() {
    if (!heroArt) return;
    if (!on()) { heroArt.style.transform = ""; return; }
    var lift = clamp(scrollY * -0.07, -60, 0);
    heroArt.style.transform = "perspective(1100px) translate3d(" + (artPX * -16).toFixed(1) + "px," + (artPY * -12 + lift).toFixed(1) + "px,0) rotateX(" + (artPY * -5).toFixed(2) + "deg) rotateY(" + (artPX * 7).toFixed(2) + "deg)";
  }
  function update() {
    ticking = false;
    scrollY = win.pageYOffset || root.scrollTop || 0;
    var max = Math.max(1, root.scrollHeight - win.innerHeight);
    var p = clamp(scrollY / max, 0, 1);
    barFill.style.transform = "scaleX(" + p.toFixed(4) + ")";
    if (header) header.classList.toggle("is-stuck", scrollY > 24);
    toTop.classList.toggle("is-on", scrollY > 700);
    ring.style.strokeDashoffset = String(131.95 * (1 - p));
    if (heroBg) {
      if (!on()) heroBg.style.transform = "";
      else if (scrollY < win.innerHeight * 1.2) heroBg.style.transform = "translate3d(0," + clamp(scrollY * 0.2, 0, 150).toFixed(1) + "px,0)";
    }
    applyArt();
    if (mcta) {
      var navOpen = header && header.classList.contains("nav-open");
      mcta.classList.toggle("is-on", scrollY > 560 && endCount === 0 && !onContact && !navOpen);
    }
  }
  win.addEventListener("scroll", requestUpdate, { passive: true });
  win.addEventListener("resize", requestUpdate, { passive: true });
  if (header) new MutationObserver(requestUpdate).observe(header, { attributes: true, attributeFilter: ["class"] });
  update();

  /* ================================================================
     3. Reveal on scroll (Web Animations API, so it never fights hover transitions)
     ================================================================ */
  var REVEAL = [".sec-head", ".grid > *", ".facts li", ".steps li", ".split__media", ".split__body", ".faq__item", ".partner", ".table-wrap",
    ".note", ".info__item", ".form", ".anatomy__plate", ".anatomy__panel", ".cta-band__in > div", ".checks li", ".foot__top > *", ".foot__mid > *"];

  function reveal(n, instant) {
    if (!n.__hidden) { n.classList.add("is-in"); return; }
    n.__hidden = false;
    n.style.opacity = "";
    n.classList.add("is-in");
    if (instant || !on() || !n.animate) return;
    n.animate([{ opacity: 0, transform: "translateY(28px)" }, { opacity: 1, transform: "none" }],
      { duration: 800, delay: n.__delay || 0, easing: "cubic-bezier(.2,.7,.2,1)", fill: "backwards" });
  }
  function revealAll() {
    revealables.forEach(function (n) { reveal(n, true); });
    revealables = [];
  }

  function setupReveal() {
    if (!on() || isBot || !HAS_IO) return;
    var vh = win.innerHeight, counts = new Map();
    REVEAL.forEach(function (sel) {
      $$(sel).forEach(function (n) {
        if (n.__seen || n.closest(".hero, .page-hero, .site-header")) return;
        n.__seen = true;
        var r = n.getBoundingClientRect();
        if (r.top < vh * 0.9) { n.classList.add("is-in"); return; }     // already on screen: leave untouched
        var par = n.parentNode, idx = counts.get(par) || 0;
        counts.set(par, idx + 1);
        n.__delay = Math.min(idx, 6) * 85;
        n.__hidden = true;
        n.style.opacity = "0";
        revealables.push(n);
      });
    });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        reveal(e.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
    revealables.forEach(function (n) { io.observe(n); });
    // failsafe: never leave anything hidden if observers misbehave
    win.setTimeout(function () {
      revealables.forEach(function (n) { if (n.__hidden && n.getBoundingClientRect().top < win.innerHeight) reveal(n); });
    }, 3000);
    win.addEventListener("beforeprint", revealAll);
  }

  /* ================================================================
     4. Count-up for the fact strip
     ================================================================ */
  function setupCounters() {
    var nodes = $$(".facts strong");
    if (!nodes.length || !on() || isBot) return;
    nodes.forEach(function (n) {
      var orig = n.textContent, parts = orig.split(/(\d+)/);
      if (parts.length < 3) return;
      function run() {
        var t0 = win.performance.now(), dur = 1600;
        (function tick(now) {
          var p = clamp((now - t0) / dur, 0, 1), e = 1 - Math.pow(1 - p, 4);
          n.textContent = parts.map(function (s, i) { return i % 2 ? String(Math.round(parseInt(s, 10) * e)) : s; }).join("");
          if (p < 1) win.requestAnimationFrame(tick); else n.textContent = orig;
        })(t0);
      }
      var r = n.getBoundingClientRect();
      if (r.top < win.innerHeight * 0.95 || !HAS_IO) { run(); return; }
      n.textContent = parts.map(function (s, i) { return i % 2 ? "0" : s; }).join("");
      var io = new IntersectionObserver(function (es) {
        if (es[0].isIntersecting) { io.disconnect(); run(); }
      }, { threshold: 0.6 });
      io.observe(n);
    });
  }

  /* ================================================================
     5. Pointer effects: card spotlight, tilt, magnetic buttons
     ================================================================ */
  function setupPointer() {
    if (!fine) return;
    var SPOT = ".card, .tile, .ind, .model, .facts li", TILT = ".tile, .model", MAG = ".btn";
    var curTilt = null, curMag = null, ev = null, pend = false;
    function clearTilt(t) { t.classList.remove("is-tilt"); t.style.removeProperty("--rx"); t.style.removeProperty("--ry"); }
    function clearMag(m) { m.style.translate = ""; }
    function step() {
      pend = false;
      var e = ev; if (!e || !on()) return;
      var t = e.target; if (!t || !t.closest) return;
      var s = t.closest(SPOT);
      if (s) {
        var r = s.getBoundingClientRect();
        s.style.setProperty("--mx", (e.clientX - r.left).toFixed(0) + "px");
        s.style.setProperty("--my", (e.clientY - r.top).toFixed(0) + "px");
      }
      var tl = t.closest(TILT);
      if (tl !== curTilt) { if (curTilt) clearTilt(curTilt); curTilt = tl; }
      if (tl) {
        var r2 = tl.getBoundingClientRect();
        var px = (e.clientX - r2.left) / r2.width - 0.5, py = (e.clientY - r2.top) / r2.height - 0.5;
        tl.style.setProperty("--ry", (px * 6).toFixed(2) + "deg");
        tl.style.setProperty("--rx", (-py * 6).toFixed(2) + "deg");
        tl.classList.add("is-tilt");
      }
      var mg = t.closest(MAG);
      if (mg !== curMag) { if (curMag) clearMag(curMag); curMag = mg; }
      if (mg) {
        var r3 = mg.getBoundingClientRect();
        mg.style.translate = ((e.clientX - (r3.left + r3.width / 2)) * 0.14).toFixed(1) + "px " + ((e.clientY - (r3.top + r3.height / 2)) * 0.22).toFixed(1) + "px";
      }
    }
    doc.addEventListener("pointermove", function (e) {
      if (e.pointerType === "touch") return;
      ev = e; if (!pend) { pend = true; win.requestAnimationFrame(step); }
    }, { passive: true });
    doc.documentElement.addEventListener("mouseleave", function () {
      if (curTilt) clearTilt(curTilt); if (curMag) clearMag(curMag); curTilt = curMag = null;
    });
  }

  /* ================================================================
     6. Signal field: drifting signal nodes that bend around the cursor like a shield
     ================================================================ */
  function SignalField(host, o) {
    var cv = el("canvas", "fx-canvas"); cv.setAttribute("aria-hidden", "true");
    var glow = o.glow ? el("div", "fx-glow") : null;
    if (glow) host.appendChild(glow);
    host.appendChild(cv);
    var ctx = cv.getContext("2d");
    if (!ctx) return null;
    var W = 0, H = 0, dpr = 1, pts = [], pk = [], mouse = { x: 0, y: 0, on: false }, raf = 0, last = 0, t = 0;
    var visible = false, running = false, low = false, frames = 0, acc = 0, nextPk = 0, glowRaf = 0;
    var R = o.repel || 120, L = o.link || 110;

    function seed() {
      var n = clamp(Math.round(W * H / o.area), 10, o.max);
      if (low) n = Math.ceil(n / 2);
      pts = [];
      for (var i = 0; i < n; i++) {
        pts.push({ x: rand(0, W), y: rand(0, H), vx: rand(8, 30), vy: rand(-7, 7), r: rand(1.2, 2.7), a: rand(0.5, 1), ph: rand(0, 6.28) });
      }
      pk = [];
    }
    function resize() {
      var r = host.getBoundingClientRect();
      if (!r.width || !r.height) return;
      W = r.width; H = r.height;
      dpr = Math.min(win.devicePixelRatio || 1, 1.75);
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      seed();
      if (!running) draw();
    }
    function step(dt) {
      var i, p, dx, dy, d, f;
      for (i = 0; i < pts.length; i++) {
        p = pts[i];
        if (mouse.on) {
          dx = p.x - mouse.x; dy = p.y - mouse.y; d = Math.sqrt(dx * dx + dy * dy);
          if (d < R && d > 0.01) { f = 1 - d / R; f = f * f * 190 * dt; p.x += dx / d * f; p.y += dy / d * f; }
        }
        p.x += p.vx * dt; p.y += (p.vy + Math.sin(t * 0.7 + p.ph) * 5) * dt;
        if (p.x > W + 12) p.x = -12; else if (p.x < -12) p.x = W + 12;
        if (p.y > H + 12) p.y = -12; else if (p.y < -12) p.y = H + 12;
      }
      // data packets hop from node to neighbouring node
      if (!low && o.packets && t > nextPk && pk.length < 4) {
        var a = (Math.random() * pts.length) | 0, b = neighbour(a, -1);
        if (b >= 0) pk.push({ a: a, b: b, k: 0, sp: rand(0.8, 1.5), hops: 0 });
        nextPk = t + rand(0.5, 1.3);
      }
      for (i = pk.length - 1; i >= 0; i--) {
        var q = pk[i]; q.k += q.sp * dt;
        if (q.k >= 1) {
          var nb = q.hops < 3 && Math.random() < 0.8 ? neighbour(q.b, q.a) : -1;
          if (nb >= 0) { q.a = q.b; q.b = nb; q.k = 0; q.hops++; } else pk.splice(i, 1);
        }
      }
    }
    function neighbour(i, not) {
      var p = pts[i], c = [];
      for (var j = 0; j < pts.length; j++) {
        if (j === i || j === not) continue;
        var dx = pts[j].x - p.x, dy = pts[j].y - p.y;
        if (dx * dx + dy * dy < L * L) c.push(j);
      }
      return c.length ? c[(Math.random() * c.length) | 0] : -1;
    }
    function draw() {
      ctx.clearRect(0, 0, W, H);
      var i, j, p, q, dx, dy, d, al;
      // slow scan beam
      if (o.beam && on()) {
        var bw = Math.max(170, W * 0.14), bx = ((t * 0.09) % 1.5 - 0.25) * W;
        var g = ctx.createLinearGradient(bx - bw, 0, bx + bw, 0);
        g.addColorStop(0, "rgba(83,185,229,0)"); g.addColorStop(0.5, "rgba(83,185,229,.11)"); g.addColorStop(1, "rgba(83,185,229,0)");
        ctx.fillStyle = g; ctx.fillRect(bx - bw, 0, bw * 2, H);
      }
      ctx.lineWidth = 1.15;
      for (i = 0; i < pts.length; i++) {
        p = pts[i];
        for (j = i + 1; j < pts.length; j++) {
          q = pts[j]; dx = p.x - q.x; dy = p.y - q.y;
          if (dx > L || dx < -L || dy > L || dy < -L) continue;
          d = Math.sqrt(dx * dx + dy * dy);
          if (d >= L) continue;
          al = (1 - d / L) * o.line;
          ctx.strokeStyle = "rgba(111,200,238," + al.toFixed(3) + ")";
          ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
        }
      }
      for (i = 0; i < pts.length; i++) {
        p = pts[i];
        ctx.fillStyle = "rgba(111,200,238," + p.a.toFixed(2) + ")";
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.2832); ctx.fill();
      }
      for (i = 0; i < pk.length; i++) {
        var a = pts[pk[i].a], b = pts[pk[i].b]; if (!a || !b) continue;
        var x = a.x + (b.x - a.x) * pk[i].k, y = a.y + (b.y - a.y) * pk[i].k;
        ctx.fillStyle = "rgba(83,185,229,.28)"; ctx.beginPath(); ctx.arc(x, y, 8, 0, 6.2832); ctx.fill();
        ctx.fillStyle = "rgba(220,244,255,.95)"; ctx.beginPath(); ctx.arc(x, y, 2.2, 0, 6.2832); ctx.fill();
      }
      if (mouse.on && on()) {
        ctx.save();
        ctx.strokeStyle = "rgba(140,214,246,.38)"; ctx.lineWidth = 1.4; ctx.setLineDash([5, 8]); ctx.lineDashOffset = -t * 10;
        ctx.beginPath(); ctx.arc(mouse.x, mouse.y, R * 0.92, 0, 6.2832); ctx.stroke();
        ctx.restore();
        ctx.fillStyle = "rgba(212,241,255,.8)"; ctx.beginPath(); ctx.arc(mouse.x, mouse.y, 2.6, 0, 6.2832); ctx.fill();
      }
    }
    function frame(now) {
      raf = 0; if (!running) return;
      var dt = Math.min(0.05, (now - last) / 1000); last = now; t += dt;
      step(dt); draw();
      // if the device cannot hold ~30 fps, halve the node count once and drop packets
      acc += dt; frames++;
      if (frames === 90) {
        if (acc / frames > 0.036 && !low) { low = true; pts.length = Math.ceil(pts.length / 2); pk = []; }
        frames = 0; acc = 0;
      }
      raf = win.requestAnimationFrame(frame);
    }
    function start() { if (running) return; running = true; last = win.performance.now(); raf = win.requestAnimationFrame(frame); }
    function stop() { running = false; if (raf) win.cancelAnimationFrame(raf); raf = 0; }
    function refresh() {
      if (visible && !doc.hidden && on()) start(); else { stop(); if (W) draw(); }
    }

    host.addEventListener("pointermove", function (e) {
      if (e.pointerType === "touch" || !on()) return;
      var r = cv.getBoundingClientRect();
      mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; mouse.on = true;
      if (glow) {
        glow.classList.add("is-on");
        if (!glowRaf) glowRaf = win.requestAnimationFrame(function () {
          glowRaf = 0; glow.style.setProperty("--gx", mouse.x.toFixed(0) + "px"); glow.style.setProperty("--gy", mouse.y.toFixed(0) + "px");
          if (o.onMove) o.onMove(mouse.x / W - 0.5, mouse.y / H - 0.5);
        });
      }
    }, { passive: true });
    host.addEventListener("pointerleave", function () {
      mouse.on = false; if (glow) glow.classList.remove("is-on");
      if (o.onMove) o.onMove(0, 0);
    });

    if (win.ResizeObserver) new ResizeObserver(function () { win.requestAnimationFrame(resize); }).observe(host); else win.addEventListener("resize", resize);
    if (HAS_IO) new IntersectionObserver(function (es) { visible = es[0].isIntersecting; refresh(); }, { threshold: 0 }).observe(host); else visible = true;
    resize();
    refresh();
    return { refresh: refresh };
  }

  function setupFields() {
    var mobile = win.innerWidth < 700;
    var specs = [
      { sel: ".hero", o: { area: mobile ? 20000 : 13000, max: mobile ? 42 : 92, link: mobile ? 120 : 145, line: 0.36, repel: 140, packets: true, beam: true, glow: true,
          onMove: function (x, y) { artPX = x; artPY = y; applyArt(); } } },
      { sel: ".page-hero", o: { area: 16000, max: 62, link: 125, line: 0.28, repel: 120, packets: true, beam: true, glow: true } },
      { sel: ".cta-band", o: { area: 22000, max: 44, link: 120, line: 0.26, repel: 120, packets: false, beam: false, glow: false } }
    ];
    specs.forEach(function (s) {
      $$(s.sel).forEach(function (h) { var f = SignalField(h, s.o); if (f) fields.push(f); });
    });
    doc.addEventListener("visibilitychange", function () { fields.forEach(function (f) { f.refresh(); }); });
  }

  /* ================================================================
     7. Chamber diagram: animate only while on screen
     ================================================================ */
  function setupDiagram() {
    var an = $(".anatomy");
    if (!an) return;
    if (!HAS_IO) { an.classList.add("is-live"); return; }
    new IntersectionObserver(function (es) { es.forEach(function (e) { an.classList.toggle("is-live", e.isIntersecting); }); }, { threshold: 0.15 }).observe(an);
  }

  /* ================================================================
     8. Instant navigation: prefetch pages when a link is about to be used
     ================================================================ */
  function setupPrefetch() {
    if (win.location.protocol === "file:") return;
    var c = navigator.connection; if (c && (c.saveData || /2g/.test(c.effectiveType || ""))) return;
    var done = {}, n = 0;
    function hint(e) {
      var a = e.target && e.target.closest && e.target.closest("a[href]");
      if (!a || a.origin !== win.location.origin || a.target === "_blank") return;
      var u = a.href.split("#")[0];
      if (done[u] || u === win.location.href.split("#")[0] || n > 12) return;
      done[u] = 1; n++;
      var l = doc.createElement("link"); l.rel = "prefetch"; l.href = u; doc.head.appendChild(l);
    }
    doc.addEventListener("pointerover", hint, { passive: true });
    doc.addEventListener("touchstart", hint, { passive: true });
  }

  /* ================================================================
     Start
     ================================================================ */
  function boot() {
    try { setupReveal(); } catch (e) { revealAll(); }
    try { setupCounters(); } catch (e) { /* static numbers stay */ }
    try { setupPointer(); } catch (e) { /* hover effects are optional */ }
    try { setupFields(); } catch (e) { /* hero stays static */ }
    try { setupDiagram(); } catch (e) { /* diagram stays static */ }
    try { setupPrefetch(); } catch (e) { /* normal navigation */ }
    requestUpdate();
  }
  if (isBot) { fields = []; }
  boot();
})();
