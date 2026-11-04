"""Home, company and utility pages."""
from .core import (SITE, SOLUTIONS, icon, esc, section, sec_head, btn, card, grid, checklist, table, split, faq_html, cta_band, related)
from .art import hero_art, anatomy
from .blocks import (page_hero, solution_tile, HOME_TILE_TEXT, process_steps, industry_cards, partners_html, INDUSTRIES)

# ---------------------------------------------------------------------------
HOME_FAQ = [
    ("What is an anechoic chamber used for?",
     "An anechoic chamber is a shielded room lined with radio-absorbing material. It lets engineers measure the signals a product emits, or test how it behaves under interference, without outside noise or reflections affecting the result. Typical uses are EMC compliance testing, automotive and military qualification, and antenna measurements."),
    ("What is the difference between a semi-anechoic and a fully anechoic chamber?",
     "A semi-anechoic chamber (SAC) has absorbers on the walls and ceiling and a reflective metal floor, which many emissions standards require. A fully anechoic chamber (FAR) also has absorbers on the floor, so there are no ground reflections and the antenna can stay at one height. FAR rooms are smaller and quicker to test in; SAC rooms are used where a standard specifies a ground plane."),
    ("Do you manufacture in the UAE?",
     "Yes. Shield Tech Steel Manufacturing LLC fabricates chambers and shielded rooms at KEZAD Logistics Park, ICAD 3, in Abu Dhabi."),
    ("Can you build to a custom size or specification?",
     "Yes. Shielded rooms can be manufactured in any size or shape, and chambers are configured around your test standard, product size and building. Send your requirements through the quote form and an engineer will respond."),
]


def home(c):
    hero = f'''<section class="hero">
<div class="hero__bg" aria-hidden="true">{c.img("hero-absorbers", "", cls="hero__img", eager=True, sizes="100vw")}</div><div class="hero__mesh" aria-hidden="true"></div>
<div class="wrap hero__grid"><div class="hero__copy">
<p class="hero__place">{icon("pin", "ic", 18)}<span>Abu Dhabi, United Arab Emirates</span></p>
<h1>Anechoic chambers and shielded rooms, built in the UAE</h1>
<p class="lead">Shield Tech designs and manufactures EMC test chambers, antenna ranges, Faraday cages and secure shielded rooms. More than two decades of chamber experience, now backed by steel fabrication in KEZAD, Abu Dhabi.</p>
<div class="btn-row">{btn(c.l("contact"), "Request a quote", "light", True)}{btn(c.s("anechoic-emc-test-chambers"), "Explore chambers", "ghost")}</div>
<ul class="tags" aria-label="Solutions"><li>SAC-3, SAC-5, SAC-10</li><li>FAR-3</li><li>CISPR 25 and MIL-STD-461</li><li>TEMPEST</li><li>EMP and HEMP</li><li>Forensic Faraday cages</li></ul>
</div><div class="hero__art">{hero_art(c)}</div></div></section>'''

    facts = f'''<div class="facts-wrap"><div class="wrap"><ul class="facts">
<li><strong>20+ years</strong><span>Experience in EMC anechoic, antenna and Wi-Fi chambers</span></li>
<li><strong>3 m, 5 m, 10 m</strong><span>Semi-anechoic test distances, plus FAR-3 and pre-compliant rooms</span></li>
<li><strong>Over 100 dB</strong><span>Shielding in our portable forensic evidence box</span></li>
<li><strong>Abu Dhabi</strong><span>Steel fabrication at KEZAD Logistics Park, ICAD 3</span></li></ul></div></div>'''

    tiles = [solution_tile(c, s, HOME_TILE_TEXT[s]) for s in HOME_TILE_TEXT]
    sols = section(
        sec_head("What we design and manufacture", "From a 3 m compliance chamber to a portable forensic evidence box, every Shield Tech enclosure is engineered around your standard, site and budget.")
        + grid(tiles, 3) + f'<p class="more-link">{btn(c.l("solutions"), "See all ten solution areas", "outline", True)}</p>', id="solutions")

    anat = section(
        sec_head("How an anechoic chamber works", "A chamber has two jobs: keep the outside world out, and stop the walls from bouncing signals back. Switch between the two chamber types and select a part to see what it does.")
        + anatomy(c)
        + f'<p class="more-link">{btn(c.s("anechoic-emc-test-chambers"), "Compare SAC and FAR chambers", "outline", True)}</p>', tone="tint", id="how-it-works")

    why_cards = [
        card("factory", "Made in Abu Dhabi", "Steel structures and shielding modules are fabricated in the UAE at KEZAD, so design, production and site support run through one team."),
        card("pencil", "Engineered to your brief", "No two sites are alike. We size, configure and detail every chamber and shielded room around your standard, footprint and building."),
        card("signal", "Two decades in EMC chambers", "Our team has worked on anechoic, antenna and Wi-Fi chambers for over twenty years, from compact pre-compliance rooms to 10 m facilities."),
        card("link", "Delivered with a local partner", "We work with Kemar EMC Electromechanical Equipment Installations LLC to support delivery in the field."),
    ]
    why = section(sec_head("Why teams choose Shield Tech", "One manufacturer for the shield, the absorbers and the finished facility.") + grid(why_cards, 4), tone="dark", id="why")

    inds = section(
        sec_head("Industries we serve", "Our chambers and shielded rooms support defence, government, automotive, telecom, healthcare and critical infrastructure projects.")
        + grid(industry_cards(c), 3) + f'<p class="more-link">{btn(c.l("industries"), "Explore industries", "outline", True)}</p>')

    proc = section(sec_head("From brief to handover", "A clear route from first conversation to a verified, documented facility.") + process_steps(c), tone="dark", id="process")

    partners = section(
        sec_head("Delivered with a trusted partner", "Shield Tech works closely with Kemar EMC to meet each client's specific needs.")
        + partners_html(c))

    return hero + facts + sols + anat + why + inds + proc + partners + faq_html(HOME_FAQ) + cta_band(c)


