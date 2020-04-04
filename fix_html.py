"""Removes input cells from the generated HTML and adds a usable TOC.
"""

from bs4 import BeautifulSoup

with open('analyze.html') as fin:
    soup = BeautifulSoup(fin, features='lxml')

# Remove input cells.
for indiv in soup.select('div.input'):
    indiv.decompose()

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
        # This is the README warning - don't include it in the ToC, but put the ToC after it.
        h.insert_after(toc)
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

with open('analyze.html', 'w', encoding='utf-8') as fout:
    fout.write(str(soup))
