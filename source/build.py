#!/usr/bin/env python3
"""Build the Shield Tech website.

    python3 build.py            -> dist/production, dist/preview, dist/artifact

production : root-absolute clean URLs (/solutions/x/). Upload the CONTENTS of this folder to the web root.
preview    : relative links ending in index.html. Opens straight from disk, no server needed.
artifact   : like preview, but Poppins comes from Google Fonts (used for the hosted preview).
"""
import datetime
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from lib.core import SITE, render_page  # noqa: E402
from lib.registry import PAGES, NOT_FOUND, SITEMAP_META  # noqa: E402

SRC = os.path.join(ROOT, "src", "assets")
DIST = os.path.join(ROOT, "dist")
TODAY = datetime.date.today().isoformat()

FONT_FILES = [400, 500, 600, 700, 800]


def font_face(prefix="../fonts/"):
    return "\n".join(
        f'@font-face {{ font-family: "Poppins"; font-style: normal; font-weight: {w}; font-display: swap; '
        f'src: url({prefix}poppins-latin-{w}-normal.woff2) format("woff2"); }}' for w in FONT_FILES)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def copy_assets(out, mode):
    dst = os.path.join(out, "assets")
    shutil.copytree(SRC, dst, ignore=shutil.ignore_patterns("_manifest.json", "site.css", "site.artifact.css", "*.psd"))
    css = open(os.path.join(SRC, "css", "site.css"), encoding="utf-8").read()
    if "/*FONTFACE*/" not in css:
        raise SystemExit("site.css is missing the /*FONTFACE*/ marker")
    os.makedirs(os.path.join(dst, "css"), exist_ok=True)
    if mode == "artifact":
        write(os.path.join(dst, "css", "site.artifact.css"), css.replace("/*FONTFACE*/", ""))
        shutil.rmtree(os.path.join(dst, "fonts"), ignore_errors=True)
    else:
        write(os.path.join(dst, "css", "site.css"), css.replace("/*FONTFACE*/", font_face()))
    write(os.path.join(dst, "site.webmanifest"),
          '{"name":"Shield Tech","short_name":"Shield Tech","start_url":"/","display":"standalone","background_color":"#ffffff",'
          '"theme_color":"#084771","icons":[{"src":"/assets/img/icon-192.png","sizes":"192x192","type":"image/png"},'
          '{"src":"/assets/img/icon-512.png","sizes":"512x512","type":"image/png"}]}\n')


def page_file(out, path):
    return os.path.join(out, "index.html") if path == "" else os.path.join(out, path, "index.html")


def sitemap():
    rows = []
    for p in PAGES:
        cf, pr = SITEMAP_META.get(p["path"], ("monthly", "0.7"))
        if p["path"].startswith("solutions/"):
            pr = "0.8"
        loc = SITE["url"] + ("/" if p["path"] == "" else "/" + p["path"] + "/")
        rows.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n"


HTACCESS = """# Shield Tech: optional Apache settings. Safe to delete if your host is not Apache.
ErrorDocument 404 /404.html
DirectoryIndex index.html
Options -Indexes

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json application/xml image/svg+xml
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType text/css "access plus 1 week"
  ExpiresByType application/javascript "access plus 1 week"
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>
"""


def build(mode, name):
    out = os.path.join(DIST, name)
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    copy_assets(out, mode)
    for p in PAGES:
        write(page_file(out, p["path"]), render_page(p, mode))
    write(os.path.join(out, "404.html"), render_page(NOT_FOUND, mode))
    if mode == "prod":
        write(os.path.join(out, "sitemap.xml"), sitemap())
        write(os.path.join(out, "robots.txt"), f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
        write(os.path.join(out, ".htaccess"), HTACCESS)
        shutil.copy(os.path.join(SRC, "img", "favicon.ico"), os.path.join(out, "favicon.ico"))
    return out


if __name__ == "__main__":
    only = sys.argv[1:] or ["production", "preview", "artifact"]
    modes = {"production": "prod", "preview": "local", "artifact": "artifact"}
    for name in only:
        o = build(modes[name], name)
        n = sum(len(f) for _, _, f in os.walk(o))
        print(f"{name:11s} -> {o}  ({n} files)")