# ---------------------------------------------------------------------------
def about(c):
    hero = page_hero(c, [], "About Shield Tech",
                     "Shield Tech Steel Manufacturing LLC builds EMC anechoic chambers, antenna measurement chambers, Faraday cages and shielded rooms in Abu Dhabi.",
                     img="shielded-room-a", alt="Interior of a shielded room built by Shield Tech", short="About")
    who = section(split(
        c.img("far3-interior", "Interior of a fully anechoic chamber with white absorbers and a turntable"),
        f'''<h2>Two decades of chamber experience, built for the UAE market</h2>
<p>We bring more than twenty years of experience in EMC anechoic chambers, antenna chambers and Wi-Fi chambers to the region. Our work also covers cyber security and forensic Faraday cages, removable shielded containers and a wide range of other shielding technologies.</p>
<p>Working closely with Kemar EMC, we plan every project around the specific needs of the client, drawing on years of industry experience. Where a standard product does not fit, we offer custom design solutions.</p>''',
    ))
    pillars = section(sec_head("What sets us apart") + grid([
        card("factory", "UAE manufacturing", "Fabrication takes place at KEZAD Logistics Park in Abu Dhabi, close to the sites we serve."),
        card("pencil", "Custom engineering", "Chambers and shielded rooms are configured to your standard, frequency range, footprint and building constraints."),
        card("layers", "A full range", "Test chambers, secure rooms and specialist shielding come from one supplier, so interfaces between systems are managed for you."),
        card("link", "Local delivery partner", "Kemar EMC Electromechanical Equipment Installations LLC supports delivery in the field."),
    ], 4), tone="tint")
    caps = section(sec_head("Our capabilities", "Ten solution areas, each with its own page.") + checklist([
        f'<a href="{c.s(s[0])}">{s[1]}</a>' for s in SOLUTIONS
    ], "checks--2"))
    proc = section(sec_head("How we work", "The same five steps apply from a compact shielded room to a 10 m chamber.") + process_steps(c), tone="dark")
    details = section(sec_head("Company details") + table(
        ["Item", "Detail"],
        [
            ["Legal name", esc(SITE["legal"])],
            ["Location", f'{esc(SITE["street"])}, {esc(SITE["city"])}, {esc(SITE["country"])}'],
            ["Website", f'<a href="{SITE["url"]}">{esc(SITE["domain"])}</a>'],
            ["Delivery partner", "Kemar EMC Electromechanical Equipment Installations LLC"],
            ["Core products", "Anechoic EMC chambers, antenna chambers, shielded rooms and Faraday cages, shielded containers, tents and data centres"],
        ]))
    partners = section(sec_head("Our partner") + partners_html(c), tone="tint")
    return hero + who + pillars + caps + proc + details + partners + cta_band(c)


