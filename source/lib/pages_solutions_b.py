"""Solution pages, part B: shielded rooms, secure facilities and specialist shielding."""
from .core import (SITE, icon, esc, section, sec_head, btn, card, grid, checklist, table, split, faq_html, cta_band, related)
from .blocks import page_hero


# ===========================================================================
# 4. Shielded rooms and Faraday cages
# ===========================================================================
SHIELDED_FAQ = [
    ("What is a Faraday cage?",
     "A Faraday cage is an electrically conductive enclosure that blocks external electric fields and radio signals. An RF shielded room applies the same principle with a six-sided metal enclosure, so interference and ambient RF noise cannot enter or leave the room."),
    ("Can you build a shielded room in any size or shape?",
     "Yes. An RF/EMI shielded room is an electrically conductive volume, and we manufacture it in any size or shape that your site, equipment and access routes allow."),
    ("How is the shielding of a room measured?",
     "Shielding effectiveness is the reduction in field strength between the outside and the inside of the enclosure, expressed in decibels (dB) across a frequency range. Test methods such as IEEE Std 299 are commonly used. We agree the target frequency range and verification method with you at the start of the project."),
    ("What is the difference between a shielded room and an anechoic chamber?",
     "A shielded room blocks signals but its metal walls still reflect them. An anechoic chamber adds absorbers on the inside surfaces so that reflections are removed too. Use a shielded room to isolate an area, and an anechoic chamber to measure emissions, immunity or antennas."),
    ("Can you shield an existing room?",
     "In many cases yes. We survey the space, the services that cross its boundary and the required performance, then propose a modular enclosure that fits inside it."),
]


def shielded_rooms(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        "RF shielded rooms and Faraday cages in the UAE",
        "Six-sided steel enclosures, manufactured in Abu Dhabi in any size or shape, that keep radio-frequency interference and ambient RF noise out of sensitive work, or keep signals in.",
        img="shielded-door", alt="Steel door of an RF shielded room with a locking handle", short="Shielded rooms and Faraday cages")

    why = section(split(
        c.img("shielded-room-a", "Interior of a shielded room with the steel-lined doorway open"),
        '''<h2>Modern buildings are full of radio signals</h2>
<p>In almost every modern building there are high levels of wireless RF from Wi-Fi, radio, mobile phone transmitters, wireless CCTV cameras and intruder alarm systems. For research, sensitive product testing or conducted EMC testing, that background noise is a problem.</p>
<p>An RF shielded room works on the Faraday cage principle of a six-sided metal enclosure. It provides a controlled environment, free from electromagnetic interference (EMI) and ambient RF noise entering or leaving the room.</p>''', flip=True), id="why")

    where = section(sec_head("Where shielded rooms are used", "One enclosure principle, many applications. Each one has its own page with more detail.") + grid([
        card("signal", "Research and development", "A quiet radio environment for sensitive measurements and prototypes."),
        card("chamber", "Conducted EMC testing", "A shielded space for conducted emissions and immunity tests.", c.s("anechoic-emc-test-chambers")),
        card("lock", "Forensic and cyber security", "Isolate seized devices from Wi-Fi, Bluetooth and mobile networks.", c.s("forensic-cyber-security-shielding")),
        card("gov", "TEMPEST and EMP", "Secure rooms for defence, police and embassies.", c.s("tempest-emp-hemp-shielding")),
        card("pulse", "EEG and TEM rooms", "Quiet rooms for EEG recording and electron microscopes.", c.s("eeg-tem-medical-research-shielding")),
        card("server", "Data centres and containers", "Modular and mobile shielded enclosures for IT and field operations.", c.s("shielded-data-centres-containers-tents")),
    ], 3), tone="tint", id="applications")

    feats = section(split(
        c.img("shielded-room-b", "Shielded room doorway lined with steel panels", sizes="(min-width: 900px) 30vw, 92vw"),
        f'''<h2>Engineered as a complete enclosure</h2>
<p>A shielded room is only as good as its weakest point. We design the shell, door, filters, ventilation and cable entries together so that the whole enclosure meets its target.</p>
{checklist(["Steel shell built in any size or shape", "Shielded doors with robust contact surfaces", "Filtered power and signal feedthroughs", "Waveguide ventilation for airflow without leakage", "Verification of shielding performance at handover"])}
<p style="margin-top:22px">{btn(c.l("contact"), "Discuss your shielded room", "primary", True)}</p>''', flip=False), id="features")

    return hero + why + where + feats + faq_html(SHIELDED_FAQ) + related(c, ["forensic-cyber-security-shielding", "tempest-emp-hemp-shielding", "eeg-tem-medical-research-shielding"]) + cta_band(c)


