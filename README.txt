SHIELD TECH WEBSITE  (www.shieldtech.ae)   -  version 3: UI polish + futuristic motion, partner list updated
================================================================================

FOLDERS
  production/  Upload the CONTENTS of this folder to your web root (public_html).
               Clean URLs, sitemap.xml, robots.txt, canonical tags, schema markup, .htaccess.
  preview/     Same site, opens straight from your computer. Double-click preview/index.html.
  source/      Generator (Python). Edit text in source/lib/*.py, then run:  python3 build.py

WHAT'S NEW IN THIS VERSION (content and structure unchanged)
  - Animated RF-field hero: drifting network nodes, signal packets, radar rings and a scan beam
  - Scroll-reveal headings and cards, animated counters, scroll-progress bar
  - Spotlight and 3D-tilt cards, HUD-style image frames, animated chamber diagram
  - Smarter header, button effects, page transitions and a mobile quote bar
  - Pause/play button for animation. Visitors whose system asks for reduced motion get a calm static version.
  - Performance guards: animation pauses off-screen and thins itself out on slower devices.

PLEASE CONFIRM BEFORE GOING LIVE
  1. Email: the site shows info@shieldtech.ae. Make sure that mailbox exists, or change SITE["email"] in source/lib/core.py.
  2. Phone: your profile has no phone number, so none is shown. Add SITE["phone"] in source/lib/core.py and rebuild.
  3. Contact form: with no form service set, "Send enquiry" opens the visitor's email app addressed to your email.
     To receive enquiries directly, put a form-to-email service URL in SITE["form_endpoint"] and rebuild.
  4. Images: renders and photos come from your profile pages. Swap in real project photos when available.
  5. Claims: "20+ years", "over 100 dB" (forensic box) and the Kemar EMC partner name come from your profile.

AFTER UPLOAD (SEO)
  - Add the site in Google Search Console and submit https://www.shieldtech.ae/sitemap.xml
  - Force HTTPS and redirect shieldtech.ae to www.shieldtech.ae at your host.
