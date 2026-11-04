"""Solution pages, part A: the three test-chamber pages."""
from .core import (SITE, icon, esc, section, sec_head, btn, card, grid, checklist, table, split, faq_html, cta_band, related)
from .blocks import page_hero, model_card


# ===========================================================================
# 1. Anechoic EMC test chambers
# ===========================================================================
ANECHOIC_FAQ = [
    ("What is the difference between a semi-anechoic chamber (SAC) and a fully anechoic room (FAR)?",
     "A semi-anechoic chamber has absorbers on the walls and ceiling and a reflective metal floor, which many emissions standards call for. A fully anechoic room also has absorbers on the floor, so there are no ground reflections and the antenna can stay at one fixed height. That shortens radiated-emissions testing and allows a lower ceiling, while a SAC is the right choice when your standard specifies a ground plane."),
    ("Which test distance do I need: 3 m, 5 m or 10 m?",
     "The distance is set by your standard and by the size of the product. A 3 m chamber suits most commercial and IT equipment. A 5 m chamber takes larger equipment and bigger turntables. A 10 m chamber is used for vehicles, military equipment and large products that must be measured in their far field. Send us the product dimensions and the standard and we will recommend a size."),
    ("What is a pre-compliant EMC chamber?",
     "A pre-compliant chamber is a compact, space-saving room that keeps the 3 m antenna distance while giving up some of the volume of a full compliance chamber. It is used for research and development and for checking a design before final compliance testing, so fewer products fail at the test house."),
    ("Can a chamber be installed inside an existing building?",
     "Yes. Our steel structures and shielding modules are designed around the hall, ceiling height and floor loading available on your site. Tell us the room dimensions and access routes during the quote stage and we will propose a layout that fits."),
    ("Where are Shield Tech chambers manufactured?",
     "Chambers are fabricated at our facility in KEZAD Logistics Park, ICAD 3, Abu Dhabi, United Arab Emirates, and installed on site with our delivery partner."),
]