# ===========================================================================
# 5. Forensic and cyber security shielding
# ===========================================================================
FORENSIC_FAQ = [
    ("Why isolate a seized phone from the network?",
     "A phone that can still reach a network can receive remote wipe commands, sync or overwrite data, and report its location. Placing it in a shielded enclosure blocks Wi-Fi, Bluetooth, cellular and GPS signals so that the evidence is preserved as it was seized."),
    ("What is the difference between a forensic shielded room and an evidence box?",
     "A forensic shielded room is a fixed Faraday-cage room in which investigators can work on devices. A forensic evidence box is a portable shielded enclosure for securing and transporting individual devices, such as mobile phones."),
    ("How much shielding does the evidence box provide?",
     "The Shield Tech forensic evidence box delivers over 100 dB of shielding."),
    ("Can you provide shielding for field investigations?",
     "Yes. Shielded containers and shielded tents allow forensic and security work to take place away from a fixed site. See our page on shielded containers and tents."),
]


def forensic(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        "Forensic Faraday rooms and evidence boxes for cyber security",
        "Isolate phones, tablets and laptops from Wi-Fi, Bluetooth, 4G and 5G so that digital evidence stays exactly as it was seized.",
        img="forensic-room", alt="Forensic facility meeting room with a shielded enclosure", short="Forensic and cyber security shielding")

    rooms = section(split(
        c.img("forensic-room", "Forensic facility interior with a long meeting table and shielded walls"),
        '''<h2>Forensic (cyber security) shielded rooms</h2>
<p>Forensic shielded rooms work on the Faraday cage principle of a six-sided metal enclosure. They provide a controlled environment, free from electromagnetic interference and ambient RF signals entering or leaving the room.</p>
<p>That makes them a suitable location for examining electronic devices without any risk of the device reaching Wi-Fi, Bluetooth, or a 4G or 5G connection.</p>'''), id="rooms")

    box = section(split(
        c.img("forensic-corridor", "Shielded forensic room entrance with a black steel door"),
        f'''<h2>Forensic evidence (cyber security) box</h2>
<p>The forensic evidence box is a portable shielded enclosure designed with law enforcement in mind, delivering over 100 dB of shielding. It is engineered so that securing and protecting a mobile phone is simple and repeatable every time. The box can only be opened and closed one way, and closes securely to make sure the shield is complete.</p>
<p>Any device inside is protected from file transfer, remote wipe commands, Find My and GPS tracking, which completely isolates it and preserves the evidence.</p>''', flip=True), tone="tint", id="evidence-box")

    blocked = section(sec_head("What isolation prevents", "Every wireless path to the device is closed, including device-to-device links.") + grid([
        card("lock", "Remote wipe and file transfer", "Commands that could erase or alter data cannot reach the device."),
        card("pin", "Location tracking", "Find My and GPS tracking are blocked, so the device cannot report where it is."),
        card("link", "Device-to-device connections", "Bluetooth, AirDrop-style file transfer and Wi-Fi links to other devices are stopped."),
        card("signal", "Cellular and satellite", "Cellular / GPRS and low Earth orbit satellite connections cannot be established."),
    ], 4), tone="dark")

    users = section(sec_head("Who uses forensic shielding") + checklist([
        "Police and law enforcement agencies",
        "Digital forensics laboratories and investigators",
        "Government and security departments",
        "Corporate security and incident response teams",
    ], "checks--2") + f'<div class="note" style="margin-top:28px">{icon("container", "ic", 24)}<p><strong>Working away from a fixed site?</strong> See our <a href="{c.s("shielded-data-centres-containers-tents", "#containers")}">shielded containers</a> and <a href="{c.s("shielded-data-centres-containers-tents", "#tents")}">shielded tents</a> for mobile forensic spaces.</p></div>')

    return hero + rooms + box + blocked + users + faq_html(FORENSIC_FAQ) + related(c, ["shielded-rooms-faraday-cages", "tempest-emp-hemp-shielding", "shielded-data-centres-containers-tents"]) + cta_band(c)