# ---------------------------------------------------------------------------
CHOOSER = [
    ("Test a product for EMC compliance", "anechoic-emc-test-chambers", "Anechoic EMC test chambers"),
    ("Qualify a vehicle, component or military system", "automotive-military-emc-chambers", "Automotive and military chambers"),
    ("Measure antenna patterns and wireless performance", "antenna-measurement-chambers", "Antenna measurement chambers"),
    ("Keep radio signals out of a lab or equipment room", "shielded-rooms-faraday-cages", "Shielded rooms and Faraday cages"),
    ("Isolate seized phones and digital evidence", "forensic-cyber-security-shielding", "Forensic and cyber security shielding"),
    ("Protect classified information or command centres", "tempest-emp-hemp-shielding", "TEMPEST and EMP / HEMP shielding"),
    ("Record EEG or run an electron microscope", "eeg-tem-medical-research-shielding", "EEG, TEM and research shielding"),
    ("Reduce magnetic fields from cables or transformers", "magnetic-field-shielding", "Magnetic field shielding"),
    ("Deploy a modular or mobile secure space", "shielded-data-centres-containers-tents", "Data centres, containers and tents"),
    ("Build a high-voltage test hall", "ehv-laboratories", "EHV laboratories"),
]


def solutions_hub(c):
    hero = page_hero(c, [], "EMC chambers, Faraday cages and shielding solutions",
                     "Ten solution areas from one UAE manufacturer: test chambers that measure, and shielded rooms that protect.",
                     img="sac3-exterior", alt="Render of a SAC-3 chamber structure installed in a large hall", short="Solutions")
    groups = {}
    for slug, title, desc, ic, g in SOLUTIONS:
        groups.setdefault(g, []).append(slug)
    blurbs = {
        "Test chambers": "Chambers for emissions, immunity and antenna measurements.",
        "Shielded rooms": "Enclosures that keep signals out, or keep them in.",
        "Specialist": "Magnetic, modular and high-voltage environments.",
    }
    sections = ""
    for i, (g, slugs) in enumerate(groups.items()):
        sections += section(sec_head(g, blurbs[g]) + grid([solution_tile(c, s) for s in slugs], 3), tone="tint" if i % 2 else "")
    rows = [[q, f'<a href="{c.s(s)}">{t}</a>'] for q, s, t in CHOOSER]
    choose = section(sec_head("Which solution do you need?", "Start with what you need to achieve.") + table(["If you need to...", "Start here"], rows), tone="tint")
    return hero + sections + choose + cta_band(c)


# ---------------------------------------------------------------------------
def industries(c):
    hero = page_hero(c, [], "Industries we serve",
                     "Shielding and EMC test facilities for the sectors where radio-frequency performance, security and safety matter most.",
                     short="Industries")
    cards = section(grid(industry_cards(c), 3))
    detail = section(sec_head("Where our solutions are used") + f'''<div class="prose"><p>Shield Tech chambers and rooms are specified wherever a radio-frequency environment has to be controlled. <strong>Test facilities</strong> need clean, repeatable conditions so that emissions and immunity results can be trusted. <strong>Secure facilities</strong> need to stop information leaking out and to keep hostile signals out. <strong>Sensitive laboratories and clinics</strong> need low-level signals protected from the ambient noise of a modern building.</p>
<p>Tell us which of these applies and we will point you to the right starting configuration, then refine it with your standard, site and timeline.</p></div>''', tone="tint")
    return hero + cards + detail + cta_band(c)


# ---------------------------------------------------------------------------
STANDARDS_FAQ = [
    ("Which standard should I choose for my chamber?",
     "Your product dictates the standard. Consumer and IT equipment normally follow CISPR 32 and IEC 61000-4-3, vehicles and components follow CISPR 12, CISPR 25 and ISO 11452, and military equipment follows MIL-STD-461. If you are unsure, send us the product category and target markets and we will advise."),
    ("What is shielding effectiveness?",
     "Shielding effectiveness is how much a shielded enclosure reduces an electromagnetic field, measured in decibels (dB) over a range of frequencies. Every 20 dB is a ten-fold reduction in field strength, so 100 dB is a reduction of 100,000 times."),
    ("Can you confirm compliance for a specific standard?",
     "Compliance is confirmed project by project. We define the chamber class, frequency range and test set-up against the clause in your standard during design, and verify performance at handover."),
]


