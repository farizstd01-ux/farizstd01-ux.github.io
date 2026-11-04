"""Reusable content blocks shared across pages."""
from .core import (SITE, SOLUTIONS, SOLUTION_BY_SLUG, PARTNERS, icon, esc, section, sec_head, btn, card, grid)


def page_hero(c, trail, h1, lead, img=None, alt="", ctas=True, short=None):
    crumbs = f'<li><a href="{c.l("")}">Home</a></li>'
    for label, path in trail:
        crumbs += f'<li><a href="{c.l(path)}">{label}</a></li>'
    crumbs += f'<li aria-current="page">{short or h1}</li>'
    media = f'<div class="page-hero__media">{c.img(img, alt, eager=True, sizes="(min-width: 900px) 40vw, 92vw")}</div>' if img else ""
    solo = "" if img else " page-hero__grid--solo"
    buttons = ""
    if ctas:
        buttons = f'<div class="btn-row">{btn(c.l("contact"), "Request a quote", "light", True)}{btn(c.l("solutions"), "All solutions", "ghost")}</div>'
    return (
        f'<section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><ol>{crumbs}</ol></nav>'
        f'<div class="page-hero__grid{solo}"><div><h1>{h1}</h1><p class="lead">{lead}</p>{buttons}</div>{media}</div></div></section>'
    )


# slug -> (image name, alt)
TILE_IMAGES = {
    "anechoic-emc-test-chambers": ("sac5-side", "Steel structure of a SAC-5 semi-anechoic EMC test chamber installed in a hall"),
    "automotive-military-emc-chambers": ("auto-chamber", "Automotive EMC test chamber structure with a coach parked beside it"),
    "antenna-measurement-chambers": ("antenna-room-2", "Antenna measurement chamber lined with pyramidal absorbers around a positioner"),
    "shielded-rooms-faraday-cages": ("shielded-door", "Steel door of an RF shielded room with a locking handle"),
    "forensic-cyber-security-shielding": ("forensic-room", "Forensic facility meeting room with a shielded enclosure"),
    "tempest-emp-hemp-shielding": ("shielded-room-a", "Interior of a shielded room with the steel-lined doorway open"),
    "eeg-tem-medical-research-shielding": ("eeg-room", "Cutaway of an EEG shielded room with a desk and shielded door"),
    "magnetic-field-shielding": ("trunking", "Shielded cable trunking with bolted joints"),
    "shielded-data-centres-containers-tents": ("container-inside", "Interior of a shielded container fitted out as an office"),
    "ehv-laboratories": (None, ""),
}


def solution_tile(c, slug, text=None):
    s = SOLUTION_BY_SLUG[slug]
    img, alt = TILE_IMAGES[slug]
    if img:
        media = f'<div class="tile__img">{c.img(img, alt, sizes="(min-width: 1020px) 30vw, (min-width: 640px) 45vw, 92vw")}</div>'
    else:
        media = f'<div class="tile__img tile__img--icon">{icon("tower", "ic", 56)}</div>'
    return (
        f'<a class="tile" href="{c.s(slug)}">{media}<div class="tile__body"><h3>{s[1]}</h3><p>{text or s[2]}</p>'
        f'<span class="card__more">Explore {icon("arrow", "ic", 16)}</span></div></a>'
    )


HOME_TILE_TEXT = {
    "anechoic-emc-test-chambers": "SAC-3, SAC-5, SAC-10, FAR-3 and pre-compliant chambers for radiated emissions and immunity testing.",
    "automotive-military-emc-chambers": "Vehicle and component chambers for CISPR 25 and ISO 11452, plus MIL-STD-461 facilities.",
    "antenna-measurement-chambers": "Absorber-lined ranges for 5G, telecom, radar, marine and aerospace antennas.",
    "shielded-rooms-faraday-cages": "RF and EMI shielded enclosures in any size or shape, from research labs to secure facilities.",
    "tempest-emp-hemp-shielding": "TEMPEST rooms that contain emanations and EMP / HEMP rooms that protect command centres.",
    "shielded-data-centres-containers-tents": "Shielded data halls, ISO containers and field tents for mobile, secure operations.",
}


