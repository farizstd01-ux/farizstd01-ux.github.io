"""Shield Tech site generator: configuration, URL helpers, icons and the page shell."""
import html as _html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")

# --------------------------------------------------------------------------
# Company data. Anything marked CONFIRM should be checked by Shield Tech.
# --------------------------------------------------------------------------
SITE = {
    "name": "Shield Tech",
    "legal": "Shield Tech Steel Manufacturing LLC",
    "url": "https://www.shieldtech.ae",
    "domain": "www.shieldtech.ae",
    "email": "info@shieldtech.ae",          # CONFIRM: mailbox must exist
    "phone": "",                            # CONFIRM: add to show phone in header, footer, contact page and schema
    "street": "KEZAD Logistics Park, ICAD 3",
    "city": "Abu Dhabi",
    "country": "United Arab Emirates",
    "country_code": "AE",
    "year": 2026,
    "form_endpoint": "",                    # optional: URL of a form-to-email service; blank = opens visitor's mail app
    "map_link": "https://www.google.com/maps/search/?api=1&query=KEZAD+Logistics+Park+ICAD+3+Abu+Dhabi",
}

PARTNERS = [
    {"name": "Kemar EMC Electromechanical Equipment Installations LLC", "group": "Kemar EMC", "img": "partner-kemar"},
]

# Solutions in navigation order: (slug, short title, one-line descriptor, icon, group)
SOLUTIONS = [
    ("anechoic-emc-test-chambers", "Anechoic EMC test chambers", "SAC-3, SAC-5, SAC-10, FAR-3 and pre-compliant rooms", "chamber", "Test chambers"),
    ("automotive-military-emc-chambers", "Automotive and military chambers", "CISPR 25, ISO 11452 and MIL-STD-461 facilities", "car", "Test chambers"),
    ("antenna-measurement-chambers", "Antenna measurement chambers", "5G, radar, telecom and wireless antenna ranges", "antenna", "Test chambers"),
    ("shielded-rooms-faraday-cages", "Shielded rooms and Faraday cages", "RF/EMI enclosures built in any size or shape", "shield", "Shielded rooms"),
    ("forensic-cyber-security-shielding", "Forensic and cyber security shielding", "Evidence rooms and portable evidence boxes", "lock", "Shielded rooms"),
    ("tempest-emp-hemp-shielding", "TEMPEST and EMP / HEMP shielding", "Secure facilities and pulse protection", "bolt", "Shielded rooms"),
    ("eeg-tem-medical-research-shielding", "EEG, TEM and research shielding", "Hospitals, universities and laboratories", "pulse", "Shielded rooms"),
    ("magnetic-field-shielding", "Magnetic field shielding", "Shielded trunking, transformer and switchgear shielding", "magnet", "Specialist"),
    ("shielded-data-centres-containers-tents", "Data centres, containers and tents", "Modular and mobile shielded enclosures", "server", "Specialist"),
    ("ehv-laboratories", "EHV laboratories", "Extra-high-voltage test halls and lighting chambers", "tower", "Specialist"),
]
SOLUTION_BY_SLUG = {s[0]: s for s in SOLUTIONS}

TOP_NAV = [
    ("industries", "Industries"),
    ("standards", "Standards"),
    ("about", "About"),
    ("contact", "Contact"),
]

_MANIFEST = json.load(open(os.path.join(SRC, "assets", "img", "_manifest.json")))


def esc(s):
    return _html.escape(str(s), quote=True)