def anechoic(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        'Anechoic EMC test chambers: <span class="nb">SAC-3,</span> <span class="nb">SAC-5,</span> <span class="nb">SAC-10</span> and <span class="nb">FAR-3</span>',
        "Shield Tech designs and manufactures custom semi-anechoic and fully anechoic EMC chambers in Abu Dhabi, giving test engineers a zero-interference space for accurate, repeatable emissions and immunity measurements.",
        img="far3-interior", alt="Interior of a fully anechoic EMC chamber with white absorbers and a turntable", short="Anechoic EMC chambers")

    overview = section(split(
        c.img("sac5-side", "Steel structure of a SAC-5 semi-anechoic EMC test chamber installed in a hall"),
        f'''<h2>A controlled space for results you can trust</h2>
<p>An EMC chamber is a shielded room lined with radio-absorbing material. The steel shell keeps outside signals away from the test and stops the product's own emissions from leaking out. The absorbers stop the walls from bouncing energy back at the antenna. Together they create a stable, comparable environment for emissions and immunity testing.</p>
<p>Whether you are testing military-grade electronics, consumer devices, automotive components or aerospace systems, a Shield Tech chamber is built around your standard, your product size and your building. Fabrication is carried out in the UAE, so design, production and site support run through one team.</p>
{checklist(["Compliant emissions and immunity testing in one facility", "3 m, 5 m and 10 m test distances", "Semi-anechoic, fully anechoic and pre-compliant options", "Custom layouts for your hall, standard and product"])}'''))

    models = grid([
        model_card("SAC-10", "10 m semi-anechoic chamber",
                   "Spacious enough for complete vehicles and voluminous products. Heavy-duty flooring and large turntables suit ruggedised military component and vehicle testing, and the longer distance lets large products be measured in their far field. Commercial, automotive, military and avionic test procedures can all be performed here.",
                   "Vehicles, military and avionic equipment, very large commercial products",
                   c.img("sac10-plan", "Plan view of a SAC-10 chamber structure", sizes="(min-width: 1020px) 30vw, 92vw"), "sac-10"),
        model_card("SAC-5", "5 m semi-anechoic chamber",
                   "The advantage of size. Designed for commercial EMC testing of larger equipment under test, it combines compliant emissions and immunity testing in one facility. The longer distance takes larger turntables and bigger products, and one chamber can serve a variety of standards.",
                   "Larger commercial products, labs that need one room for several standards",
                   c.img("sac5-side", "Side view of a SAC-5 chamber with its steel frame", sizes="(min-width: 1020px) 30vw, 92vw"), "sac-5"),
        model_card("SAC-3", "3 m semi-anechoic chamber",
                   "Designed for accuracy. The SAC-3 is purpose designed for commercial EMC testing and brings compliant emissions and immunity testing into a single facility, so your products meet national and international EMC standards.",
                   "Commercial and IT equipment, test houses, in-house manufacturer labs",
                   c.img("sac3-exterior", "Render of a SAC-3 chamber installed in a large hall", sizes="(min-width: 1020px) 30vw, 92vw"), "sac-3"),
        model_card("FAR-3", "3 m fully anechoic chamber",
                   "A shielded enclosure with the latest-generation absorber on all walls, ceiling and floor. With no ground reflections there is no need for a 1 m to 4 m antenna sweep: a fixed antenna height is aimed at the centre of the test volume. Radiated-emissions runs are faster, throughput is higher and the lower ceiling reduces capital cost and building space.",
                   "High-throughput product testing, sites with limited ceiling height",
                   c.img("far3-interior", "Fully anechoic FAR-3 chamber with white absorbers", sizes="(min-width: 1020px) 30vw, 92vw"), "far-3"),
        model_card("Pre-compliant", "Compact 3 m semi-anechoic chamber",
                   "When space matters. A compact, cost-effective chamber that delivers dependable, repeatable EMC measurements on your own premises. It keeps the 3 m measuring distance between antenna and equipment, and makes the most of the available space to give pre-compliant emissions and compliant immunity testing.",
                   "Research and development, design iteration, fast-tracking products toward final compliance",
                   c.img("emc-control-cabinets", "Render of EMC test equipment cabinets with digital displays in a control room", sizes="(min-width: 1020px) 45vw, 92vw"), "pre-compliant"),
    ], 3, "grid--five")
    models_sec = section(sec_head("Choose the right chamber", "Five configurations cover most commercial, automotive, military and R&amp;D requirements. Each one is adapted to your standard and site.") + models, tone="tint", id="models")

    cmp_tbl = table(
        ["", "Semi-anechoic chamber (SAC)", "Fully anechoic room (FAR)"],
        [
            ["Absorber coverage", "Walls and ceiling, with a reflective metal ground plane", "Walls, ceiling and floor"],
            ["Antenna height", "Scans from 1 m to 4 m to find the strongest emission", "Fixed height, aimed at the centre of the test volume"],
            ["Radiated-emissions test time", "Longer, because of the height scan", "Shorter, so more products can be tested per day"],
            ["Ceiling height and footprint", "Taller room for the antenna scan", "Lower ceiling, smaller building volume and lower capital cost"],
            ["Choose it when", "Your standard calls for a ground plane, or the product is very large or heavy", "You want fast, compact testing and your standard allows a fully anechoic room"],
        ], caption="SAC and FAR compared")
    compare = section(sec_head("Semi-anechoic or fully anechoic?", "The key difference is the floor. Lining it with absorber removes ground reflections and changes how a test is run.") + cmp_tbl, id="sac-vs-far")

    parts = grid([
        card("shield", "Shielded steel enclosure", "A closed, electrically conductive steel shell that works as a Faraday cage around the test volume."),
        card("layers", "Absorbers", "Pyramidal foam, ferrite tiles or a hybrid of both, selected for the frequency range you need to cover."),
        card("lock", "Shielded doors", "Single and double-leaf doors with robust contact surfaces, sized for people, equipment and vehicles."),
        card("bolt", "Filtered feedthroughs", "Filtered power and signal lines, fibre-optic links and connector panels keep interference out of the room."),
        card("wave", "Ventilation", "Waveguide honeycomb vents let air in and out without opening a path for radio signals."),
        card("signal", "Monitoring and lighting", "Emission-free lighting, cameras and intercom let operators watch and talk to the test area from the control room."),
        card("ruler", "Positioning", "Turntables, test benches and antenna masts with controllers for repeatable positioning."),
        card("clock", "Verification", "Shielding and chamber performance are verified at handover and documented."),
    ], 4)
    inside = section(sec_head("What is inside a Shield Tech chamber", "Chamber performance depends on every component, from the steel shell to the door seals. Each part is specified together as one system.") + parts, tone="dark", id="components")

    choose = section(sec_head("Which chamber suits your product?") + table(
        ["If your product is...", "Start with", "Why"],
        [
            ["A vehicle, bus or very large military or avionic item", '<a href="#sac-10">SAC-10</a>', "Far-field measurement and floor strength for heavy equipment"],
            ["Large commercial equipment or several product families", '<a href="#sac-5">SAC-5</a>', "Bigger turntable and test volume, flexible for several standards"],
            ["Typical commercial, IT or consumer electronics", '<a href="#sac-3">SAC-3</a>', "Compliant emissions and immunity in a compact footprint"],
            ["Tabletop equipment tested at high volume", '<a href="#far-3">FAR-3</a>', "Fixed antenna height means shorter test runs"],
            ["Under development, needing quick in-house checks", '<a href="#pre-compliant">Pre-compliant chamber</a>', "Low-cost, space-saving, dependable pre-scans"],
        ]), tone="tint")

    return hero + overview + models_sec + compare + inside + choose + faq_html(ANECHOIC_FAQ) + related(c, ["automotive-military-emc-chambers", "antenna-measurement-chambers", "shielded-rooms-faraday-cages"]) + cta_band(c)


