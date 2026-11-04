"""Page registry: URL, title, meta description, schema and body function for every page."""
from . import pages_main as pm
from . import pages_solutions_a as pa
from . import pages_solutions_b as pb
from .core import SOLUTION_BY_SLUG

S = "solutions/"


def _sol(slug, body, title, desc, faq, short, hero_img, stype, og="og-card.jpg"):
    s = SOLUTION_BY_SLUG[slug]
    return dict(
        path=S + slug, title=title, description=desc, body=body, faq=faq, hero_img=hero_img, og_image=og,
        crumbs=[("Solutions", "solutions"), (short, S + slug)],
        service=dict(name=s[1], type=stype),
    )


PAGES = [
    dict(path="", body=pm.home, hero_img="hero-absorbers", faq=pm.HOME_FAQ, webpage_type="WebPage",
         title="Anechoic Chambers & Shielded Rooms UAE | Shield Tech",
         description="Shield Tech manufactures EMC anechoic chambers, antenna chambers, Faraday cages and TEMPEST shielded rooms in Abu Dhabi, UAE. Request a quote today."),
    dict(path="solutions", body=pm.solutions_hub, webpage_type="CollectionPage", crumbs=[("Solutions", "solutions")],
         title="EMC Chambers & Shielding Solutions UAE | Shield Tech",
         description="Ten shielding solution areas from one UAE manufacturer: EMC chambers, antenna ranges, Faraday cages, TEMPEST rooms, forensic enclosures and more."),
    _sol("anechoic-emc-test-chambers", pa.anechoic,
         "Anechoic EMC Test Chambers UAE | Shield Tech",
         "Custom SAC-3, SAC-5, SAC-10, FAR-3 and pre-compliant anechoic EMC test chambers, manufactured in Abu Dhabi for emissions and immunity testing.",
         pa.ANECHOIC_FAQ, "Anechoic EMC chambers", "far3-interior", "EMC test chamber design and manufacture"),
    _sol("automotive-military-emc-chambers", pa.automotive,
         "Automotive & MIL-STD-461 EMC Chambers | Shield Tech",
         "CISPR 25 vehicle and component chambers and MIL-STD-461 military test chambers with steel structure and modular shielding, made in Abu Dhabi, UAE.",
         pa.AUTO_FAQ, "Automotive and military chambers", "auto-chamber", "Automotive and military EMC chamber manufacture"),
    _sol("antenna-measurement-chambers", pa.antenna,
         "Antenna Measurement Chambers UAE | Shield Tech",
         "Absorber-lined antenna measurement chambers for 5G, radar, telecom and wireless testing, configured for military, marine, aerospace and commercial use.",
         pa.ANTENNA_FAQ, "Antenna measurement chambers", "antenna-room", "Antenna measurement chamber design and manufacture"),
    _sol("shielded-rooms-faraday-cages", pb.shielded_rooms,
         "RF Shielded Rooms & Faraday Cages UAE | Shield Tech",
         "RF and EMI shielded rooms and Faraday cages in any size or shape, manufactured in Abu Dhabi for research, testing and secure facilities.",
         pb.SHIELDED_FAQ, "Shielded rooms and Faraday cages", "shielded-door", "RF shielded room and Faraday cage manufacture"),
    _sol("forensic-cyber-security-shielding", pb.forensic,
         "Forensic Faraday Rooms & Evidence Boxes | Shield Tech",
         "Forensic shielded rooms and a portable evidence box with over 100 dB shielding, isolating seized devices from Wi-Fi, Bluetooth, cellular and GPS.",
         pb.FORENSIC_FAQ, "Forensic and cyber security shielding", "forensic-room", "Forensic shielding design and manufacture"),
    _sol("tempest-emp-hemp-shielding", pb.tempest,
         "TEMPEST & EMP / HEMP Shielded Rooms UAE | Shield Tech",
         "TEMPEST shielded rooms to NATO SDIP-29/2 and EMP, NEMP and HEMP shielded rooms for defence, police, government and embassy facilities in the UAE.",
         pb.TEMPEST_FAQ, "TEMPEST and EMP / HEMP shielding", "shielded-room-a", "TEMPEST and EMP shielded room manufacture"),
    _sol("eeg-tem-medical-research-shielding", pb.eeg_tem,
         "EEG & TEM Shielded Rooms | Shield Tech",
         "EEG shielded rooms optimised for VLF and ELF, and TEM rooms with passive shielding and active cancellation, for hospitals, universities and labs.",
         pb.EEG_FAQ, "EEG, TEM and research shielding", "eeg-room", "EEG and TEM shielded room manufacture"),
    _sol("magnetic-field-shielding", pb.magnetic,
         "Magnetic Field Shielding for Power Systems | Shield Tech",
         "Shielded trunking and transformer and switchgear shielding that reduce 50 Hz magnetic fields from cables, bus-bars and substations near people.",
         pb.MAG_FAQ, "Magnetic field shielding", "trunking", "Magnetic field shielding design and manufacture"),
    _sol("shielded-data-centres-containers-tents", pb.mobile,
         "Shielded Data Centres, Containers & Tents | Shield Tech",
         "Shielded data centres, ISO 20 ft and 40 ft shielded containers and conductive shielded tents for secure, signal-isolated workspaces in the UAE.",
         pb.MOBILE_FAQ, "Data centres, containers and tents", "container-inside", "Shielded enclosure manufacture"),
    _sol("ehv-laboratories", pb.ehv,
         "EHV Laboratories & Lighting Chambers | Shield Tech",
         "Extra-high-voltage laboratory facilities and lighting test chambers for dielectric strength, temperature rise and operational testing above 100 kV.",
         pb.EHV_FAQ, "EHV laboratories", None, "High-voltage laboratory facility design"),
    dict(path="industries", body=pm.industries, crumbs=[("Industries", "industries")],
         title="Industries: Defence, Automotive, Telecom | Shield Tech",
         description="EMC chambers and shielded rooms for defence, government, automotive, telecom, healthcare, research, data centres and utilities across the UAE."),
    dict(path="standards", body=pm.standards, faq=pm.STANDARDS_FAQ, crumbs=[("Standards", "standards")],
         title="EMC Standards & Shielding Performance | Shield Tech",
         description="CISPR 25, ISO 11452, MIL-STD-461, NATO SDIP-29/2 and more: the standards our chambers are designed around, and how shielding effectiveness is measured."),
    dict(path="about", body=pm.about, webpage_type="AboutPage", crumbs=[("About", "about")],
         title="About Shield Tech | Chamber Manufacturer in Abu Dhabi",
         description="Shield Tech Steel Manufacturing LLC builds EMC chambers and shielded rooms at KEZAD, Abu Dhabi, with over two decades of anechoic chamber experience."),
    dict(path="contact", body=pm.contact, webpage_type="ContactPage", crumbs=[("Contact", "contact")],
         title="Request a Quote | Shield Tech Abu Dhabi",
         description="Request a quote for an EMC chamber, Faraday cage or shielded room. Send your standard, frequency range and footprint to our Abu Dhabi engineering team."),
    dict(path="privacy", body=pm.privacy, crumbs=[("Privacy policy", "privacy")],
         title="Privacy Policy | Shield Tech",
         description="How Shield Tech Steel Manufacturing LLC handles the information you send through shieldtech.ae."),
]

NOT_FOUND = dict(path="", body=pm.not_found, title="Page not found | Shield Tech",
                 description="The page you requested could not be found on www.shieldtech.ae.", robots="noindex,follow")

# Pages listed in sitemap.xml: (path, changefreq, priority)
SITEMAP_META = {"": ("monthly", "1.0"), "solutions": ("monthly", "0.9"), "contact": ("yearly", "0.8"),
                "privacy": ("yearly", "0.2")}
