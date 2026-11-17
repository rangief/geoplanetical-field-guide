# How to keep the field guide useful after every Geoplanetical patch

This guide is built to be **repairable in small pieces**, not guaranteed to be correct forever. The difference matters: an update notice should visibly flag stale chapters until somebody verifies them.

## Files that matter

- `chapters/NN-topic.md`: one editable chapter each; editing one doesn't disturb the others.
- `data/chapters.json`: which chapters depend on which game systems and their last review status.
- `data/patches.json`: record of game updates and their affected topics.
- `CHANGELOG.md`: human-readable history of edits.
- `SOURCES.md`: contributors, provenance, limits.
- `patch_intake.py`: queue relevant chapters after a new game patch.
- `review_chapter.py`: record that a chapter was checked *after you actually check/edit it*.
- `build_guide.py`: produce the shareable `.md` and `.html` versions.

## When a new update arrives

**Step 1:** Find the developer's original Steam patch note and confirm the public build ID. Read the *actual* changes rather than guessing which chapters are affected.

**Step 2:** Record the patch and its changed topics. Example (replace values):

```bash
python patch_intake.py --game-version 1.1.5 --build 26799999 --released 2026-11-21 \
  --url https://steamcommunity.com/app/940230/allnews/ \
  --topics inflation,budget,politics \
  --summary "Inflation and election balancing updates"
```

This marks matching chapters **NEEDS REVIEW** and leaves unrelated chapters untouched. It does not silently rewrite any text.

**Step 3:** Examine the flagged chapters and replace only the affected paragraphs. If the patch is vague, label uncertain details **not yet verified**. For game-specific rules, cross-check the current game and a repeatable save if possible.

**Step 4:** Mark each chapter as reviewed, only when that review is genuinely finished:

```bash
python review_chapter.py --chapter 07-inflation-and-currency --build 26799999 \
  --game-version 1.1.5 --note "Read patch; tested Price Pressure layout in-game"
```

This writes a record into the changelog and records the review scope; it **does not** mean all formulas were gameplay-tested. State that in the note.

**Step 5:** Rebuild the reading editions:

```bash
python build_guide.py
```

## Automated test

```bash
python test_maintenance.py
```

This tests that an unrelated chapter stays untouched when the next patch affects only one system. It does not test game mechanics.

## Review triggers and safe defaults

- **Inflation / budget:** recheck old thresholds, interest-rate advice, tax effects, currency behaviour.
- **Industry / trade / construction:** recheck goods recipes, import shares, project bottlenecks and menu paths.
- **Energy / reserves:** recheck plant sites, storage, reserve categories and supply routes.
- **Politics / population:** recheck approval, movements, election and family-policy timings.
- **War / diplomacy / sanctions:** recheck combat-base permissions, army behaviours, negotiation flow and occupation effects.
- **Research / space:** recheck points, unlocks, missions and Moon panels.
- **Interface:** recheck any quoted button labels or navigation paths.

If a patch's scope is unclear, pass `--topics all` to flag every chapter instead of pretending nothing changed.

## Editorial consistency

Each chapter should keep four elements: a simple main idea, a practical in-game investigation, a short illustrative example, and a *patch watch/evidence note*. Avoid long statistical tables unless the value is actively version-verified. Don't quietly copy entire third-party guides. Cite the original contributors and patch source in release material.

## Updating Steam or another website

Keep this editable source archive as the master copy. Generate a fresh HTML edition and/or copy the affected Markdown text into Steam-friendly BBCode. Do not edit the only master in Steam; otherwise the two copies diverge.

## Monitoring

Scripts here work **offline**; they do not continuously monitor Steam, access the game, or update themselves. Monitoring future game patches requires a separate scheduled check or a person running Step 1. A future patch without an entry in `patches.json` will not be detected automatically.
