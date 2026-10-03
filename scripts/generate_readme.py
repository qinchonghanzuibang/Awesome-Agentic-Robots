#!/usr/bin/env python3
"""Update only the marked paper-list region; preserve all editorial text."""
from html import escape
from urllib.parse import quote

from validate import DOMAINS, ROOT, TAXONOMY, load_papers, validate

BEGIN = '<!-- BEGIN AUTO-GENERATED PAPER LIST -->'
END = '<!-- END AUTO-GENERATED PAPER LIST -->'


def link(label, url):
    target = escape(quote(url, safe=":/?#=&%+@~.-_"), quote=True)
    return f'<a href="{target}">{escape(label)}</a>'


def row(paper):
    resources = ' · '.join(link(label, paper[field]) for field, label in
                           [('project', 'Project'), ('code', 'Code')] if paper[field]) or '—'
    date = paper["date"].replace("-", "/")
    return ('<tr>'
            f'<td nowrap>{date}</td>'
            f'<td>{link(paper["title"], paper["paper"])}</td>'
            f'<td>{escape(paper["venue"])}</td>'
            f'<td nowrap>{resources}</td>'
            '</tr>')


def sorted_papers(papers):
    # Year-only precision sorts conservatively at the start of that year.
    return sorted(papers, key=lambda p: (-int(p['date'].replace('-', '').ljust(6, '0')),
                                         p['title'].casefold(), p['id']))


def table(papers):
    # HTML width attributes survive README sanitization; inline CSS does not.
    return ['<table width="100%">', '<thead><tr>',
            '<th width="10%" align="left">Date</th>',
            '<th width="65%" align="left">Paper</th>',
            '<th width="10%" align="left">Venue</th>',
            '<th width="15%" align="left">Resources</th>',
            '</tr></thead>', '<tbody>',
            *(row(p) for p in sorted_papers(papers)), '</tbody>', '</table>']


def render(papers):
    validate(papers)
    lines = []
    for domain in DOMAINS:
        lines += [f'### {domain}', '']
        for key, (d, name) in TAXONOMY.items():
            if d == domain:
                lines += [f'#### {name}', '', *table([p for p in papers if key in p['categories']]), '']
    return '\n'.join(lines)


def updated_readme(readme, papers):
    if readme.count(BEGIN) != 1 or readme.count(END) != 1 or readme.index(BEGIN) >= readme.index(END):
        raise ValueError('README must contain one ordered pair of generation markers.')
    before, rest = readme.split(BEGIN, 1)
    _, after = rest.split(END, 1)
    return before + BEGIN + '\n\n' + render(papers) + '\n' + END + after


def main():
    path = ROOT / 'README.md'
    result = updated_readme(path.read_text(encoding='utf-8'), load_papers())
    path.write_text(result, encoding='utf-8')
    print('Updated README paper-list region.')


if __name__ == '__main__':
    main()
