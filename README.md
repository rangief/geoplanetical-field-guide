# Geoplanetical Â· Living Field Guide

An independent, community-informed, searchable guide to Geoplanetical, maintained as chapters so patches can be addressed without rewriting everything.

**Website (after GitHub Pages is enabled):** https://rangief.github.io/geoplanetical-field-guide/  
**Repository:** https://github.com/rangief/geoplanetical-field-guide  
**Source release:** Edition 0.1, reviewed against recorded Geoplanetical 1.1.4 / Steam build 26709373 (18 Nov 2026).

This is not an official game guide. Version notes describe the last recorded/reviewed state, not automatic compatibility with future game builds.

## Publication

The public site uses the root `index.html`. GitHub Pages should be configured for `main` / `/(root)` or an approved Pages deployment workflow. Keep `.nojekyll` in the root. No separate domain or paid hosting is necessary.

**Do not enable GitHub Pages or post its URL publicly until the owner has reviewed the staged site and explicitly approved publication.**

## Editing the guide

Edit only the affected `source/chapters/*.md`, not a generated snapshot. Refer to `source/MAINTAINERS.md` for patch intake, verification notes and release history.

From the repository root:

```bash
python -m pip install -r source/requirements.txt
python source/test_maintenance.py
python tools/build_site.py
python tools/test_site.py
```

`tools/build_site.py` regenerates `source/Geoplanetical_Living_Field_Guide.html`, the full Markdown, and the root `index.html`. Inspect the diff before committing.

## Contributor credit and limits

Community research credited to Balee_92, warmaninger, grayassembly and Traslo. See `source/SOURCES.md` for provenance and caveats. Exact older numerical rules and all 107 goods recipes must not be advertised as verified for new builds without supporting evidence. No community raw guide collection or private game files are bundled.

## Steam link after site approval

`[url=https://rangief.github.io/geoplanetical-field-guide/]Read the Geoplanetical Living Field Guide[/url]`

The address above will work only after Pages is actually enabled and deployed.
