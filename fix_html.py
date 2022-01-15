"""Removes input cells from the generated HTML and adds a usable TOC.
"""

import sys

from bs4 import BeautifulSoup

def fix(fname, all_fnames):
    print('fixing', fname, '...')
    with open(fname, encoding='utf-8') as fin:
        soup = BeautifulSoup(fin, features='lxml')

    # Remove input cells.
    for indiv in soup.select('div.input'):
        indiv.decompose()

    other_analyses_links_html = []
    binder_url = 'https://mybinder.org/v2/gh/ibudiselic/covid/master?filepath=binder_sandbox.ipynb'
    other_analyses_links_html.append(f'<li><a href="{binder_url}">Binder sandbox (takes a few minutes to load)</a></li>')
    for other_fname in all_fnames:
        if other_fname == fname:
            continue
        other_analyses_links_html.append(f'<li><a href="{other_fname}">{other_fname.split(".")[0].title()}</a></li>')

    other_analyses = BeautifulSoup(f'<div><h2>Other analyses</h2><ul>{"".join(other_analyses_links_html)}</ul></div>', features='lxml').div
    toc = BeautifulSoup('<div style="margin-top: 40px;"><h1 id="fixhtmltoc">Table of Contents</h1><ul></ul></div>', features='lxml').div
    toc_ul = toc.ul

    h1_level = -1
    h2_level = 0
    for h in soup.select('h1,h2,h3'):
        # Remove useless generated anchors.
        anchors = h.select('a.anchor-link')
        assert(len(anchors) <= 1)
        if len(anchors) == 1:
            anchors[0].decompose()
        if h1_level == -1 and h.name == 'h1':
            # This is the README warning - don't include it in the ToC, but put cross-links and the ToC after it.
            h.insert_after(toc)
            h.insert_after(other_analyses)
            h1_level = 0
            continue

        htxt = h.get_text()
        back_to_toc = soup.new_tag('a', href='#fixhtmltoc', title='Back to ToC')
        back_to_toc.string = '⮸'
        h.append(back_to_toc)
        if h.name == 'h1':
            h1_level += 1
            h2_level = 0
        elif h.name == 'h2':
            h2_level += 1
        else:
            continue

        hid = f'h{h1_level}.{h2_level}'
        li_code = f'<li><a href="#{hid}">{htxt}</a></li>'
        new_entry = BeautifulSoup(li_code, features='lxml').li
        h['id'] = hid
        if h.name == 'h1':
            toc_ul.append(new_entry)
            toc_h2_ul = soup.new_tag('ul')
            new_entry.append(toc_h2_ul)
            h1_level += 1
            h2_level = 0
        elif h.name == 'h2':
            toc_h2_ul.append(new_entry)
            h2_level += 1

    with open(fname, 'w', encoding='utf-8') as fout:
        fout.write(str(soup))

fnames = sys.argv[1:]
for fname in fnames:
    fix(fname, fnames)