# --------------------------------------------------------------------------
# Context: builds links and asset URLs for a given output mode and page depth
#   prod     -> root-absolute clean URLs (/solutions/x/), for the live domain
#   local    -> relative links ending in index.html, opens straight from disk
#   artifact -> same as local, but Poppins loads from Google Fonts
# --------------------------------------------------------------------------
class Ctx:
    def __init__(self, mode, path):
        self.mode = mode
        self.path = path  # "" for home, "solutions/x" otherwise
        self.depth = 0 if path == "" else path.count("/") + 1

    @property
    def up(self):
        return "../" * self.depth

    def l(self, path="", frag=""):
        if self.mode == "prod":
            u = "/" if path == "" else "/" + path.strip("/") + "/"
        else:
            u = self.up + ("index.html" if path == "" else path.strip("/") + "/index.html")
            if path == "" and self.depth == 0:
                u = "index.html"
        return u + frag

    def s(self, slug, frag=""):
        return self.l("solutions/" + slug, frag)

    def a(self, asset):
        if self.mode == "prod":
            return "/assets/" + asset
        return self.up + "assets/" + asset

    def abs(self, path=""):
        return SITE["url"] + ("/" if path == "" else "/" + path.strip("/") + "/")

    def img(self, name, alt, cls="", sizes="(min-width: 900px) 40vw, 92vw", eager=False, ext="webp", w=None, h=None):
        m = _MANIFEST.get(name, {})
        w = w or m.get("w")
        h = h or m.get("h")
        dims = f' width="{w}" height="{h}"' if w and h else ""
        load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
        c = f' class="{cls}"' if cls else ""
        return f'<img{c} src="{self.a("img/" + name + "." + ext)}" alt="{esc(alt)}"{dims}{load}>'


# --------------------------------------------------------------------------
# Icons (24px grid, stroke based, inherit currentColor)
# --------------------------------------------------------------------------
_ICONS = {
    "shield": '<path d="M12 3 4.5 5.8v5.4c0 4.4 3 8.2 7.5 9.8 4.5-1.6 7.5-5.4 7.5-9.8V5.8L12 3Z"/><path d="m8.8 12 2.3 2.3 4.2-4.6"/>',
    "chamber": '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5v-9Z"/><path d="m3 7.5 9 4.5 9-4.5M12 12v9"/>',
    "antenna": '<path d="M12 12.5V21M8.5 21h7"/><circle cx="12" cy="10.5" r="1.6"/><path d="M8.6 7.1a4.8 4.8 0 0 0 0 6.8M15.4 7.1a4.8 4.8 0 0 1 0 6.8M5.6 4.4a8.8 8.8 0 0 0 0 12.2M18.4 4.4a8.8 8.8 0 0 1 0 12.2"/>',
    "car": '<path d="M4.5 16.5V13l1.7-4.3A2 2 0 0 1 8.1 7.5h7.8a2 2 0 0 1 1.9 1.2L19.5 13v3.5"/><path d="M3.5 13h17M7 16.5v2M17 16.5v2M7.5 15.2h.01M16.5 15.2h.01"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="1.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5M12 14.5v2.5"/>',
    "bolt": '<path d="M13 2.5 5 13.5h6l-1 8 8-11h-6l1-8Z"/>',
    "pulse": '<path d="M2.5 12h4l2.2-6 3.6 12 2.6-9 1.6 3h5"/>',
    "magnet": '<path d="M5 3.5v8a7 7 0 0 0 14 0v-8h-4v8a3 3 0 0 1-6 0v-8H5Z"/><path d="M5 7.5h4M15 7.5h4"/>',
    "server": '<rect x="3.5" y="4" width="17" height="6" rx="1"/><rect x="3.5" y="14" width="17" height="6" rx="1"/><path d="M7 7h.01M7 17h.01M11 7h5M11 17h5"/>',
    "container": '<path d="M3 7h18v10H3zM7 7v10M11 7v10M15 7v10M19 7v10"/>',
    "tent": '<path d="M3 20 12 4l9 16H3Z"/><path d="M12 4v16M9.2 20l2.8-6 2.8 6"/>',
    "tower": '<path d="M12 3 7 21M12 3l5 18M9.3 11h5.4M8 16h8M10.5 7h3"/>',
    "pin": '<path d="M12 21s7-6.2 7-11.5a7 7 0 1 0-14 0C5 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
    "phone": '<path d="M6.5 3.5h3l1.3 4-2 1.3a10 10 0 0 0 5 5l1.3-2 4 1.3v3a2 2 0 0 1-2 2A14.5 14.5 0 0 1 4.5 5.5a2 2 0 0 1 2-2Z"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "gov": '<path d="M3 21h18M5.5 21V10.5M9.8 21V10.5M14.2 21V10.5M18.5 21V10.5M2.8 10 12 4l9.2 6H2.8Z"/>',
    "medical": '<path d="M9 3.5h6V9h5.5v6H15v5.5H9V15H3.5V9H9V3.5Z"/>',
    "defence": '<path d="M12 3 4.5 5.8v5.4c0 4.4 3 8.2 7.5 9.8 4.5-1.6 7.5-5.4 7.5-9.8V5.8L12 3Z"/><path d="m12 8 1.2 2.6 2.8.3-2.1 1.9.6 2.8L12 14.2l-2.5 1.4.6-2.8L8 10.9l2.8-.3L12 8Z"/>',
    "factory": '<path d="M3.5 20.5v-9l6 3v-3l6 3V6.5h5v14h-17Z"/><path d="M8 17.5h.01M12 17.5h.01M16.5 17.5h.01"/>',
    "layers": '<path d="m12 3.5 8.5 4.5-8.5 4.5L3.5 8 12 3.5Z"/><path d="m3.5 12.5 8.5 4.5 8.5-4.5M3.5 16.5l8.5 4.5 8.5-4.5"/>',
    "pencil": '<path d="m4 20 1-4L16.6 4.4a2 2 0 0 1 3 3L8 19l-4 1Z"/><path d="m14.5 6.5 3 3"/>',
    "doc": '<path d="M7 3h8l4 4v14H7V3Z"/><path d="M15 3v4h4M10 12h6M10 16h6"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "signal": '<path d="M3 12h3l2-5 4 10 2.5-7 1.5 2H21"/>',
    "ruler": '<path d="M3 17 17 3l4 4L7 21l-4-4Z"/><path d="m7.5 12.5 2 2M10.5 9.5l2 2M13.5 6.5l2 2"/>',
    "wave": '<path d="M2.5 12c2-5 3.8-5 5.5 0s3.5 5 5.500 0 3.500-5 5.500 0 .5 2.500 .5 2.500"/>',
    "wrench": '<path d="M14.5 6a4 4 0 0 0 4.9 4.9L21 12.500 12.500 21 3 11.500 11.500 3l3 3Z"/>',
    "box": '<path d="M4 8.500 12 4l8 4.500v7L12 20l-8-4.500v-7Z"/><path d="M4 8.500 12 13l8-4.500M12 13v7"/>',
    "clock": '<circle cx="12" cy="12" r="8.500"/><path d="M12 7.500V12l3 2"/>',
}