# ===========================================================================
# 2. Automotive and military chambers
# ===========================================================================
AUTO_FAQ = [
    ("What is the difference between CISPR 12 and CISPR 25?",
     "CISPR 12 covers emissions from vehicles that could disturb radio receivers outside the vehicle, measured at a distance such as 10 m. CISPR 25 covers emissions that could disturb receivers on board the vehicle, for both vehicles and components. Our vehicle chambers are designed so that both can be run in one facility where the layout allows."),
    ("Can a complete vehicle be tested in your chambers?",
     "Yes. Vehicle chambers and our SAC-10 are built large enough to take complete vehicles, with heavy-duty flooring and large turntables. Tell us the largest vehicle you need to test and we will size the room, doors and floor loading around it."),
    ("What is MIL-STD-461?",
     "MIL-STD-461 is the US military standard that sets the electromagnetic interference emission and susceptibility requirements for equipment and subsystems. A MIL-STD-461 chamber is a shielded, absorber-lined room used to qualify equipment against those requirements."),
    ("Why use a bespoke absorber for MIL-STD-461?",
     "A compact pyramidal absorber designed specifically for MIL-STD-461 takes up less depth than a general-purpose lining. That increases the usable space inside the chamber and helps reduce the overall cost of the facility."),
    ("Can the same chamber be used for emissions and immunity?",
     "Our automotive chambers are designed to run both. They are compliant for emissions testing to EN 55025 / CISPR 25 and for immunity testing to ISO 11452-2."),
]