# ===========================================================================
# 6. TEMPEST and EMP / HEMP
# ===========================================================================
TEMPEST_FAQ = [
    ("What is TEMPEST?",
     "TEMPEST refers to the practice of preventing electronic equipment from leaking information through unintended radio, electrical or magnetic emissions. A TEMPEST shielded room helps contain those emanations so that classified or sensitive information cannot be picked up from outside."),
    ("Is a Faraday cage enough for TEMPEST?",
     "A shielded room is a core part of a TEMPEST solution, but it is not the whole of it. Power, signal lines, ventilation and the equipment inside also matter. Our shielded rooms are designed as part of a complete TEMPEST solution to the shielding effectiveness and design requirements you specify, including NATO SDIP-29/2."),
    ("What does EMP, NEMP and HEMP mean?",
     "EMP is an electromagnetic pulse, a short burst of intense electromagnetic energy. NEMP is a nuclear electromagnetic pulse and HEMP is a high-altitude electromagnetic pulse. Our EMP shielded rooms are adapted to protect equipment from all of these."),
    ("Can one room provide both TEMPEST and EMP protection?",
     "Often yes. Because both are based on a shielded conductive volume, a room can be designed to meet both sets of requirements, with the design driven by whichever is more demanding. Share your requirements with us and we will confirm what is practical."),
]


def tempest(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        "TEMPEST and EMP / HEMP shielded rooms",
        "Secure rooms that stop sensitive information from escaping, and protect critical electronics from electromagnetic pulses, for defence, police, government and embassy facilities.",
        img="shielded-room-a", alt="Interior of a shielded room with the steel-lined doorway open", short="TEMPEST and EMP / HEMP shielding")

    temp = section(split(
        c.img("shielded-door", "Steel door and frame of a shielded room"),
        '''<h2>TEMPEST shielded rooms</h2>
<p>TEMPEST shielded enclosures and rooms are designed to meet the shielding effectiveness and design requirements of TEMPEST and NATO SDIP-29/2. The room works on the Faraday cage principle of a six-sided metal enclosure, providing a controlled environment, free from electromagnetic interference (EMI) and ambient RF signals entering or leaving.</p>
<p>The shielded room is a suitable location for police, defence and military organisations or embassies to protect sensitive information, as part of a complete TEMPEST solution.</p>''', flip=True), id="tempest")

    emp = section(split(
        c.img("shielded-room-b", "Shielded room doorway lined with steel panels", sizes="(min-width: 900px) 30vw, 92vw"),
        '''<h2>EMP, NEMP and HEMP shielded rooms</h2>
<p>An RF/EMI shielded room (Faraday cage) is an electrically conductive volume that can be manufactured and designed in any size or shape. Our EMP rooms adapt this principle to electromagnetic pulse shielding, including NEMP and HEMP.</p>
<p>EMP shielding is required to protect command and control centres and communication facilities, and wherever electronic equipment must be safe from damage by an EMP, NEMP or HEMP event.</p>'''), tone="tint", id="emp")

    cmp_tbl = table(["", "TEMPEST room", "EMP / HEMP room"], [
        ["Purpose", "Stops information leaking out through emissions", "Stops a pulse from damaging equipment inside"],
        ["Direction of protection", "Mostly inside to outside", "Mostly outside to inside"],
        ["Typical users", "Police, defence and military bodies, embassies", "Command and control centres, communication facilities, critical infrastructure"],
        ["Reference", "TEMPEST and NATO SDIP-29/2", "Project-specific EMP, NEMP and HEMP requirements"],
    ], caption="TEMPEST and EMP rooms compared")
    compare = section(sec_head("Two threats, one shielding principle") + cmp_tbl + f'<div class="note" style="margin-top:28px">{icon("shield", "ic", 24)}<p><strong>Requirements first.</strong> Government and defence projects are specified in detail. Share the standard, security zone and classification level and we will confirm what we can design, manufacture and verify.</p></div>')

    return hero + temp + emp + compare + faq_html(TEMPEST_FAQ) + related(c, ["shielded-rooms-faraday-cages", "forensic-cyber-security-shielding", "automotive-military-emc-chambers"]) + cta_band(c)


