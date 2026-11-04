"""Inline SVG artwork: hero shield and the interactive anechoic chamber cross-section."""
from .core import icon

SHIELD_D = ("M200 10 C140 38 80 56 20 58 L16 72 L14 250 C14 360 90 420 200 472 "
            "C310 420 386 360 386 250 L384 72 L380 58 C320 56 260 38 200 10 Z")


def hero_art(c):
    img = c.a("img/far3-interior.webp")
    rings = "".join(f'<circle class="ring" style="--i:{i}" cx="52" cy="235" r="44"/>' for i in range(5))
    return f'''<svg class="hero-art" viewBox="0 0 640 500" role="img" aria-labelledby="ha-t ha-d" focusable="false">
<title id="ha-t">Radio waves stopping at a shield</title>
<desc id="ha-d">Concentric radio waves travel from an emitter on the left and stop at the edge of a shield that frames the inside of an anechoic chamber.</desc>
<defs>
<clipPath id="ha-sh"><path transform="translate(250 12) scale(.93)" d="{SHIELD_D}"/></clipPath>
<clipPath id="ha-air"><rect x="0" y="0" width="262" height="500"/></clipPath>
<pattern id="ha-facet" width="44" height="44" patternUnits="userSpaceOnUse">
<polygon points="0,0 44,0 22,22" fill="#fff" opacity=".13"/><polygon points="44,0 44,44 22,22" fill="#53b9e5" opacity=".10"/>
<polygon points="44,44 0,44 22,22" fill="#04243b" opacity=".30"/><polygon points="0,44 0,0 22,22" fill="#1f659c" opacity=".14"/>
</pattern>
<linearGradient id="ha-fade" x1="0" x2="0" y1="0" y2="1"><stop offset=".55" stop-color="#04243b" stop-opacity="0"/><stop offset="1" stop-color="#04243b" stop-opacity=".78"/></linearGradient>
<linearGradient id="ha-scan" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#53b9e5" stop-opacity="0"/><stop offset=".82" stop-color="#53b9e5" stop-opacity=".38"/><stop offset="1" stop-color="#d4f1ff" stop-opacity=".95"/></linearGradient>
</defs>
<g clip-path="url(#ha-air)" class="rings">{rings}</g>
<g class="emitter" transform="translate(52 235)"><circle r="7" fill="#53b9e5"/><circle r="15" fill="none" stroke="#53b9e5" stroke-opacity=".5" stroke-width="1.5"/></g>
<g clip-path="url(#ha-sh)"><image href="{img}" x="236" y="0" width="400" height="500" preserveAspectRatio="xMidYMid slice"/>
<rect x="236" y="0" width="400" height="500" fill="url(#ha-facet)"/><rect x="236" y="0" width="400" height="500" fill="url(#ha-fade)"/>
<rect class="scan" x="236" y="-90" width="400" height="90" fill="url(#ha-scan)" opacity="0"/></g>
<path class="rim" transform="translate(250 12) scale(.93)" d="{SHIELD_D}" fill="none" stroke="#08476d" stroke-width="13" stroke-linejoin="round"/>
<path transform="translate(261 26) scale(.875)" d="{SHIELD_D}" fill="none" stroke="#53b9e5" stroke-opacity=".75" stroke-width="2" stroke-linejoin="round"/>
<path class="rim-hit" transform="translate(250 12) scale(.93)" d="{SHIELD_D}" fill="none" stroke="#53b9e5" stroke-width="6" stroke-linejoin="round" opacity="0"/>
<path class="trace" transform="translate(261 26) scale(.875)" d="{SHIELD_D}" pathLength="100" fill="none" stroke="#d4f1ff" stroke-width="3.2" stroke-linecap="round" stroke-dasharray="6 94" opacity="0"/>
<path class="trace trace--b" transform="translate(261 26) scale(.875)" d="{SHIELD_D}" pathLength="100" fill="none" stroke="#53b9e5" stroke-width="3.2" stroke-linecap="round" stroke-dasharray="6 94" opacity="0"/>
</svg>'''


def _zig_down(x0, y, n, w, h):
    pts = [f"M{x0} {y}"]
    for i in range(n):
        pts.append(f"L{x0 + w * i + w / 2:g} {y + h} L{x0 + w * (i + 1):g} {y}")
    return " ".join(pts) + " Z"


def _zig_up(x0, y, n, w, h):
    pts = [f"M{x0} {y}"]
    for i in range(n):
        pts.append(f"L{x0 + w * i + w / 2:g} {y - h} L{x0 + w * (i + 1):g} {y}")
    return " ".join(pts) + " Z"