def automotive(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        'Automotive and military EMC test chambers: <span class="nb">CISPR 25</span> and <span class="nb">MIL-STD-461</span>',
        "Vehicle, component and military test chambers for CISPR 25, ISO 11452 and MIL-STD-461 requirements, manufactured in Abu Dhabi on a self-standing steel structure with modular steel shielding.",
        img="auto-chamber", alt="Automotive EMC chamber structure with a coach parked beside it", short="Automotive and military chambers")

    overview = section(split(
        c.img("mil-interior", "Interior wall of a MIL-STD chamber with a personnel door and steel frame"),
        '''<h2>Qualification facilities for vehicles and defence equipment</h2>
<p>Vehicles and military systems must prove they neither disturb nor are disturbed by their electromagnetic surroundings. That means large, rugged, accurately lined chambers that can carry heavy loads and still deliver repeatable results.</p>
<p>Shield Tech builds these facilities on a self-standing steel structure with a modular steel shield. The result is a robust, scalable room that can be sized for a component bench or for a complete vehicle, and that can be installed in an existing hall.</p>'''))

    models = grid([
        model_card("CISPR 25", "Automotive vehicle test chamber",
                   "A CISPR 12 / CISPR 25 automotive test facility, including 10 m configurations, designed for compliant EN 55025 / CISPR 25 testing. The chamber is also compliant for immunity tests to ISO 11452-2 and is built from a self-standing steel structure and modular steel shield.",
                   "Vehicle emissions and immunity, OEM and supplier validation", "", "vehicle"),
        model_card("Component", "Automotive component test chamber",
                   "A CISPR 25 facility designed for component testing to EN 55025 / CISPR 25 and ISO 11452-1, and compliant for component immunity tests to ISO 11452-2.",
                   "Tier-1 and tier-2 suppliers, electronic modules, sensors, infotainment", "", "component"),
        model_card("MIL-STD-461", "Military test chamber",
                   "A MIL-STD-461 facility designed for the varied, heavy-duty testing the military requires. Built on a self-standing steel structure and modular steel shield, with a compact, cost-effective pyramidal absorber made specifically for this standard to increase internal space and reduce overall cost.",
                   "Military components, vehicles and large equipment, avionics", "", "mil-std"),
    ], 3)
    models_sec = section(sec_head("Three chamber families", "Choose a configuration, then we adapt it to your standard, product envelope and building.") + models, tone="tint", id="models")

    std = table(["Standard", "What it governs", "Applies to"], [
        ["EN 55025 / CISPR 25", "Emissions that could disturb receivers on board the vehicle", "Vehicle and component chambers"],
        ["CISPR 12", "Emissions that could disturb receivers outside the vehicle", "Vehicle chambers, including 10 m facilities"],
        ["ISO 11452-1 and ISO 11452-2", "Immunity of components to radiated electromagnetic energy, using an absorber-lined chamber", "Component and vehicle chambers"],
        ["MIL-STD-461", "Electromagnetic interference characteristics of military equipment and subsystems", "MIL-STD test chambers and 10 m facilities"],
    ], caption="Standards these chambers are designed around")
    std_sec = section(sec_head("Standards and compliance", f'Edition, chamber class and verification method are confirmed project by project. See our <a href="{c.l("standards")}">standards overview</a> for more.') + std, id="standards")

    feat = section(sec_head("Built for heavy-duty testing") + grid([
        card("car", "Large-product capability", "Spacious rooms, heavy-duty flooring and large turntables carry vehicles, buses and heavy military equipment."),
        card("layers", "Self-standing steel structure", "The frame carries the shield and absorbers independently of the building, which simplifies installation in an existing hall."),
        card("shield", "Modular steel shield", "Shielding is assembled from engineered modules for consistent performance and a practical installation sequence."),
        card("ruler", "Efficient use of space", "Bespoke absorbers for MIL-STD-461 free up internal volume and keep the cost of the facility down."),
    ], 4), tone="dark")

    users = section(sec_head("Who uses these chambers") + checklist([
        "Automotive manufacturers and their tier-1 and tier-2 suppliers",
        "Independent test laboratories offering vehicle and component services",
        "Defence contractors and military test programmes",
        "Avionics and aerospace developers needing large far-field test rooms",
    ], "checks--2"), tone="tint")

    return hero + overview + models_sec + std_sec + feat + users + faq_html(AUTO_FAQ) + related(c, ["anechoic-emc-test-chambers", "antenna-measurement-chambers", "tempest-emp-hemp-shielding"]) + cta_band(c)


