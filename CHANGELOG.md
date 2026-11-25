# Changelog

What changed in this repository, which describes the AURORA database and holds read-only examples of its
API. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This file is not the
release history of the data: no release is published yet.

Figures below are the ones in [`data/numbers.json`](data/numbers.json), with the date each was read.

## [Unreleased] (2026-11-25): Quickstart and production checked with an account

Documentation only. New [`docs/QUICKSTART.md`](docs/QUICKSTART.md): sign-up, approval e-mail, API keys, first calls, cursors, rate limit and errors, and a table of what production offers. Checked on 2026-11-25 against production with an approved test account: sign-in 200; scopes `read`, `download`, `collaborate`, `download_nc` held with no second acceptance; an API key created, used on compounds, search and collections (200), refused on bioactivity, bundles, the one-compound package and the account (`403 api_key_not_allowed`), then revoked; a signed link of an NC bundle served by range (206); bioactivity 200 with the session; similarity search 503; pipeline funnel 404; rate limit 429 after the 60 per 60 seconds budget; `/health/*` and the OpenAPI file not exposed on the public address; only the Home and sign-in pages open without an account. `README.md`, `docs/API.md`, `docs/FAQ.md` and the two examples now say so. Not proven: the new acceptance of the Terms and Policy 1.1 at sign-in (the API does not expose it), the refusal of a key after it is revoked.

## [Unreleased] (2026-11-24): platform commit `4df61e1` in production, approval e-mail on

Documentation only. Commit `4df61e1` of platform version 1.5.2 has been in production since 2026-11-24, about 14:53 UTC, with no database migration. Read on the platform's VM by the platform's node and in its deploy report (`docs/deploy/2026-11-24-relatorio-do-deploy-sessao-e-email.md` of the platform repository). What changed for a person: the e-mail that says an account is approved is now sent, from `contact@alchemia.solutions`, with a button to the login page; the sign-in page can keep a person signed in on a device (14 days idle, 30 days at most), and a signed-in person can change the e-mail address by a link sent to the new one; the sign-in page has larger tab names and a larger AURORA mark. Not proven in production: the stay-signed-in box and the e-mail change with an account, and the sign-in and download paths with an account. `docs/API.md`, `docs/FAQ.md` and `docs/COLLECTIONS.md` had their statements about the Terms and Policy 1.1 and the `#downloads` section brought up to date; their route tables still follow the 1.5.1 contract, which was not read again.

## [Unreleased] (2026-11-23, evening): platform 1.5.2 in production

Documentation only. Platform version 1.5.2 (commit `9363ed5`) has been in production since 2026-11-23, 22:18 UTC (19:18 Brasília), read from the platform's deploy report: deploy steps P0 to P6 done on the VM, API ready in 4.3 s, V5 and V6 ok, 0 responses 503, anonymous pages 200, `/terms` 308 to `/policy#terms-signup`, `/download` 308 to `#downloads`, the Policy shows version 1.1, logs without errors; rollback possible through the tags `rollback-v1.5.1-7030a42` (no database change, no migration). Not proven: the full smoke test with the founder's account (sign-in, new acceptance of Terms and Policy 1.1, SA and NC download), the render of the screens at 320, 375, 768 and 1440 px against the served build, `tests/integration`. Every account accepts the Terms and the Policy 1.1 again at its next sign-in. `README.md` now says version 1.5.2 is in production; `docs/API.md`, `docs/COLLECTIONS.md` and `docs/FAQ.md` still follow the contract 1.5.1 read earlier the same day and were not read again. The entries below are records of their dates.

## [Unreleased] (2026-11-23, later): platform 1.5.1 confirmed in production

Documentation only. Production runs platform version 1.5.1 (commit `7030a42`, "Hot fixes v1.5.1"), confirmed on 2026-11-23: founder, "Versao 1.5.1 rodando na VM"; read-only reading of the VM by the coordinator (`VERSION` 1.5.1, containers `aurora-web` and `aurora-api` `:prod` up and healthy for 15 hours). This supersedes "which version answers in production was not confirmed" in the two entries below, which stay as the record. Version 1.5.2 stays prepared and not deployed. There is still no deploy report for 1.5.1 on disk. The README "Download and access" line now says so.

## [Unreleased] (2026-11-23): platform 1.5.2 prepared, not deployed

