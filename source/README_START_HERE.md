# Geoplanetical · Living Player's Field Guide

**Guide edition:** 0.1, created 18 November 2026  
**Game version reviewed against:** 1.1.4, public Steam build 26709373  
**Nature:** Independent community-informed guide, not official and not an automatic live game feed

## To read

**Double-click `Geoplanetical_Living_Field_Guide.html`** in a browser. It has search and 16 simple chapters. No internet connection is required to read it. The current update status is displayed above each chapter.

`Geoplanetical_Living_Field_Guide.md` is an alternate single-file editable/readable copy.

## To make a small correction

Open a single relevant `.md` file under `chapters/` in any text editor. Run `python build_guide.py` to regenerate the reader and full Markdown. If prompted, install the small Markdown converter with `python -m pip install -r requirements.txt`.

## When Geoplanetical gets patched

Follow `MAINTAINERS.md`: record the new build with `patch_intake.py` and specify the affected topics. The system flags relevant chapters as **Needs review**, not as automatically correct. After reviewing/editing a chapter, record the verified scope with `review_chapter.py`, then rebuild. All changes are tracked in `CHANGELOG.md`.

## Rules that protect the guide's accuracy

- **Developer patch note** ≠ every related rule has been gameplay-tested.
- **Community code reading** ≠ observed in a running campaign.
- **Old precise numbers** ≠ verified for the latest build.
- **No patch record** ≠ no patch exists. Someone or a scheduled monitoring task must check Steam.
- The complete 107-goods recipe data from Balee_92's hosted map was *not* included in the original text upload and is not fabricated here.

The original guide collection remains in the conversation as `geo guide.txt`. Credits and source URLs are in `SOURCES.md`.
