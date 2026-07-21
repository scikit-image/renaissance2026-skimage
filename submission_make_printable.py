#!/usr/bin/env python3
#
# On the final preview page, view source, click on HTML, save inner HTML as inner.html.
# Run this script.
#

import html
import sys
from pathlib import Path

from bs4 import BeautifulSoup


def build_sections(soup):
    review = soup.find(id='widget-uCJ9BpMNGgNGTRNdjBqTAS')
    sections = []
    for group in review.select('div.py-3.px-1'):
        dl = group.find('dl')
        if not dl:
            continue
        btn = group.find('button', attrs={'aria-label': True})
        label = btn['aria-label'] if btn else ""
        section_name = label.replace('Edit: ', '') if label.startswith('Edit: ') else "Other"
        dts = dl.find_all('dt')
        dds = dl.find_all('dd')
        rows = []
        for dt, dd in zip(dts, dds):
            key = dt.get_text(strip=True)
            val = dd.get_text('\n', strip=True)
            rows.append((key, val))
        if rows:
            sections.append((section_name, rows))
    return sections


def esc(s):
    return html.escape(s)


def render(sections):
    rows_html = []
    for name, rows in sections:
        rows_html.append(f'<h2>{esc(name)}</h2>')
        rows_html.append('<dl class="qa">')
        for k, v in rows:
            v_html = '<br>'.join(esc(line) for line in v.split('\n'))
            rows_html.append(f'  <div class="row"><dt>{esc(k)}</dt><dd>{v_html}</dd></div>')
        rows_html.append('</dl>')
    body = '\n'.join(rows_html)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Full Proposal Form - Submission</title>
<style>
  :root {{
    color-scheme: light;
  }}
  body {{
    font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 1.5rem;
    color: #1a1a1a;
    line-height: 1.5;
  }}
  h1 {{
    font-size: 1.6rem;
    margin-bottom: 0.25rem;
  }}
  .subtitle {{
    color: #666;
    margin-top: 0;
    margin-bottom: 2rem;
  }}
  h2 {{
    font-size: 1.05rem;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    color: #444;
    border-bottom: 2px solid #333;
    padding-bottom: 0.3rem;
    margin-top: 2.2rem;
    margin-bottom: 0.8rem;
  }}
  dl.qa {{
    margin: 0;
  }}
  .row {{
    display: grid;
    grid-template-columns: minmax(160px, 32%) 1fr;
    gap: 1rem;
    padding: 0.55rem 0;
    border-bottom: 1px solid #e5e5e5;
    break-inside: avoid;
  }}
  dt {{
    font-weight: 600;
    color: #555;
    font-size: 0.92rem;
  }}
  dd {{
    margin: 0;
    white-space: normal;
  }}
  @media print {{
    body {{ margin: 0.5in; max-width: none; }}
    h2 {{ break-after: avoid; }}
    .row {{ break-inside: avoid; }}
    a {{ color: inherit; text-decoration: none; }}
  }}
</style>
</head>
<body>
<h1>Full Proposal Form</h1>
<p class="subtitle">Submission review</p>
{body}
</body>
</html>
"""


def main():
    script_dir = Path(__file__).resolve().parent
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else script_dir / 'inner.html'
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else script_dir / 'inner_printable.html'

    data = src.read_text(encoding='utf-8', errors='ignore')
    soup = BeautifulSoup(data, 'html.parser')
    sections = build_sections(soup)
    out = render(sections)
    dst.write_text(out, encoding='utf-8')
    print(f"wrote {dst} ({len(out)} bytes)")


if __name__ == '__main__':
    main()