# ===========================================================================
# 7. EEG, TEM, medical and research shielding
# ===========================================================================
EEG_FAQ = [
    ("Why does an EEG need a shielded room?",
     "An electroencephalogram records very small electrical signals from the brain. Universities and hospitals are full of high-current cables, Wi-Fi, wireless signals and other electrical equipment, which can swamp those signals with noise. A shielded room keeps that background out and gives a stable, repeatable recording environment."),
    ("What frequencies do EEG shielded rooms protect against?",
     "EEG rooms are designed for optimised performance at VLF and ELF frequencies, as well as protecting against higher-frequency interference such as Wi-Fi. This helps protect the highly sensitive test equipment inside from external interference."),
    ("What does a TEM shielded room do?",
     "A TEM shielded room is designed to shield sensitive transmission electron microscopes from 50 Hz AC and quasi-DC interference. It uses passive shielding together with an active cancellation system to create a magnetically shielded room in which the microscope can work to its full potential."),
    ("Can you size the room around my equipment?",
     "Yes. Rooms are sized for the instrument, operator desk and access route, and for the ceiling height and services available in your building."),
]


def eeg_tem(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        "EEG and TEM shielded rooms for hospitals and universities",
        "Quiet electromagnetic environments for neurological recordings and electron microscopy, built to protect low-level signals from the noise of a modern building.",
        img="eeg-room", alt="Cutaway of an EEG shielded room with a desk, chair and shielded door", short="EEG, TEM and research shielding")

    eeg = section(split(
        c.img("eeg-room", "Cutaway of an EEG shielded room with a desk, chair and shielded door"),
        '''<h2>EEG laboratories</h2>
<p>Universities and hospitals have an increasingly polluted electromagnetic environment, with high-current cables, Wi-Fi, wireless signals and other electrical equipment. To run electroencephalogram (EEG) tests without interference and ambient noise affecting the sensitive measurements, shielding is required.</p>
<p>EEG shielded rooms are designed specifically for medical and educational environments, with optimised performance at VLF and ELF frequencies. They protect the highly sensitive test equipment inside the room from external interference and provide a stable, repeatable testing environment.</p>''', flip=True), id="eeg")

    tem = section(split(
        c.img("tem-room", "Cutaway of a TEM shielded room housing an electron microscope and a desk"),
        '''<h2>TEM shielded rooms</h2>
<p>A TEM shielded room is a shielded room or laboratory designed specifically to protect sensitive transmission electron microscopes from 50 Hz AC and quasi-DC interference.</p>
<p>Through passive shielding and an active cancellation system, a magnetically shielded room is created so that the microscope can work to its greatest potential.</p>'''), tone="tint", id="tem")

    cmp_tbl = table(["", "EEG room", "TEM room"], [
        ["Protects", "EEG recording equipment and subjects", "Transmission electron microscope"],
        ["Main interference", "Mains fields, Wi-Fi, wireless signals, nearby electrical equipment", "50 Hz AC fields and quasi-DC magnetic fields"],
        ["Approach", "Shielded enclosure optimised for VLF and ELF", "Passive shielding plus an active cancellation system"],
        ["Typical site", "Hospitals, universities, neuroscience laboratories", "Universities, research institutes, materials laboratories"],
    ], caption="EEG and TEM rooms compared")
    cmp_sec = section(sec_head("Choosing between EEG and TEM rooms") + cmp_tbl)

    return hero + eeg + tem + cmp_sec + faq_html(EEG_FAQ) + related(c, ["shielded-rooms-faraday-cages", "magnetic-field-shielding", "shielded-data-centres-containers-tents"]) + cta_band(c)