def _zig_right(x, y0, n, w, h):
    pts = [f"M{x} {y0}"]
    for i in range(n):
        pts.append(f"L{x + h} {y0 + w * i + w / 2:g} L{x} {y0 + w * (i + 1):g}")
    return " ".join(pts) + " Z"


def _zig_left(x, y0, n, w, h):
    pts = [f"M{x} {y0}"]
    for i in range(n):
        pts.append(f"L{x - h} {y0 + w * i + w / 2:g} L{x} {y0 + w * (i + 1):g}")
    return " ".join(pts) + " Z"


PARTS = [
    ("shield", "Shielded enclosure",
     "A closed steel shell working as a Faraday cage. It keeps outside radio signals out of the test volume and keeps emissions from the equipment under test from leaking out."),
    ("absorbers", "Absorbers",
     "Carbon-loaded foam pyramids and ferrite tiles line the walls and ceiling. They soak up radio energy instead of reflecting it, which keeps measurements repeatable."),
    ("turntable", "Turntable and test table",
     "The equipment under test (EUT) sits on a turntable so it can be measured from every angle. Larger chambers take larger turntables and heavier loads."),
    ("antenna", "Antenna mast",
     "The receiving antenna sits at the standard test distance. In a semi-anechoic chamber it scans between 1 m and 4 m in height to catch the strongest signal."),
    ("floor", "Ground plane",
     "A semi-anechoic chamber has a metal floor that reflects, as the test standards require. A fully anechoic chamber lines the floor with absorbers instead."),
    ("door", "Door and feedthroughs",
     "Shielded doors, filtered power and signal feedthroughs and waveguide ventilation let people, cables and air in without opening a path for interference."),
]
PART_FAR_FLOOR = ("floor", "Floor absorbers",
                  "A fully anechoic chamber (FAR) lines the floor with absorbers too, so there are no ground reflections. The antenna stays at one fixed height, which shortens each test run.")


