#!/usr/bin/env python3
"""Build the site's HTML pages from src/layout.html and src/pages/*.html.

The generated pages are written to the repository root, which is what gets
uploaded to the hosting. Run `python3 build.py` after editing anything in
src/; `python3 build.py --check` fails if the root pages are out of date.

A page source starts with a front matter block:

    ---
    title: Page title
    description: Meta description
    ---

Optional keys: `noindex: yes` (no indexing, no Open Graph) and `root: /`
(prefix for asset and menu links, for pages served at any URL depth).
The rest is the page body, placed inside <main> between the header and
the footer. It may end
with `<!-- @head -->` and/or `<!-- @scripts -->` blocks that go into <head>
and after the Bootstrap script.
"""
import datetime
import html
import pathlib
import sys

BASE_URL = 'http://www.vlabidem.cz/'
NAV = [
    ('index.html', 'Úvod'),
    ('taxes.html', 'Daně'),
    ('economy.html', 'Účetnictví'),
    ('wages.html', 'Mzdy'),
    ('commissions.html', 'Provize'),
    ('links.html', 'Odkazy'),
    ('contacts.html', 'Kontakty'),
]

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / 'src'


def parse(text):
    _, front, rest = text.split('---\n', 2)
    meta = dict(line.split(': ', 1) for line in front.splitlines())
    blocks = {'head': '', 'scripts': ''}
    for name in ('scripts', 'head'):
        marker = f'<!-- @{name} -->\n'
        if marker in rest:
            rest, blocks[name] = rest.split(marker, 1)
    return meta, rest, blocks


def render(name, text, layout):
    meta, body, blocks = parse(text)
    root = meta.get('root', '')
    attr = lambda s: html.escape(s, quote=True)
    if meta.get('noindex') == 'yes':
        head_meta = ['    <meta name="robots" content="noindex">']
    else:
        head_meta = [f'    <meta name="description" content="{attr(meta["description"])}">']
    head_meta.append(f'    <link rel="icon" href="{root}favicon.svg" type="image/svg+xml">')
    head_meta.append(f'    <link rel="icon" href="{root}favicon.ico" sizes="any">')
    if meta.get('noindex') != 'yes':
        url = BASE_URL + ('' if name == 'index.html' else name)
        head_meta += [
            '    <meta property="og:type" content="website">',
            '    <meta property="og:site_name" content="VLABIDEM s.r.o.">',
            '    <meta property="og:locale" content="cs_CZ">',
            f'    <meta property="og:title" content="{attr(meta["title"])}">',
            f'    <meta property="og:description" content="{attr(meta["description"])}">',
            f'    <meta property="og:url" content="{url}">',
        ]
    nav = ''.join(
        '              <li class="nav-item">'
        + (f'<a class="nav-link active" aria-current="page" href="{root}{href}">{label}</a>'
           if href == name else f'<a class="nav-link" href="{root}{href}">{label}</a>')
        + '</li>\n'
        for href, label in NAV)
    values = {
        'meta': '\n'.join(head_meta) + '\n',
        'title': meta['title'],
        'root': root,
        'head': blocks['head'],
        'nav': nav,
        'body': body,
        'year': str(datetime.date.today().year),
        'scripts': blocks['scripts'],
    }
    out = layout
    for key, value in values.items():
        out = out.replace('{{' + key + '}}', value)
    return out


def main():
    check = '--check' in sys.argv[1:]
    layout = (SRC / 'layout.html').read_text(encoding='utf-8')
    stale = []
    for src in sorted((SRC / 'pages').glob('*.html')):
        page = render(src.name, src.read_text(encoding='utf-8'), layout)
        target = ROOT / src.name
        if target.exists() and target.read_text(encoding='utf-8') == page:
            continue
        if check:
            stale.append(src.name)
        else:
            target.write_text(page, encoding='utf-8')
            print('built', src.name)
    if stale:
        sys.exit('out of date, run python3 build.py: ' + ', '.join(stale))


if __name__ == '__main__':
    main()