def icon(name, cls="ic", size=24):
    body = _ICONS.get(name, _ICONS["shield"])
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{body}</svg>')


# --------------------------------------------------------------------------
# Small HTML helpers used by every page
# --------------------------------------------------------------------------
def section(inner, cls="", id="", tone=""):
    idp = f' id="{id}"' if id else ""
    t = f" sec--{tone}" if tone else ""
    c = f" {cls}" if cls else ""
    return f'<section class="sec{t}{c}"{idp}><div class="wrap">{inner}</div></section>'


def sec_head(h2, lead="", cls=""):
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    c = f" {cls}" if cls else ""
    return f'<div class="sec-head{c}"><h2>{h2}</h2>{lead_html}</div>'


def btn(href, label, kind="primary", arrow=False, cls=""):
    a = icon("arrow", "ic ic--btn", 18) if arrow else ""
    return f'<a class="btn btn--{kind} {cls}" href="{href}"><span>{label}</span>{a}</a>'


def card(ic, title, text, href=None, cls=""):
    inner = f'<span class="card__ic">{icon(ic)}</span><h3>{title}</h3><p>{text}</p>'
    if href:
        inner += f'<span class="card__more">Learn more {icon("arrow", "ic", 16)}</span>'
        return f'<a class="card card--link {cls}" href="{href}">{inner}</a>'
    return f'<div class="card {cls}">{inner}</div>'


def grid(items, cols=3, cls=""):
    return f'<div class="grid grid--{cols} {cls}">{"".join(items)}</div>'


def checklist(items, cls=""):
    lis = "".join(f'<li>{icon("check", "ic", 18)}<span>{i}</span></li>' for i in items)
    return f'<ul class="checks {cls}">{lis}</ul>'


def table(headers, rows, caption="", cls=""):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    trs = ""
    for r in rows:
        tds = f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:])
        trs += f"<tr>{tds}</tr>"
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'<div class="table-wrap {cls}"><table class="spec">{cap}<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def split(media_html, inner, flip=False, cls=""):
    f = " split--flip" if flip else ""
    c = f" {cls}" if cls else ""
    return f'<div class="split{f}{c}"><div class="split__media">{media_html}</div><div class="split__body">{inner}</div></div>'


