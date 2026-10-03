#!/usr/bin/env python3
"""Validate the public collection locally; no network requests or writes."""
from collections import Counter
import re
from pathlib import Path
import sys
import unicodedata
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
    'Model': ['Training', 'Perception', 'Planning', 'Robot Control', 'Adaptation'],
    'Data': ['Collection', 'Filtering', 'Correction'],
    'Environment': ['Reconstruction', 'Task Generation', 'Benchmarking'],
    'Harness': ['Orchestration', 'Memory', 'Monitoring', 'Recovery', 'Skill Synthesis', 'Evolution'],
}
TAXONOMY = {f'{domain.lower()}.{name.lower().replace(" ", "_")}': (domain, name)
            for domain, names in DOMAINS.items() for name in names}
FIELDS = {'id', 'title', 'date', 'venue', 'paper', 'project', 'code',
          'categories', 'boundary'}


def normalize_title(title):
    return ''.join(c for c in unicodedata.normalize('NFKD', title).casefold()
                   if c.isalnum())


def load_papers(path=ROOT / 'data/papers.yaml'):
    papers = yaml.safe_load(path.read_text(encoding='utf-8'))
    if not isinstance(papers, list) or not papers:
        raise ValueError('Expected a nonempty list of paper records.')
    return papers


def validate(papers):
    ids, titles, urls = set(), {}, {}
    for p in papers:
        if not isinstance(p, dict) or set(p) != FIELDS:
            raise ValueError('Record fields must match the documented public schema.')
        identity = p['id']
        if not isinstance(identity, str) or not re.fullmatch(
                r'(?:arxiv:\d{4}\.\d{4,5}|doi:10\.\d{4,9}/\S+|(?:iclr|pmlr|work):[\w.-]+)', identity):
            raise ValueError(f'Invalid canonical ID: {identity!r}')
        if identity in ids:
            raise ValueError(f'Duplicate ID: {identity}')
        ids.add(identity)
        for field in ('title', 'venue', 'date', 'paper'):
            if not isinstance(p[field], str) or not p[field].strip():
                raise ValueError(f'{identity}: missing {field}')
        title = normalize_title(p['title'])
        if not title or title in titles:
            raise ValueError(f'Suspicious duplicate normalized title: {identity}, {titles.get(title)}')
        titles[title] = identity
        if not re.fullmatch(r'(?:19|20)\d{2}(?:-(?:0[1-9]|1[0-2]))?', p['date']):
            raise ValueError(f'{identity}: expected YYYY or YYYY-MM date')
        if type(p['boundary']) is not bool:
            raise ValueError(f'{identity}: boundary must be boolean')
        for field in ('categories',):
            values = p[field]
            if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
                raise ValueError(f'{identity}: {field} must be a list of category keys')
            if len(values) != len(set(values)) or set(values) - TAXONOMY.keys():
                raise ValueError(f'{identity}: duplicate or unknown taxonomy key in {field}')
        if p['boundary'] != (not p['categories']):
            raise ValueError(f'{identity}: boundary works must have empty category lists')
        for field in ('paper', 'project', 'code'):
            url = p[field]
            if url is None and field != 'paper':
                continue
            if not isinstance(url, str) or re.search(r'[\s<>"\\]', url):
                raise ValueError(f'{identity}: invalid {field} URL')
            parsed = urlsplit(url)
            if parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.username or parsed.password:
                raise ValueError(f'{identity}: invalid {field} URL')
        url = p['paper'].rstrip('/')
        if url in urls:
            raise ValueError(f'Duplicate paper URL: {identity}, {urls[url]}')
        urls[url] = identity
        if identity.startswith('arxiv:') and p['paper'] != 'https://arxiv.org/abs/' + identity[6:]:
            raise ValueError(f'{identity}: expected canonical arXiv paper URL')
    counts = Counter(c for p in papers for c in p['categories'])
    if TAXONOMY.keys() - counts.keys():
        raise ValueError('Every category must contain at least one indexed work.')
    return counts


def summary(papers):
    counts = validate(papers)
    indexed = [p for p in papers if not p['boundary']]
    lines = ['Awesome Agentic Robots validation', '',
             f'Landscape works: {len(papers)}', f'Indexed unique works: {len(indexed)}',
             f'Category placements: {sum(counts.values())}',
             f'Boundary works: {len(papers) - len(indexed)}']
    for domain in DOMAINS:
        count = sum(any(TAXONOMY[c][0] == domain for c in p['categories']) for p in indexed)
        lines += ['', f'{domain} ({count} unique works):']
        lines += [f'  {name}: {counts[key]}' for key, (d, name) in TAXONOMY.items() if d == domain]
    lines += ['', 'Metadata (all landscape works):']
    lines += [f'  {field.title()} URLs: {sum(bool(p[field]) for p in papers)}'
              for field in ('paper', 'project', 'code')]
    return '\n'.join(lines)


def main():
    try:
        papers = load_papers()
        validate(papers)
        from generate_readme import updated_readme
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        if readme != updated_readme(readme, papers):
            raise ValueError('README paper list is stale; run scripts/generate_readme.py.')
        if (ROOT / '.github/workflows').exists():
            raise ValueError('GitHub workflows are outside this repository scope.')
        print(summary(papers))
        print('\nPASS: structure and generated README are consistent.')
    except (ValueError, OSError, yaml.YAMLError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