# ===========================================================================
# 8. Magnetic field shielding
# ===========================================================================
MAG_FAQ = [
    ("Why do power cables, transformers and bus-bars produce magnetic fields?",
     "Any conductor carrying current creates a magnetic field. The greater the current, the stronger the field. With higher power demand inside modern buildings, these fields are getting larger."),
    ("Why not use ordinary steel or aluminium sheet?",
     "Radio-frequency shielding relies on conductivity. Low-frequency magnetic fields at 50 Hz need a material with very high magnetic permeability, which draws the field into the shield instead of letting it pass through the room. That is why a purpose-designed high-permeability shield is used for 50 Hz magnetic field problems."),
    ("What field level should I design for?",
     "It depends on who or what you are protecting and on local regulation. Reference levels commonly used are 100 µT for public exposure, 3.75 µT for equipment sensitive to EMC effects, and 0.4 µT for permanent occupancy. We confirm the target for your site at the brief stage."),
    ("Can you shield a substation that sits close to housing or offices?",
     "That is one of the main uses of transformer and switch shielding. We assess the equipment, distances and target field level and propose a modular shielding system for the room or building."),
]


def magnetic(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        "Magnetic field shielding for trunking, transformers and switchgear",
        "Shielding for the strong 50 Hz magnetic fields produced by high-voltage cables, bus-bars, transformers and switchgear, so modern power infrastructure can sit close to people and sensitive equipment.",
        img="trunking", alt="Shielded cable trunking with bolted joints", short="Magnetic field shielding")

    why = section(sec_head("Power infrastructure creates magnetic fields",
                           "High-voltage power cables, transformers and bus-bars all generate electromagnetic fields (EMF). The more current they carry, the more field they emit, and demand for power inside buildings keeps growing.")
                  + table(["Reference level", "Typical use as a design target"], [
                      ["100 µT", "Public exposure, for example protecting people with heart pacemakers"],
                      ["3.75 µT", "Limit for EMC-sensitive equipment"],
                      ["0.4 µT", "Permanent occupancy and long-term exposure"],
                  ], caption="Reference levels for 50 Hz magnetic fields")
                  + f'<div class="note" style="margin-top:24px">{icon("ruler", "ic", 24)}<p><strong>Targets depend on the project.</strong> The applicable limit depends on who or what is being protected and on local regulation. We confirm the design target with you at the start of the project.</p></div>', id="why")

    trunk = section(split(
        c.img("trunking", "Shielded cable trunking with bolted joints", sizes="(min-width: 900px) 30vw, 92vw"),
        '''<h2>Shielded trunking</h2>
<p>Cable and bus-bar routes pass through the same corridors and risers that people and equipment use. Shielded trunking contains the magnetic field right at the source, along the whole length of the route.</p>
<p>It is a practical way to reduce exposure in offices, hospitals, data halls and residential buildings, where moving the cables is not an option.</p>''', flip=True), tone="tint", id="trunking")

    trans = section(split(
        '<div class="note note--plain">' + icon("magnet", "ic", 36) + '<p><strong>How the shield works.</strong> A shield made of high-purity iron has very high magnetic permeability. The field flows more easily inside the shield than through the surrounding air, which diverts, or shunts, it away from the protected space.</p></div>',
        '''<h2>Transformer and switchgear shielding (50 Hz building shielding)</h2>
<p>Our modular shielding system uses high-purity iron with very high magnetic permeability, from 50 Hz up to microwave frequencies. Because the field is drawn into the shield rather than into free air, a protected room can be created next to the equipment.</p>
<p>Smaller building footprints and high land prices mean electrical switchgear, MV/LV transformer substations and plant rooms are increasingly sited close to homes and offices. Shielding allows them to be installed there while keeping fields at acceptable levels.</p>'''), id="transformer")

    return hero + why + trunk + trans + faq_html(MAG_FAQ) + related(c, ["eeg-tem-medical-research-shielding", "shielded-data-centres-containers-tents", "ehv-laboratories"]) + cta_band(c)


