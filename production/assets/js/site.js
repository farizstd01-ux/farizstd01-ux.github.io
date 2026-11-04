/* Shield Tech site script: navigation, chamber diagram, enquiry form. No dependencies. */
(function () {
  "use strict";
  var doc = document;

  /* ---------- Navigation ---------- */
  var header = doc.querySelector(".site-header");
  var burger = doc.querySelector(".burger");
  var menuItem = doc.querySelector(".has-menu");
  var menuBtn = menuItem && menuItem.querySelector("button");

  function closeMega() {
    if (!menuItem) return;
    menuItem.classList.remove("open");
    menuBtn.setAttribute("aria-expanded", "false");
  }
  if (burger) {
    burger.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      burger.setAttribute("aria-expanded", String(open));
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
  }
  if (menuBtn) {
    menuBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = menuItem.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", String(open));
    });
    doc.addEventListener("click", function (e) {
      if (!menuItem.contains(e.target)) closeMega();
    });
    menuItem.addEventListener("mouseenter", function () { menuBtn.setAttribute("aria-expanded", "true"); });
    menuItem.addEventListener("mouseleave", function () { if (!menuItem.classList.contains("open")) menuBtn.setAttribute("aria-expanded", "false"); });
  }
  doc.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    closeMega();
    if (header && header.classList.contains("nav-open")) {
      header.classList.remove("nav-open");
      burger.setAttribute("aria-expanded", "false");
      burger.focus();
    }
  });

  /* ---------- Chamber anatomy diagram ---------- */
  var an = doc.querySelector(".anatomy");
  if (an) {
    var buttons = an.querySelectorAll(".part");
    var modeBtns = an.querySelectorAll(".anatomy__modes button");
    var nameEl = an.querySelector(".anatomy__name");
    var textEl = an.querySelector(".anatomy__text");
    var current = "shield";

    function show(key, userAction) {
      current = key;
      if (userAction) an.classList.add("has-active");
      var mode = an.getAttribute("data-mode");
      buttons.forEach(function (b) {
        var on = b.getAttribute("data-part") === key;
        b.setAttribute("aria-pressed", String(on));
        if (on) {
          var label = b.querySelector(mode === "far" && b.querySelector(".lbl-far") ? ".lbl-far" : ".lbl-sac");
          nameEl.textContent = label ? label.textContent : b.textContent;
          textEl.textContent = b.getAttribute("data-desc-" + mode);
        }
      });
      an.querySelectorAll("svg [data-part]").forEach(function (g) {
        g.classList.toggle("is-active", g.getAttribute("data-part") === key);
      });
    }
    buttons.forEach(function (b) {
      var key = b.getAttribute("data-part");
      b.addEventListener("click", function () { show(key, true); });
      b.addEventListener("mouseenter", function () { if (window.matchMedia("(hover: hover)").matches) show(key, true); });
      b.addEventListener("focus", function () { show(key, true); });
    });
    an.querySelectorAll("svg [data-part]").forEach(function (g) {
      g.addEventListener("click", function () { show(g.getAttribute("data-part"), true); });
    });
    modeBtns.forEach(function (m) {
      m.addEventListener("click", function () {
        an.setAttribute("data-mode", m.getAttribute("data-mode"));
        modeBtns.forEach(function (x) { x.setAttribute("aria-checked", String(x === m)); });
        show(current, false);
      });
    });
    show("shield", false);
  }

  /* ---------- Enquiry form ---------- */
  var form = doc.getElementById("enquiry");
  if (form) {
    var status = form.querySelector(".form__status");
    var host = doc.body.hasAttribute("data-email") ? doc.body : (doc.querySelector(".site") || doc.body);
    var endpoint = host.getAttribute("data-form-endpoint") || "";
    var email = host.getAttribute("data-email") || "";

    function setErr(field, msg) {
      var p = field.parentNode.querySelector(".err");
      if (msg) { field.setAttribute("aria-invalid", "true"); if (p) p.textContent = msg; }
      else { field.removeAttribute("aria-invalid"); if (p) p.textContent = ""; }
    }
    function validate() {
      var ok = true;
      var firstBad = null;
      form.querySelectorAll("[required]").forEach(function (f) {
        var bad = f.type === "checkbox" ? !f.checked : !f.value.trim();
        if (!bad && f.type === "email") bad = !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value.trim());
        setErr(f, bad ? (f.type === "email" ? "Enter a valid email address." : "This field is required.") : "");
        if (bad && !firstBad) firstBad = f;
        if (bad) ok = false;
      });
      if (firstBad) firstBad.focus();
      return ok;
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (form.querySelector(".hp input").value) return;
      if (!validate()) {
        status.setAttribute("data-state", "error");
        status.textContent = "Check the highlighted fields and try again.";
        return;
      }
      var data = {};
      new FormData(form).forEach(function (v, k) { if (k !== "company_site") data[k] = v; });
      if (endpoint) {
        status.removeAttribute("data-state");
        status.textContent = "Sending your enquiry...";
        fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
          .then(function (r) {
            if (!r.ok) throw new Error("bad status");
            form.reset();
            status.setAttribute("data-state", "ok");
            status.textContent = "Thank you. We have received your enquiry and will reply by email.";
          })
          .catch(function () {
            status.setAttribute("data-state", "error");
            status.textContent = "We could not send the form. Please email " + email + " instead.";
          });
        return;
      }
      var lines = [
        "Name: " + data.name, "Company: " + data.org, "Email: " + data.email, "Phone: " + (data.phone || "-"),
        "Solution: " + data.interest, "Project location: " + (data.location || "-"), "", data.details || ""
      ];
      var href = "mailto:" + email + "?subject=" + encodeURIComponent("Quote request: " + data.interest) + "&body=" + encodeURIComponent(lines.join("\n"));
      status.setAttribute("data-state", "ok");
      status.textContent = "Your email app should open with the enquiry filled in. If nothing opens, copy the details and send them to " + email + ".";
      window.location.href = href;
    });
    form.addEventListener("input", function (e) {
      if (e.target.getAttribute("aria-invalid")) setErr(e.target, "");
    });
  }
})();