Documentation only. Platform version 1.5.2 is prepared and not deployed, with no commit (platform deploy package of 2026-11-23); which version answers in production was not confirmed. `README.md`, `docs/API.md`, `docs/COLLECTIONS.md` and `docs/FAQ.md` now say: the downloads move to the `#downloads` section of each collection page, with no Download page and a 308 on the old addresses; the NC package opens to an account that accepted the Terms and the Policy at sign-up, with no second acceptance, and withdrawal closes it; the combined bundle list drops the v1 duplicates; Terms 1.1 and Policy 1.1 are prepared, approved by counsel by the founder's declaration of 2026-11-23 (no document of counsel seen), and take effect when 1.5.2 is deployed. The contract on `docs/API.md` stays the one of 1.5.1.

## [Unreleased] (2026-11-23): platform version note

Documentation note only; nothing in the README body was changed. The README says platform 1.5.1 was deployed on 2026-11-23 and the Terms and Privacy Policy are final at version 1.0. The platform repository records v1.5.2 as prepared in its working tree and not deployed, with Terms 1.1 and Policy 1.1, and has no deploy report for 1.5.1 on disk. The README lines are to be reconciled when the deploy report exists. Source: `alchemia-ai/softwares/aurora-platform/docs/deploy/2026-11-23-pacote-de-deploy-v1-5-2.md`.

## [Unreleased] (2026-11-23): AURORA banner and the seven gates described

This entry changes presentation and documentation. It changes no figure, no data, no schema and no licence text. Nothing is published.

### Changed

- `assets/hero.svg`: the banner is now AURORA's, with the AURORA wordmark and symbol. It no longer carries the ATHANOR wordmark.
- `README.md`: new header with badges, the five collection symbols and a "How AURORA is made" section with the seven gates. ATHANOR now lives in the documentation.
- `docs/PIPELINE.md`: each gate, G1 to G7, is described sub-stage by sub-stage (S1.1 to S7.8), with what each one does and what it guarantees. Still no parameter, threshold or code.

- `assets/collection-*.svg`: replaced by the isometric figures of the platform v1.5.1, the ones its Home shows. The file names are the same.
- `README.md` (Download and access): states that platform 1.5.1 was deployed on 2026-11-23 and that sign-up is open by request, with approval by an administrator. It said sign-up was not open.
- Gate names in the README follow the platform: Collect sources, Standardize and identify, Set protonation, Build 3D conformers, Compute properties, Prepare for docking, Release and load.

### Added

- `assets/gates.svg`: the seven gates as cards. Generated by the brand system, like the other assets.
- `assets/step-collect.svg`, `step-curate.svg`, `step-release.svg`, `step-inspect.svg` and `platform.svg`: the four steps and the landing scene of the platform v1.5.1.
- `README.md`: sections "How it works" and "The platform".

### Contract 1.5.1 merged (same day, second pass)

- `docs/API.md` follows the platform contract 1.5.1 (read 2026-11-23, 116 operations on 106 paths): sign-up open by request, the two new open sign-in routes, bundles, capabilities, the one-compound package, the NC routes, API keys, the account and social routes, and the pipeline funnel. The substructure search is behind `SUBSTRUCTURE_SEARCH_ENABLED`; the similarity search no longer says it is off, because the contract names no switch for it.
- `docs/FAQ.md`, `docs/COLLECTIONS.md` and `README.md` (Download and access) drop "sign-up is not open" and the 1.4.0 references.
- Not read: the running instance. Which switches are on there is not known.

## [Unreleased] (2026-11-22): label of the one-compound download

This entry changes one phrase. It changes no figure, no data, no schema and no licence text. Nothing is published.

### Changed

- `README.md` (Download and access): the Explorer button for one compound is called "Download Data", as the
  platform audit of 2026-11-22 records (`docs/qc/2026-11-22-auditoria-conteudo-e-documents.md` of the platform
  repository); it said "Download package". Not checked in a running instance.

### Checked, not changed

- Links: `scripts/check_links.py`, 26 files, 0 broken. Figures: `scripts/gen_numbers.py --check`, in sync.
- The glance figures keep their reading date of 2026-11-18. A reading of the packages in object storage on
  2026-11-22 was given in the request for this audit and is not recorded in any file read here, so it is not
  printed.

## [Unreleased] (2026-11-20): packages, sources with their terms, download and access, citation

This entry changes wording and adds sections. It changes no data, no schema and no licence text. Nothing is
published.

### Changed

- `README.md`: the section "Planned package layout" is now "Packages". It says what the two packages are, that each
  collection has a set of six bundles (`sdf`, `pdbqt`, `descriptors`, `descriptors3d`, `admet`, `fingerprints`),
  which collections have an AURORA set and which have an AURORA-NC set (no NC set for Bioactivity Space, because
  AURORA-NC carries no bioactivity rows), what a one-compound `.zip` holds, and what the bundles do not carry.
  Source: the bundle manifest and the reports of 2026-11-19 in the AURORA data repository.