# ===========================================================================
# 9. Shielded data centres, containers and tents
# ===========================================================================
MOBILE_FAQ = [
    ("Do shielded containers look different from ordinary shipping containers?",
     "No. Externally they have the appearance of a standard shipping container. Inside, they can be fitted out with a high-quality, office-style interior."),
    ("What sizes are available?",
     "Shielded containers are available in ISO 20 ft and 40 ft standard and high-cube sizes, as well as bespoke non-ISO sizes. Each one is individually configurable to your exact requirements."),
    ("Which signals does a shielded container block?",
     "A shielded container is isolated from external Wi-Fi, radio, television, GPS, LoRa, Bluetooth, GSM 2G and 3G, 4G and 5G signals. It is also 5G ready."),
    ("What are shielded tents used for?",
     "Shielded tents are specialised enclosures designed to block or reduce electromagnetic interference (EMI) and radio frequency interference (RFI). They protect sensitive electronic equipment, support secure communications and allow EMI/RFI testing outside a fixed room."),
    ("What does a shielded data centre protect against?",
     "The high-frequency shell protects IT rooms and IT equipment against electromagnetic interference from outside."),
]


def mobile(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        "Shielded data centres, containers and tents",
        "Modular and mobile shielded enclosures that protect IT infrastructure from electromagnetic interference, or provide secure, signal-isolated workspaces wherever you need them.",
        img="container-inside", alt="Interior of a shielded container fitted out as an office", short="Data centres, containers and tents")

    dc = section(split(
        c.img("datacentre-black", "Render of a black shielded data centre module with a double door", sizes="(min-width: 900px) 40vw, 92vw"),
        f'''<h2>Shielded data centres</h2>
<p>Protect your information technology with our shielding technology, enclosed in a shielded data centre. The high-frequency shell protects IT rooms and equipment against electromagnetic interference from outside.</p>
<p>The enclosure is modular, so racks, cooling and access doors can be arranged around your equipment, and the shield travels with the layout.</p>''', flip=True), id="datacentres")

    ct = section(split(
        c.img("container-inside", "Interior of a shielded container fitted out as an office with desks and a display wall"),
        f'''<h2>Shielded containers</h2>
<p>A shielded container is isolated from external Wi-Fi, radio, television, GPS, LoRa, Bluetooth, GSM 2G and 3G, 4G and 5G signals.</p>
{checklist(["Available in ISO 20 ft and 40 ft standard and high-cube sizes, plus bespoke (non-ISO) sizes", "High-quality, office-style interiors", "External appearance of a standard shipping container", "Individually configurable to exact requirements", "5G ready"])}'''), tone="tint", id="containers")

    tent = section(split(
        c.img("tent", "Shielded tent made from black conductive fabric on an aluminium frame", sizes="(min-width: 900px) 30vw, 92vw"),
        '''<h2>Shielded tents</h2>
<p>Shielded tents are specialised enclosures designed to block or reduce electromagnetic interference (EMI) and radio frequency interference (RFI). They are commonly used to protect sensitive electronic equipment, ensure secure communications and conduct EMI/RFI testing.</p>
<p>They are made with conductive materials such as silver, copper or nickel mesh and provide a controlled environment free from external electromagnetic signals.</p>''', flip=True), id="tents")

    cmp_tbl = table(["", "Shielded data centre", "Shielded container", "Shielded tent"], [
        ["Best for", "Protecting IT rooms and equipment", "Secure, relocatable workspaces and offices", "Fast, temporary shielding"],
        ["Construction", "Modular shielded shell", "Steel container shell", "Conductive fabric on a frame"],
        ["Mobility", "Planned installation", "Transportable like a shipping container", "Portable"],
        ["Typical users", "IT operators, data-centre developers", "Police, defence, forensic teams", "Test teams, field operations"],
    ], caption="Choosing a modular or mobile enclosure")
    cmp_sec = section(sec_head("Compare the options") + cmp_tbl, id="compare")

    return hero + dc + ct + tent + cmp_sec + faq_html(MOBILE_FAQ) + related(c, ["shielded-rooms-faraday-cages", "forensic-cyber-security-shielding", "magnetic-field-shielding"]) + cta_band(c)