def faq_html(items, h2="Frequently asked questions"):
    if not items:
        return ""
    rows = "".join(
        f'<details class="faq__item"><summary><span>{q}</span>{icon("chev", "ic faq__chev", 20)}</summary><div class="faq__a"><p>{a}</p></div></details>'
        for q, a in items
    )
    return section(f'{sec_head(h2)}<div class="faq">{rows}</div>', tone="tint", id="faq")


def strip_tags(s):
    out, inside = [], False
    for ch in s:
        if ch == "<":
            inside = True
        elif ch == ">":
            inside = False
        elif not inside:
            out.append(ch)
    return _html.unescape("".join(out)).strip()


def cta_band(c, title="Tell us what you need to shield or test", text="Share your standard, frequency range, footprint and timeline. Our engineers will come back with a clear recommendation and a scoped quotation.", label="Request a quote"):
    return (
        '<section class="cta-band"><div class="cta-band__bg" aria-hidden="true">'
        f'{c.img("cta-absorbers", "", cls="cta-band__img")}</div>'
        f'<div class="wrap cta-band__in"><div><h2>{title}</h2><p>{text}</p></div>'
        f'<div class="btn-row">{btn(c.l("contact"), label, "light", True)}'
        f'{btn(c.l("solutions"), "Browse solutions", "ghost")}</div></div></section>'
    )


def related(c, slugs, h2="Related solutions"):
    cards = []
    for s in slugs:
        slug, title, desc, ic, _ = SOLUTION_BY_SLUG[s]
        cards.append(card(ic, title, desc, c.s(slug)))
    return section(sec_head(h2) + grid(cards, 3), tone="")


# --------------------------------------------------------------------------
# Page shell
# --------------------------------------------------------------------------
def _nav_html(c, current):
    groups = {}
    for slug, title, desc, ic, g in SOLUTIONS:
        groups.setdefault(g, []).append((slug, title, desc, ic))
    cols = ""
    for g, items in groups.items():
        lis = "".join(
            f'<li><a href="{c.s(slug)}"{" aria-current=\"page\"" if current == "solutions/" + slug else ""}>'
            f'<span class="mega__ic">{icon(ic, "ic", 22)}</span><span><strong>{title}</strong><small>{desc}</small></span></a></li>'
            for slug, title, desc, ic in items
        )
        cols += f'<div class="mega__col"><p class="mega__h">{g}</p><ul>{lis}</ul></div>'
    sol_cur = ' aria-current="true"' if current.startswith("solutions") else ""
    nav = (
        f'<li class="has-menu"><button type="button" class="nav-link" aria-expanded="false" aria-controls="mega"{sol_cur}>'
        f'<span>Solutions</span>{icon("chev", "ic ic--chev", 16)}</button>'
        f'<div class="mega" id="mega"><div class="mega__grid">{cols}</div>'
        f'<a class="mega__all" href="{c.l("solutions")}">View all solutions {icon("arrow", "ic", 16)}</a></div></li>'
    )
    for slug, label in TOP_NAV:
        cur = ' aria-current="page"' if current == slug else ""
        nav += f'<li><a class="nav-link" href="{c.l(slug)}"{cur}><span>{label}</span></a></li>'
    return nav


def header_html(c, current):
    logo_l = c.img("logo", "Shield Tech", cls="logo logo--on-light", eager=False, ext="png", w=190, h=91).replace(' loading="lazy" decoding="async"', ' decoding="async"')
    logo_d = c.img("logo-light", "", cls="logo logo--on-dark", ext="png", w=190, h=91).replace(' loading="lazy" decoding="async"', ' decoding="async"')
    return (
        '<a class="skip" href="#main">Skip to content</a>'
        '<header class="site-header" id="top"><div class="wrap bar">'
        f'<a class="brand" href="{c.l("")}" aria-label="Shield Tech home">{logo_l}{logo_d}</a>'
        f'<nav class="nav" id="nav" aria-label="Main"><ul>{_nav_html(c, current)}</ul>'
        f'<a class="btn btn--primary btn--sm nav__cta" href="{c.l("contact")}"><span>Request a quote</span></a></nav>'
        f'<button type="button" class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav">{icon("menu", "ic ic--open", 26)}{icon("close", "ic ic--shut", 26)}</button>'
        "</div></header>"
    )