- `README.md` and `docs/SOURCES.md`: the sources of the platform's summary are listed with the package of each
  source, the terms as recorded and the reference, including the three non-commercial ones (TCMBank, Drug
  Repurposing Hub, AntibioticDB) and ChEMBL. BindingDB is described as bioactivity rows only, not a source of
  compounds. "License under review" per row is replaced by the terms the sources state; the sentence about the
  ShareAlike condition is unchanged.
- `README.md`: "Availability" is now "Download and access": how a file is fetched, the scopes `download` and
  `download_nc`, and the switch the one-compound download sits behind. No platform was read for this update.
- `README.md` and `docs/FAQ.md`: the status line and the answer to "Can I download the database?" say that the
  packages are staged in object storage and that no anonymous download is open.
- `README.md`: the citation names the author (Alchemia LTDA) and the publisher (Alchemia Solutions), with the
  BibTeX the platform shows. No DOI.
- `docs/API.md`: the file row says the one-compound package route is in the platform code of 2026-11-19 and not
  in the 1.4.0 contract the page follows.

- The figures of the glance table, `LICENSE`, `CITATION.cff` and the sentence about the ShareAlike status of some
  sources. The count of bundles and the counts per collection are not printed here.

## [Unreleased] (2026-11-18, claim gate): figures withdrawn, search routes and package layout corrected

This entry changes wording and the figures of the glance table. It changes no data, no schema and no licence
text. Nothing is published.

### Changed

- `README.md`, `data/numbers.json` and `scripts/gen_numbers.py`: the five figures of the glance table now carry
  the date 2026-11-18, the day the official reading was taken (1,000,000 complete, 983,687 in AURORA, 16,313 in
  AURORA-NC, 15,021 incomplete, 1,015,021 in both areas). They were unchanged by that reading.
- The status badge and the status line read "release 2.0.0 loaded, not published", instead of "release
  candidate 2.0.0 (unreleased)". "Loaded" is the state of the production database on 2026-11-18. The word
  "live" is not used: it waits for the founder.
- `README.md` and `docs/API.md`: the substructure and similarity search routes are marked as off in the beta,
  and the README no longer offers them as a way to use AURORA. The text search by identifier, name or synonym
  is the one offered.
- `README.md` and `docs/COLLECTIONS.md`: the five collections are called top-level, and the text says the
  registry also holds subcollections, so the platform's summary lists more rows than five.
- `README.md`: "What a release will carry" is now "Planned package layout", with no package published and no date
  promised, and no longer says one SDF and one PDBQT per compound. The product surface is described as planned.
- `README.md`: the sentence on the predecessor pipeline no longer says "most" of its files, a quantity this
  repository does not print.
- `examples/python/README.md`: a note that the two search calls above answer with an error while the routes are off.

### Removed

- The rows "learned-embeddings table" (1,000,000) and "names and synonyms" (9,339,498) from the glance table and
  from `data/numbers.json`. They were read on 2026-11-16 and are not in the official reading of 2026-11-18.

### Restored (2026-11-18, later the same day)

- The two rows withdrawn above are back in the glance table, in `data/numbers.json` and in
  `scripts/gen_numbers.py`, with a new reading: learned embeddings, 1,000,000 across both packages, and name rows,
  9,339,498 (rows, not distinct names), both read on 2026-11-18 in the production database (queries `7f3ed95` and
  `8641b26`; report `docs/qc/2026-11-18-releitura-embeddings-nomes.md` of the AURORA data repository). The
  reading shows the counts did not change since 2026-11-16; it does not show that the content is the same. The
  README block was regenerated by the script, not edited by hand.

## [Unreleased] (2026-11-18): licence wording by package, and the state of sign-up

This entry changes wording only: no figure, no data, no schema. Nothing is published.

### Changed

- The licence of each package is stated as it is on the platform's Licence page (version 1.0): AURORA under
  CC BY-SA 4.0 and AURORA-NC under CC BY-NC 4.0, each compound in exactly one package. The words "intended" and
  "planned" are gone from `README.md`, `docs/FAQ.md`, `docs/SCHEMA.md` and `scripts/gen_numbers.py` (badge and
  table labels). The sentence that the licences were provisional "until counsel's review is closed" is gone.
  What stays: each source keeps its own terms, and the licence status of some sources for the ShareAlike
  condition is not settled. No package is published yet.
- `README.md`, `docs/API.md`, `docs/FAQ.md`, `docs/COLLECTIONS.md`: sign-up "is off until the privacy policy is
  published" is replaced by the state as it is: the Terms of Use and the Privacy Policy are final (version 1.0);
  sign-up for the public is not open, opens as its own step after the next platform release is cut, and has no date.
