# Contributing

We welcome paper and resource suggestions that fit the scope and taxonomy of **Towards Agentic Robots: Model, Data, Environment, and Harness**.

Please open a [paper suggestion](https://github.com/qinchonghanzuibang/Awesome-Agentic-Robots/issues/new?template=paper-suggestion.yml) with:

- Paper title and paper URL.
- Proposed category or categories from the README taxonomy.
- Official project and code URLs, if available.
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

Each unique work has one record. Prefer `arxiv:` IDs, followed by `doi:` or another stable publication ID. Dates in YAML use `YYYY-MM` or `YYYY` and display as `YYYY/MM` in the README; unconfirmed project and code links use `null`. Category keys use `domain.category_name`, as listed in `scripts/validate.py`. Keep all supported placements in `categories`. Boundary works have empty category lists and `boundary: true`.

The generator changes only the marked paper-list region of the README. Edit the introduction, overview and citation outside that region directly. The validator checks structure, duplicate identities and titles, counts, and README freshness; it does not establish scientific fit or verify remote link availability.
