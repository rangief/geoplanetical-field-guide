# Review status — 18 November 2026

Prepared for owner review. Publication is NOT approved. No Pages deployment workflow is included.

## Verification

- Original handoff SHA256 manifest: every entry matched.
- Installed source/requirements.txt into an isolated local environment.
- source/test_maintenance.py: PASS. Future patch simulation flags matching chapters, leaves unrelated chapters unchanged, and clears only the reviewed flag.
- tools/build_site.py and tools/test_site.py: PASS; all 16 chapters preserved.
- Headless Microsoft Edge: PASS at 1440, 390 and 320 pixels. Checked no horizontal overflow, repeated search, empty results, Escape reset, matching navigation visibility, keyboard skip link, hidden chapter hash navigation, all chapter anchors, relative credit/maintenance links and no JavaScript errors.
- Official Steam news checked 18 November 2026: latest displayed announcement was 1.1.4, dated 16 November. https://steamcommunity.com/app/940230/allnews/
- Exact current public build was not independently established. Build 26709373 remains the supplied recorded build. No gameplay verification was performed.

## Improvements to supplied reader

Search now indexes textContent so repeated searches can reliably include hidden chapters. Explicit hidden styling prevents navigation display rules overriding filtered links. Added keyboard skip link, focus indication, live result counts, Escape reset, hash navigation recovery, semantic chapter headings and working source/maintenance links. All chapter Markdown and review metadata remain unchanged.

## Publication after owner approval only

1. Place the approved source on `main` in this same repository.
2. Open https://github.com/rangief/geoplanetical-field-guide/settings/pages
3. Under **Build and deployment**, choose **Source: Deploy from a branch**.
4. Choose **Branch: main**, folder **/(root)**, then **Save**.
5. Wait for the Pages deployment to complete in Actions. Verify HTTPS, all 16 chapters and search at https://rangief.github.io/geoplanetical-field-guide/ before sharing.

The GitHub connector does not expose Pages configuration here, so the owner must perform the setting change after approving publication. Keep repository owner/name and the root index unchanged to preserve the address. Do not add a custom domain.

## Future patches

Use source/MAINTAINERS.md. Confirm official release notes/build; queue affected topics with patch_intake.py (use all when scope is uncertain); edit flagged chapter Markdown; record an honest review scope with review_chapter.py; rebuild and rerun both test scripts; review the diff and CHANGELOG before releasing. This is a manual editorial workflow, not automatic monitoring or automatic factual verification.