def standards(c):
    hero = page_hero(c, [], "Standards and shielding performance",
                     "The test standards our chambers are designed around, and how shielding performance is measured.", short="Standards")
    named = table(
        ["Standard", "What it covers", "Where it applies"],
        [
            ["CISPR 25 / EN 55025", "Limits and methods for vehicle and component emissions that could disturb on-board radio receivers", "Automotive vehicle and component chambers"],
            ["CISPR 12", "Vehicle emissions that could disturb receivers outside the vehicle", "Automotive vehicle chambers, including 10 m facilities"],
            ["ISO 11452-1 and ISO 11452-2", "Component immunity to radiated electromagnetic energy, with -2 using an absorber-lined chamber", "Automotive component and vehicle chambers"],
            ["MIL-STD-461", "Electromagnetic interference characteristics of military equipment and subsystems", "MIL-STD test chambers and 10 m military and avionic test facilities"],
            ["NATO SDIP-29/2", "Facility design criteria for processing classified information while limiting compromising emanations (TEMPEST)", "TEMPEST shielded rooms"],
        ], caption="Standards named in our project scope")
    other = table(
        ["Standard", "What it covers", "Typical chamber"],
        [
            ["CISPR 32 / EN 55032", "Emissions from multimedia equipment", "SAC-3, SAC-5, FAR-3"],
            ["CISPR 11 / EN 55011", "Industrial, scientific and medical equipment", "SAC-3, SAC-5, SAC-10 depending on product size"],
            ["IEC 61000-4-3", "Radiated radio-frequency immunity", "SAC-3, SAC-5, FAR-3"],
            ["ISO 11451-2", "Vehicle immunity to off-board radiated sources", "Vehicle chambers"],
            ["MIL-STD-188-125", "High-altitude electromagnetic pulse (HEMP) protection for facilities", "EMP / HEMP shielded rooms"],
            ["IEEE Std 299", "Method for measuring the effectiveness of shielding enclosures", "All shielded rooms"],
        ], caption="Other standards we can configure for on request")
    sec1 = section(sec_head("Standards in our scope", "Tell us the clause and the frequency range that apply to you and we will define the chamber class and test set-up to match.") + named
                   + '<div class="stack-gap"></div>' + other
                   + f'<div class="note" style="margin-top:28px">{icon("shield", "ic", 24)}<p><strong>Confirmed per project.</strong> Standards are revised regularly. We confirm the edition, chamber class and verification method in the design stage of each project.</p></div>')
    db = table(
        ["Attenuation", "Field strength reduced by", "Power reduced by"],
        [["20 dB", "10 times", "100 times"], ["40 dB", "100 times", "10,000 times"], ["60 dB", "1,000 times", "1 million times"],
         ["80 dB", "10,000 times", "100 million times"], ["100 dB", "100,000 times", "10 billion times"]],
        caption="What shielding effectiveness figures mean")
    sec2 = section(split(
        '<div class="stack">' + db + "</div>",
        '''<h2>Reading a shielding figure</h2><p>Shielding effectiveness compares the field outside an enclosure with the field inside it, in decibels (dB). The scale is logarithmic, so each extra 20 dB cuts field strength by a further factor of ten.</p>
<p>Performance changes with frequency and with the type of field. A room can perform very well against radio waves and still need extra treatment for low-frequency magnetic fields, which is why we specify the frequency range, not just a single number. Our forensic evidence box, for example, delivers over 100 dB of shielding.</p>''', flip=True), tone="tint")
    return hero + sec1 + sec2 + faq_html(STANDARDS_FAQ) + cta_band(c)