def process_steps(c, dark=True):
    steps = [
        ("Brief and survey", "We review your test standard, equipment, frequency range, footprint and site conditions."),
        ("Design and engineering", "Layout, shielding targets, absorbers, doors and services are drawn up for your approval."),
        ("Manufacture", "Steel structure and shielding modules are fabricated at our KEZAD facility in Abu Dhabi."),
        ("Installation", "Our installation teams and delivery partner assemble, align and connect the facility on your site."),
        ("Test and handover", "Shielding performance is verified and the facility is handed over with documentation."),
    ]
    lis = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in steps)
    return f'<ol class="steps">{lis}</ol>'


INDUSTRIES = [
    ("defence", "Defence and military",
     "MIL-STD-461 chambers, TEMPEST and EMP / HEMP rooms, and antenna ranges for radar and avionics programmes.",
     [("automotive-military-emc-chambers", "MIL-STD chambers"), ("tempest-emp-hemp-shielding", "TEMPEST and EMP"), ("antenna-measurement-chambers", "Antenna ranges")]),
    ("gov", "Government, police and embassies",
     "Secure rooms that protect sensitive information, plus forensic enclosures that keep seized devices isolated.",
     [("tempest-emp-hemp-shielding", "TEMPEST rooms"), ("forensic-cyber-security-shielding", "Forensic shielding"), ("shielded-data-centres-containers-tents", "Mobile enclosures")]),
    ("car", "Automotive and transport",
     "Vehicle and component chambers for emissions and immunity testing, up to 10 m facilities that take complete vehicles.",
     [("automotive-military-emc-chambers", "CISPR 25 and ISO 11452"), ("anechoic-emc-test-chambers", "SAC-10 chambers")]),
    ("antenna", "Telecom, 5G and wireless",
     "Antenna measurement ranges and compact Wi-Fi test chambers for manufacturers, integrators and research teams.",
     [("antenna-measurement-chambers", "Antenna chambers"), ("anechoic-emc-test-chambers", "EMC chambers")]),
    ("medical", "Healthcare, universities and research",
     "Shielded rooms for EEG recording and electron microscopes, where low-level signals must be protected from interference.",
     [("eeg-tem-medical-research-shielding", "EEG and TEM rooms"), ("shielded-rooms-faraday-cages", "Shielded rooms")]),
    ("server", "Data centres, energy and utilities",
     "Shielded data halls, magnetic field shielding for substations and plant rooms, and extra-high-voltage laboratories.",
     [("shielded-data-centres-containers-tents", "Shielded data centres"), ("magnetic-field-shielding", "Magnetic shielding"), ("ehv-laboratories", "EHV labs")]),
]


def industry_cards(c):
    out = []
    for ic, title, text, links in INDUSTRIES:
        ls = "".join(f'<li><a href="{c.s(s)}">{t}</a></li>' for s, t in links)
        out.append(f'<div class="ind"><span class="card__ic">{icon(ic)}</span><h3>{title}</h3><p>{text}</p><ul>{ls}</ul></div>')
    return out


def partners_html(c):
    items = "".join(f'<div class="partner">{c.img(p["img"], p["name"], sizes="280px")}</div>' for p in PARTNERS)
    return f'<div class="partners">{items}</div>'


def model_card(name, kind, text, uses, img_html="", mid=""):
    media = f'<div class="model__img">{img_html}</div>' if img_html else ""
    ident = f' id="{mid}"' if mid else ""
    return (
        f'<article class="model"{ident}>{media}<h3 class="model__name">{name}</h3><p class="model__type">{kind}</p><p>{text}</p>'
        f'<dl><dt>Typical use</dt><dd>{uses}</dd></dl></article>'
    )