# ===========================================================================
# 10. EHV laboratories
# ===========================================================================
EHV_FAQ = [
    ("What is an EHV laboratory?",
     "An extra-high-voltage (EHV) laboratory is a specialised facility for testing high-voltage equipment. It is focused on electrical systems, and may also include lighting chambers for specific tests."),
    ("What voltages do EHV laboratories work at?",
     "EHV laboratories test electrical systems at voltages above 100 kV, including insulation and breakdown voltage assessments."),
    ("What is a lighting chamber?",
     "A lighting chamber simulates various lighting conditions so that fixtures, lamps and electrical components can be tested."),
    ("How is personnel safety handled?",
     "Because of the extreme voltages involved, strict safety measures and shielding are essential to protect personnel. We discuss the safety concept and shielding as part of the project brief."),
]


def ehv(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        "EHV laboratories and lighting test chambers",
        "Specialised facilities for testing extra-high-voltage equipment, with the shielding and safety measures that make testing at these voltages practical and safe.",
        short="EHV laboratories")

    overview = section(f'''<div class="prose"><h2>Facilities for high-voltage equipment</h2>
<p>EHV laboratories, or extra-high-voltage laboratories, are specialised facilities for testing high-voltage equipment. While they are focused on electrical systems, they may also include lighting chambers for specific testing.</p></div><div style="margin-top:36px">''' + grid([
        card("tower", "High-voltage testing", "Electrical systems are tested at voltages above 100 kV, including insulation and breakdown voltage assessments."),
        card("bolt", "Lighting chambers", "Chambers simulate various lighting conditions to test fixtures, lamps and electrical components."),
        card("shield", "Safety and shielding", "At extreme voltages, strict safety measures and shielding are essential to protect personnel."),
    ], 3) + "</div>", id="overview")

    tests = section(sec_head("Types of tests conducted") + table(["Test", "What it checks"], [
        ["Dielectric strength testing", "Insulation performance"],
        ["Temperature rise testing", "How much heat builds up under load"],
        ["Operational testing", "How components behave under high voltage"],
    ]), tone="tint", id="tests")

    apps = section(split(
        '<div class="note note--plain">' + icon("pulse", "ic", 36) + '<p><strong>Research and development.</strong> These laboratories advance innovation in lighting and high-voltage technology, help ensure compliance with standards and promote safer electrical systems.</p></div>',
        f'''<h2>Applications</h2>
<p>EHV laboratories support the development of high-voltage products and the systems that use them.</p>
{checklist(["High-voltage switches and breakers", "Insulation materials and cables", "Lighting systems for high-voltage environments"])}
<p style="margin-top:22px">{btn(c.l("contact"), "Discuss an EHV laboratory", "primary", True)}</p>'''), id="applications")

    return hero + overview + tests + apps + faq_html(EHV_FAQ) + related(c, ["magnetic-field-shielding", "shielded-rooms-faraday-cages", "tempest-emp-hemp-shielding"]) + cta_band(c)