def footer_html(c):
    cols = {}
    for slug, title, desc, ic, g in SOLUTIONS:
        cols.setdefault(g, []).append((slug, title))
    sol = ""
    for g, items in cols.items():
        sol += f'<div class="foot__col"><p class="foot__h">{g}</p><ul>' + "".join(f'<li><a href="{c.s(s)}">{t}</a></li>' for s, t in items) + "</ul></div>"
    phone = f'<li>{icon("phone", "ic", 18)}<a href="tel:{esc(SITE["phone"].replace(" ", ""))}">{esc(SITE["phone"])}</a></li>' if SITE["phone"] else ""
    return (
        '<footer class="site-footer"><div class="foot__mesh" aria-hidden="true"></div><div class="wrap">'
        '<div class="foot__top">'
        f'<div class="foot__brand"><a href="{c.l("")}" aria-label="Shield Tech home">{c.img("logo-light", "Shield Tech", cls="logo", ext="png", w=200, h=96)}</a>'
        '<p>Manufacturers of EMC anechoic chambers, antenna measurement chambers, Faraday cages and shielded rooms in Abu Dhabi, United Arab Emirates.</p></div>'
        f'<div class="foot__cols">{sol}'
        f'<div class="foot__col"><p class="foot__h">Company</p><ul>'
        f'<li><a href="{c.l("about")}">About Shield Tech</a></li><li><a href="{c.l("industries")}">Industries</a></li>'
        f'<li><a href="{c.l("standards")}">Standards</a></li><li><a href="{c.l("contact")}">Contact and quotes</a></li>'
        f'<li><a href="{c.l("privacy")}">Privacy policy</a></li></ul></div></div></div>'
        '<div class="foot__mid">'
        f'<address><p class="foot__h">Visit or write to us</p><ul class="foot__contact">'
        f'<li>{icon("pin", "ic", 18)}<span>{esc(SITE["legal"])}<br>{esc(SITE["street"])}<br>{esc(SITE["city"])}, {esc(SITE["country"])}</span></li>'
        f'<li>{icon("mail", "ic", 18)}<a href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a></li>{phone}</ul></address>'
        f'<div><p class="foot__h">Delivery partner</p><p class="foot__partners">Kemar EMC Electromechanical Equipment Installations LLC</p></div>'
        "</div>"
        f'<div class="foot__bottom"><p>&copy; {SITE["year"]} {esc(SITE["legal"])}. All rights reserved.</p>'
        f'<p><a href="{SITE["url"]}">{esc(SITE["domain"])}</a></p></div>'
        "</div></footer>"
    )


def org_schema(c):
    org = {
        "@type": ["Organization", "LocalBusiness"],
        "@id": SITE["url"] + "/#organization",
        "name": SITE["name"],
        "legalName": SITE["legal"],
        "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/assets/img/logo.png",
        "image": SITE["url"] + "/assets/img/og-card.jpg",
        "description": "Manufacturer of EMC anechoic chambers, antenna measurement chambers, Faraday cages and shielded rooms in Abu Dhabi, UAE.",
        "email": SITE["email"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["street"],
            "addressLocality": SITE["city"],
            "addressCountry": SITE["country_code"],
        },
        "areaServed": [{"@type": "Country", "name": "United Arab Emirates"}, {"@type": "Place", "name": "GCC"}],
        "knowsAbout": [
            "EMC anechoic chambers", "Semi-anechoic chambers", "Antenna measurement chambers", "Faraday cages",
            "RF shielded rooms", "TEMPEST shielding", "EMP and HEMP shielding", "Forensic shielded rooms",
        ],
    }
    if SITE["phone"]:
        org["telephone"] = SITE["phone"]
    return org