# ===========================================================================
# 3. Antenna measurement chambers
# ===========================================================================
ANTENNA_FAQ = [
    ("What is an antenna measurement chamber?",
     "It is a shielded room lined with radio-absorbing material in which an antenna, or a device containing one, is measured without outside interference or reflections. Engineers use it to record radiation patterns, gain and polarisation, and to characterise the performance of wireless products."),
    ("How is an antenna chamber different from an EMC chamber?",
     "An EMC chamber measures unintentional emissions from a product and its immunity to interference, usually against a published standard. An antenna chamber measures how well an intentional radiator performs. The shielding is similar, but the layout, absorber choice and positioning equipment are designed around the antennas under test."),
    ("Can you build chambers for Wi-Fi and 5G devices?",
     "Yes. Wi-Fi and wireless test chambers are part of our core experience, together with antenna measurement rooms for 5G, telecommunications and radar technologies."),
    ("How do you choose the frequency range?",
     "The absorber lining, the room size and the positioning system are chosen from the frequency band of the antennas you need to measure. We confirm that band with you at the start of the design."),
]


def antenna(c):
    hero = page_hero(
        c, [("Solutions", "solutions")],
        "Antenna measurement chambers for 5G, radar and wireless testing",
        "Absorber-lined antenna test rooms designed around the antennas under test, giving you a reliable, repeatable environment for pattern measurement and antenna characterisation.",
        img="antenna-room", alt="Antenna measurement chamber lined with pyramidal absorbers around a positioner", short="Antenna measurement chambers")

    overview = section(split(
        c.img("antenna-cube", "Exterior of a compact shielded antenna chamber with a steel door", sizes="(min-width: 900px) 40vw, 92vw"),
        '''<h2>Test your latest technologies with confidence</h2>
<p>Antenna measurement rooms need to deliver exacting performance. Whether you are developing 5G, telecommunications, radar or other wireless technology, each Shield Tech chamber is designed to meet the needs of the antennas you are testing.</p>
<p>Chambers are adaptable and configurable for military, marine, aerospace and commercial applications. Each facility gives the user a reliable, repeatable test environment for antenna testing and for characterising antenna specifications.</p>''', flip=True))

    apps = section(sec_head("Designed around your technology", "The room layout, absorber lining and positioners follow from what you need to measure.") + grid([
        card("antenna", "5G and telecommunications", "Base-station, handset and infrastructure antennas, measured in a quiet, repeatable environment."),
        card("signal", "Radar and aerospace", "Antenna and sensor development for airborne, marine and ground-based systems."),
        card("shield", "Military and marine", "Rugged, configurable ranges for defence communication and surveillance antennas."),
        card("wave", "Wi-Fi and wireless devices", "Compact test chambers for over-the-air checks on wireless products and modules."),
    ], 4), tone="tint")

    meas = section(split(
        c.img("antenna-room-2", "Interior of an antenna chamber with an antenna mast and a test head on a pedestal"),
        f'''<h2>What happens inside the chamber</h2>
<p>Pyramidal absorbers cover the walls, ceiling and floor so that signals leave the antenna and are absorbed rather than reflected. The result is a quiet zone in which patterns can be measured accurately and compared from one test to the next.</p>
{checklist(["Radiation pattern and beamwidth", "Gain and efficiency", "Polarisation behaviour", "Side-lobe and back-lobe levels", "Over-the-air performance of wireless devices"])}
<p>Absorber type, room dimensions and positioner design are fixed at the design stage once the frequency band and antenna size are known.</p>'''))

    spec = section(sec_head("Typical chamber features") + table(
        ["Feature", "What it does"],
        [
            ["Shielded steel enclosure", "Isolates the range from outside signals and stops test signals from leaking out"],
            ["Absorber lining on all surfaces", "Removes reflections so the quiet zone stays clean"],
            ["Shielded door and feedthroughs", "Let people and cables in without compromising the shield"],
            ["Positioners and mounting", "Rotate and hold the antenna or device under test for repeatable alignment"],
            ["Instrumentation access", "Filtered and shielded penetrations for RF and control cables"],
        ]), tone="tint")

    return hero + overview + apps + meas + spec + faq_html(ANTENNA_FAQ) + related(c, ["anechoic-emc-test-chambers", "automotive-military-emc-chambers", "shielded-rooms-faraday-cages"]) + cta_band(c)