def anatomy(c):
    ceil = _zig_down(68, 58, 26, 24, 26)
    lwall = _zig_right(68, 58, 8, 28, 26)
    rwall = _zig_left(692, 58, 8, 28, 26)
    floor_abs = _zig_up(68, 282, 26, 24, 26)

    # Signal paths. Geometry: EUT right edge (216,243), antenna dipole (524,181); floor bounce point (302,282) is where the
    # straight line from the EUT to the mirror image of the antenna crosses the ground plane. FAR mode raises the EUT and lowers the antenna to y=217.
    def pulse(cls, d, dur, delay):
        return (f'<path class="ray ray--pulse {cls}" d="{d}" pathLength="100" fill="none" stroke="#d4f1ff" stroke-width="3.6" '
                f'stroke-linecap="round" stroke-dasharray="7 93" stroke-dashoffset="7" opacity="0" style="--dur:{dur}s;animation-delay:-{delay}s"/>')
    direct = "M216 243 L524 181"
    refl = "M216 243 L302 282 L524 181"
    far = "M216 217 L524 217"
    sac_rays = (
        f'<path class="ray ray--base" d="{direct}" fill="none" stroke="#53b9e5" stroke-opacity=".38" stroke-width="1.6" stroke-dasharray="2 7" stroke-linecap="round"/>'
        f'<path class="ray ray--base" d="{refl}" fill="none" stroke="#8fd3f3" stroke-opacity=".34" stroke-width="1.6" stroke-dasharray="2 7" stroke-linecap="round" stroke-linejoin="round"/>'
        + pulse("ray--d", direct, 3.2, 0) + pulse("ray--d", direct, 3.2, 1.6)
        + pulse("ray--r", refl, 3.45, 0) + pulse("ray--r", refl, 3.45, 1.725)
        + '<circle class="bounce" cx="302" cy="282" r="6" fill="none" stroke="#d4f1ff" stroke-width="2" opacity="0" style="--dur:3.45s"/>'
        + '<circle class="bounce" cx="302" cy="282" r="6" fill="none" stroke="#d4f1ff" stroke-width="2" opacity="0" style="--dur:3.45s;animation-delay:-1.725s"/>'
    )
    far_rays = (
        f'<path class="ray ray--base" d="{far}" fill="none" stroke="#53b9e5" stroke-opacity=".38" stroke-width="1.6" stroke-dasharray="2 7" stroke-linecap="round"/>'
        + pulse("ray--d", far, 3.14, 0) + pulse("ray--d", far, 3.14, 1.57)
    )
    absorbed = "".join(
        f'<path class="ray ray--abs" d="{d}" pathLength="100" fill="none" stroke="#8fd3f3" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="7 93" stroke-dashoffset="7" opacity="0" style="--k:{k}"/>'
        for k, d in enumerate(["M196 222 L150 88", "M206 222 L330 88", "M164 236 L96 236"])
    )
    rays_svg = (f'<g class="d-rays" aria-hidden="true"><g class="rays rays--sac">{sac_rays}</g><g class="rays rays--far">{far_rays}</g>'
                f'<g class="d-absorbed">{absorbed}</g></g>')
    buttons = ""
    for key, name, desc in PARTS:
        label = f'<span class="lbl-sac">{name}</span>' if key != "floor" else '<span class="lbl-sac">Ground plane</span><span class="lbl-far">Floor absorbers</span>'
        buttons += f'<li><button type="button" class="part" data-part="{key}" data-desc-sac="{desc}" data-desc-far="{PART_FAR_FLOOR[2] if key == "floor" else desc}" aria-pressed="false">{label}</button></li>'
    svg = f'''<svg class="anatomy__svg" viewBox="0 0 760 360" role="img" aria-labelledby="an-t an-d" focusable="false">
<title id="an-t">Cross-section of an anechoic chamber</title>
<desc id="an-d">Side view of a shielded steel box lined with pyramid absorbers, with a turntable and test object on the left, an antenna mast on the right, a door in the right wall and a dimension line for the test distance below.</desc>
<g data-part="shield"><rect class="d-shell" x="60" y="50" width="640" height="240" fill="none" stroke-width="8"/>
<rect x="46" y="190" width="14" height="44" class="d-feed"/><path d="M50 200h6M50 212h6M50 224h6" stroke="currentColor" stroke-width="1.5" class="d-feedline"/></g>
<g data-part="absorbers" class="d-abs"><path d="{ceil}"/><path d="{lwall}"/><path d="{rwall}"/><g class="d-floorabs"><path d="{floor_abs}"/></g></g>
<g data-part="floor"><line class="d-ground" x1="68" y1="282" x2="692" y2="282" stroke-width="5"/></g>
{rays_svg}
<g data-part="turntable" class="d-turn"><ellipse class="d-turnring" cx="190" cy="270" rx="66" ry="8" fill="none" stroke="#8fd3f3" stroke-opacity=".6" stroke-width="1.6" stroke-dasharray="6 8"/><rect class="d-plat" x="140" y="264" width="100" height="12" rx="2"/><rect class="d-eut" x="164" y="222" width="52" height="42" rx="2"/><path class="d-eutline" d="M172 236h36M172 246h36M172 256h36" stroke-width="1.5"/></g>
<g data-part="antenna" class="d-ant"><line class="d-mast" x1="560" y1="282" x2="560" y2="96" stroke-width="4"/>
<g class="d-antbox"><rect x="540" y="168" width="40" height="26" rx="2"/><path d="M540 181h-16M524 172v18" class="d-dipole" stroke-width="3"/></g>
<g class="d-scan"><path d="M604 112v140M598 120l6-8 6 8M598 244l6 8 6-8" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></g></g>
<g data-part="door"><rect class="d-door" x="688" y="196" width="16" height="86" rx="2"/><circle cx="696" cy="240" r="2.6" class="d-knob"/></g>
<g class="d-dim"><path d="M190 324h370M190 316v16M560 316v16" fill="none" stroke-width="2"/><path d="M190 324l9-5v10zM560 324l-9-5v10z"/></g>
</svg>'''
    return f'''<div class="anatomy" data-mode="sac">
<div class="anatomy__fig"><div class="anatomy__modes" role="radiogroup" aria-label="Chamber type">
<button type="button" role="radio" aria-checked="true" data-mode="sac">Semi-anechoic (SAC)</button>
<button type="button" role="radio" aria-checked="false" data-mode="far">Fully anechoic (FAR)</button></div>
<div class="anatomy__plate">{svg}</div>
<p class="anatomy__cap"><strong>Test distance:</strong> 3 m, 5 m or 10 m between the antenna and the equipment under test, set by the standard and the size of the product.</p></div>
<div class="anatomy__panel"><p class="anatomy__hint">Select a part to see what it does.</p>
<ul class="parts">{buttons}</ul>
<div class="anatomy__desc" aria-live="polite"><h3 class="anatomy__name">Shielded enclosure</h3><p class="anatomy__text">{PARTS[0][2]}</p></div></div></div>'''