def render_page(page, mode):
    """page: dict with path, title, description, h1_in_body (bool), body_fn(c)->str, faq, schema, og_image, hero_img (for preload), robots"""
    c = Ctx(mode, page["path"])
    body = page["body"](c)
    faq = page.get("faq") or []
    url = c.abs(page["path"])
    title = page["title"]
    desc = page["description"]
    og_img = SITE["url"] + "/assets/img/" + page.get("og_image", "og-card.jpg")

    # JSON-LD graph
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE["url"] + "/"}]
    for i, (label, p) in enumerate(page.get("crumbs", []), start=2):
        crumbs.append({"@type": "ListItem", "position": i, "name": strip_tags(label), "item": c.abs(p) if p is not None else url})
    graph = [org_schema(c)]
    if page["path"] == "":
        graph.append({"@type": "WebSite", "@id": SITE["url"] + "/#website", "url": SITE["url"] + "/", "name": SITE["name"], "publisher": {"@id": SITE["url"] + "/#organization"}, "inLanguage": "en"})
    graph.append({"@type": page.get("webpage_type", "WebPage"), "@id": url + "#webpage", "url": url, "name": title, "description": desc, "isPartOf": {"@id": SITE["url"] + "/#website"} if page["path"] == "" else {"@type": "WebSite", "url": SITE["url"] + "/"}, "inLanguage": "en", "primaryImageOfPage": {"@type": "ImageObject", "url": og_img}})
    if len(crumbs) > 1:
        graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    if page.get("service"):
        s = page["service"]
        graph.append({
            "@type": "Service", "name": s["name"], "serviceType": s.get("type", s["name"]), "description": desc, "url": url,
            "provider": {"@id": SITE["url"] + "/#organization"}, "areaServed": {"@type": "Country", "name": "United Arab Emirates"},
        })
    if faq:
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faq]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)

    fonts = ""
    if mode == "artifact":
        fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap">')
    elif mode == "local":
        fonts = ""
    else:
        fonts = (f'<link rel="preload" href="{c.a("fonts/poppins-latin-400-normal.woff2")}" as="font" type="font/woff2" crossorigin>'
                 f'<link rel="preload" href="{c.a("fonts/poppins-latin-700-normal.woff2")}" as="font" type="font/woff2" crossorigin>')
    css_name = "css/site.artifact.css" if mode == "artifact" else "css/site.css"
    preload_img = ""
    if page.get("hero_img"):
        preload_img = f'<link rel="preload" as="image" href="{c.a("img/" + page["hero_img"] + ".webp")}" fetchpriority="high">'

    robots = page.get("robots", "index,follow,max-image-preview:large,max-snippet:-1")
    canon = "" if robots.startswith("noindex") else f'<link rel="canonical" href="{url}">'
    head = (
        '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="cover">'
        f'<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">'
        f'{canon}<meta name="robots" content="{robots}">'
        f'<meta property="og:type" content="website"><meta property="og:site_name" content="{SITE["name"]}">'
        f'<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">'
        f'<meta property="og:url" content="{url}"><meta property="og:image" content="{og_img}">'
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_AE">'
        '<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{og_img}">'
        '<meta name="theme-color" content="#084771">'
        f'<link rel="icon" href="{c.a("img/favicon.ico")}" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="{c.a("img/favicon-32.png")}">'
        f'<link rel="apple-touch-icon" href="{c.a("img/apple-touch-icon.png")}"><link rel="manifest" href="{c.a("site.webmanifest")}">'
        f'{fonts}{preload_img}<link rel="stylesheet" href="{c.a(css_name)}"><link rel="stylesheet" href="{c.a("css/motion.css")}">'
        '<script>(function(){var d=document.documentElement,m=0;try{m=localStorage.getItem("shieldtech-motion")==="off"}catch(e){}d.className+=(window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches)||m?" fx-off":" fx"})()</script>'
        f'<script type="application/ld+json">{ld}</script>'
    )
    cls = page.get("body_class", "")
    inner = (
        f'{header_html(c, page["path"])}<main id="main">{body}</main>{footer_html(c)}'
        f'<script src="{c.a("js/site.js")}" defer></script>'
        f'<script src="{c.a("js/motion.js")}" defer></script>'
    )
    if mode == "artifact" and page["path"] == "":
        # The publish step wraps the main page in its own document skeleton, so emit a fragment.
        return head.replace('<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">', "") + f'<div class="site {cls}" data-form-endpoint="{esc(SITE["form_endpoint"])}" data-email="{esc(SITE["email"])}">{inner}</div>'
    return (
        f'<!doctype html><html lang="en"><head>{head}</head>'
        f'<body class="{cls}" data-form-endpoint="{esc(SITE["form_endpoint"])}" data-email="{esc(SITE["email"])}">{inner}</body></html>'
    )