# ---------------------------------------------------------------------------
def contact(c):
    hero = page_hero(c, [], "Request a quote",
                     "Tell us what you need to test or shield. An engineer will review your brief and reply with a recommendation and next steps.", ctas=False, short="Contact")
    opts = "".join(f"<option>{esc(s[1])}</option>" for s in SOLUTIONS)
    form = f'''<form class="form" id="enquiry" novalidate aria-label="Quote request form">
<div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" type="text" autocomplete="name" required><p class="err" aria-live="polite"></p></div>
<div class="field"><label for="f-org">Company or organisation</label><input id="f-org" name="org" type="text" autocomplete="organization" required><p class="err" aria-live="polite"></p></div>
<div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required><p class="err" aria-live="polite"></p></div>
<div class="field"><label for="f-phone">Phone <small>(optional)</small></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="f-interest">Solution of interest</label><select id="f-interest" name="interest" required><option value="">Select a solution</option>{opts}<option>Not sure yet</option></select><p class="err" aria-live="polite"></p></div>
<div class="field"><label for="f-loc">Project location <small>(optional)</small></label><input id="f-loc" name="location" type="text" placeholder="City or site, country"></div>
<div class="field field--full"><label for="f-details">Project details</label><textarea id="f-details" name="details" required placeholder="Standard to test against, frequency range, equipment size and weight, available room size and ceiling height, timeline."></textarea><p class="err" aria-live="polite"></p></div>
<div class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="company_site" tabindex="-1" autocomplete="off"></label></div>
<div class="field field--full"><label class="consent" for="f-consent"><input id="f-consent" name="consent" type="checkbox" value="yes" required><span>I agree that Shield Tech may use these details to respond to my enquiry. See the <a href="{c.l("privacy")}">privacy policy</a>.</span></label><p class="err" aria-live="polite"></p></div>
<div class="field--full form__foot"><button class="btn btn--primary" type="submit"><span>Send enquiry</span></button><p class="form__status" role="status" aria-live="polite"></p></div></form>'''
    phone = ""
    if SITE["phone"]:
        phone = f'<div class="info__item"><span class="card__ic">{icon("phone")}</span><div><h3>Phone</h3><p><a href="tel:{esc(SITE["phone"].replace(" ", ""))}">{esc(SITE["phone"])}</a></p></div></div>'
    info = f'''<aside class="info" aria-label="Contact details">
<div class="info__item"><span class="card__ic">{icon("pin")}</span><div><h3>Factory and office</h3><p>{esc(SITE["legal"])}<br>{esc(SITE["street"])}<br>{esc(SITE["city"])}, {esc(SITE["country"])}<br><a href="{SITE["map_link"]}" target="_blank" rel="noopener">Open in Google Maps</a></p></div></div>
<div class="info__item"><span class="card__ic">{icon("mail")}</span><div><h3>Email</h3><p><a href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a></p></div></div>{phone}
<div class="note">{icon("doc", "ic", 24)}<div><p><strong>Include these details for a faster answer</strong></p>
{checklist(["The test standard or security requirement", "Frequency range to be covered", "Size and weight of the equipment or vehicle", "Available room footprint and ceiling height", "Site location and target dates"])}</div></div></aside>'''
    body = section(f'<div class="contact">{form}{info}</div>')
    return hero + body


# ---------------------------------------------------------------------------
def privacy(c):
    hero = page_hero(c, [], "Privacy policy", "How Shield Tech handles the information you share through this website.", ctas=False, short="Privacy policy")
    body = section(f'''<div class="legal"><p>This policy explains how {esc(SITE["legal"])} ("Shield Tech", "we") handles personal information collected through {esc(SITE["domain"])}.</p>
<h2>Information we collect</h2><p>When you send an enquiry, we collect the details you enter: your name, organisation, email address, optional phone number, project location and project details. Our web server may also keep standard technical logs such as IP address, browser type and pages requested.</p>
<h2>How we use it</h2><ul><li>To respond to your enquiry and prepare quotations.</li><li>To keep records of our business communications.</li><li>To maintain the security and performance of this website.</li></ul>
<h2>Sharing</h2><p>We do not sell your information. We may share it with delivery partners only where needed to respond to your project enquiry, and where required by law.</p>
<h2>Retention and your choices</h2><p>We keep enquiry records for as long as needed to deal with your request and meet legal obligations. To ask for access, correction or deletion of your information, email <a href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a>.</p>
<h2>Cookies</h2><p>This website does not use advertising cookies. If analytics or similar tools are added, this policy will be updated.</p>
<h2>Contact</h2><p>{esc(SITE["legal"])}, {esc(SITE["street"])}, {esc(SITE["city"])}, {esc(SITE["country"])}.</p>
<p><em>Last updated: November {SITE["year"]}.</em></p></div>''')
    return hero + body


def not_found(c):
    return section(f'''<div class="notfound"><h1>Page not found</h1><p class="lead" style="margin-inline:auto">The page you are looking for has moved or does not exist. Try one of these instead.</p>
<div class="btn-row">{btn(c.l(""), "Go to the home page", "primary", True)}{btn(c.l("solutions"), "Browse solutions", "outline")}{btn(c.l("contact"), "Contact us", "outline")}</div></div>''')