- `LICENSE`: the attribution paragraph lists what a credit line carries (curator, package, sources, licence link,
  changes) and says to keep the licence with each compound.
- `data/site-links.json`: adds the platform addresses of the Policy and the License pages.

## [Unreleased, earlier today] (2026-11-18): identifier and version wording aligned to release candidate 2.0.0

Release 2.0.0 stays a candidate and is **not published**. This entry changes wording only: no figure, no
data, no schema and no licence text.

### Changed

- `docs/PIPELINE.md` and `docs/DATA_DICTIONARY.md`: the `ALC<n>` identifier is no longer described as
  permanent or never reassigned, because release 2.0.0 renumbered the identifiers once and keeps the
  old-to-new map. The G7 line says the loaded rows are reconciled with the files and the manifest.
- `CITATION.cff`: the version reads "release candidate 2.0.0, unpublished" instead of the 1.9.0 registry
  release. Still no DOI.
- The figures of `data/numbers.json` were compared with the official reading of 2026-11-18 and are unchanged:
  1,000,000 complete, 983,687 in AURORA, 16,313 in AURORA-NC, 15,021 incomplete.

## [Unreleased] (2026-11-17): documents brought to release candidate 2.0.0

Release 2.0.0 is a candidate and is **not published**: no tag, no release, no download package. The
platform is a closed beta for approved accounts. This entry changes documents and one script; it changes no
data, no schema and no licence text.

### Changed

- `README.md`, `data/numbers.json` and `scripts/gen_numbers.py`: the figures of release 1.9.0 (read on
  2026-10-17) are replaced by the readings of release 2.0.0.
  - Complete compounds of the release: 1,000,000 (read 2026-11-16).
  - Incomplete compounds, kept apart: 15,021 (read 2026-11-16). Both areas together: 1,015,021.
  - Package AURORA (CC BY-SA 4.0, intended): 983,687 (read 2026-11-17).
  - Package AURORA-NC (CC BY-NC 4.0, intended), in addition: 16,313 (read 2026-11-17).
  - 983,687 + 16,313 = 1,000,000. The release has 1,000,000 complete compounds, in two packages.
  - Two further rows of the glance table (the learned-embeddings table and the names and synonyms table) were added
    here and withdrawn on 2026-11-18, see the entry of that date.
- The generator now reads each figure with its own date and fails with exit 2 when a field is missing.
- The badges show the status "release candidate 2.0.0 (unreleased)" and the count of complete compounds of
  the release, not of a package. The licence badge says the licences are the planned ones.
- `docs/SCHEMA.md` and `docs/DATA_DICTIONARY.md` describe the data model of 2.0.0: bioactivity, targets and
  assays, ontology, collections, tables by group and the public views.
- `docs/API.md` and `examples/` follow the OpenAPI contract of platform version 1.4.0 of the closed beta: one
  route of aggregates, the health probes and the sign-in doors need no token; every other route needs a
  Bearer token.
- `docs/COLLECTIONS.md`, `docs/FAQ.md`, `docs/SOURCES.md`, `CONTRIBUTING.md`, `SECURITY.md` and the folder
  READMEs: dated state, no claim of an open page, no promise of a download.

### Removed

- The "Sources" badge and the figures "public sources", "raw source records read" and "bioactivity
  measurements" of release 1.9.0. The public list of sources of 2.0.0 is not decided, the raw-record count is
  not measured for 2.0.0, and bioactivity counts are not published here.
- The sentence that bioactivity coverage is thin and that AURORA is not a bioactivity database. Release 2.0.0
  holds bioactivity measurements about the compounds it holds, each row with its own licence.
- The statement that the v1.3 release of the platform has been live since 2026-10-26, and the list of pages
  open to read.
- From `docs/SOURCES.md`, the section "Other public collections AURORA draws on" and the citation sentence
  of one of its entries. The page now says that the AURORA-NC package groups the compounds whose source
  licence does not allow commercial use, and names no source for it.

### Not changed, on purpose

- `LICENSE`, `LICENSE-CODE` and the text of any licence.
- The six sources of the main table in `docs/SOURCES.md`: no name added; the public list is not decided.

## [Unreleased] (2026-10-26): first version of the repository

Documentation of the ATHANOR pipeline and the AURORA data model, the source list, read-only API examples,
the figures generated by `scripts/gen_numbers.py` and the link checker `scripts/check_links.py`. Figures of
release 1.9.0, read on 2026-10-17.
