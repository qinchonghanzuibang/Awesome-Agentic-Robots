# Contributing

We welcome paper and resource suggestions that fit the scope and taxonomy of **Towards Agentic Robots: Model, Data, Environment, and Harness**.

Please open a [paper suggestion](https://github.com/qinchonghanzuibang/Awesome-Agentic-Robots/issues/new?template=paper-suggestion.yml) with:

- Paper title and paper URL.
- Proposed category or categories from the README taxonomy.
- Official code URLs, if available.
- A 1–3 sentence explanation of how the work fits the collection.

Inclusion depends on relevance to the companion survey and support for the proposed placement. Suggestions are reviewed by the maintainers; submission does not guarantee inclusion.

## Local maintenance

Use Python 3.9 or newer. Install the single dependency in your preferred environment:

```sh
python3 -m pip install -r requirements.txt
```

Edit `data/papers.yaml`, then run:

```sh
python3 scripts/generate_readme.py
python3 scripts/validate.py
```

Each unique work has one record with `id`, `title`, `venue`, `year`, `publication_pending`, `paper`, `code`, and `categories`. Prefer `arxiv:` IDs, followed by `doi:` or another stable publication ID. `year` is the conference event or journal publication year, or first arXiv posting year for preprints. Set `publication_pending` to match the manuscript's provisional acceptance marker. Unconfirmed code links use `null`. Category keys use `domain.category_name`, as listed in `scripts/validate.py`.

For a manuscript refresh, compare the current four `tables/literature_*.tex` tables and their `survey_data/*_literature_index.json` source records in the Overleaf repository, then use `ref.bib` for full paper titles and stable identifiers. Preserve only visible table placements, code links, venue labels and years; commented-out rows stay excluded. Shared works have one record with the union of visible placements. The frozen `taxonomy_mapping.json` corpus and all bibliography entries are not automatically the current displayed collection. Retain existing publication URLs for proceedings-only works and canonical arXiv URLs for arXiv identities. The public generator reads YAML only; it does not synchronize Overleaf automatically.

The generator changes only the marked paper-list region of the README. Edit the overview and citation outside that region directly. The validator checks structure, duplicate identities and titles, counts, and README freshness; it does not establish scientific fit or verify remote link availability.
