# Using the data

[Repository home](../README.md) · [Docs index](README.md)

For people who will work with AURORA compounds: how to reach them, what the files hold, how to check them,
and what each licence asks of you. To get an account and an API key first, read [QUICKSTART.md](QUICKSTART.md).
What production offered on 2026-11-25 is the table at the end of the quickstart; this page does not repeat it.

## Two ways in

| You want | Use | Credential |
|---|---|---|
| To search, read records, filter a list, fetch one 3D structure at a time | The API, `/v1/...` ([API.md](API.md)) | An API key (`aurk_...`), read only |
| Whole collections as files, or the full set of files of one compound | The bundles and the one-compound package, on the platform | The signed-in session of the platform |
| Bioactivity rows of a compound | The compound page, `/activities` (session or API key) or `/bioactivity` (session) | An approved account |

An API key never receives a file: on bundles, packages, the `/bioactivity` view and the account it answers
`403 api_key_not_allowed`. Nobody gets direct database access.

## Licence, compound by compound

Every compound belongs to exactly one package, and the package decides its licence:

| Package | Licence | SPDX id in the API |
|---|---|---|
| AURORA | CC BY-SA 4.0 | `CC-BY-SA-4.0` |
| AURORA-NC | CC BY-NC 4.0, non-commercial use only | `CC-BY-NC-4.0` |

- Every compound answer of the API carries a `license` object (`package`, `label`, `spdx`, `url`,
  `noncommercial`). Keep it with the compound in whatever you build: the example scripts write it to a
  `license.tsv` next to the data.
- A set you assemble can hold compounds of both packages. The AURORA-NC rows in it stay non-commercial.
  If you need a set for commercial use, keep only rows whose `noncommercial` is `false`.
- Every bundle carries `license_per_row.tsv`, the licence and the attribution of each compound, and the
  one-compound package carries the same as `license.tsv`.
- Attribution names Alchemia LTDA for the curation and aggregation. It does not replace the original
  sources: when you publish work built on a subset, cite the upstream projects too. Their names, terms and
  the sentence each one asks for are in [SOURCES.md](SOURCES.md), and `GET /v1/sources/attribution` returns
  the attribution text of every source.
- How to cite AURORA itself: [Citing](../README.md#citing).

This page explains how the licences are carried in the data. It is not legal advice: read the licence texts
linked above and the terms of each source before you build on a subset.

## The bundles of a collection

Signed in, open a collection page and go to its **Downloads** section (`#downloads`). It lists the bundles of
that collection for each package. Each bundle is one `.tar.zst` archive of one type
([README, Packages](../README.md#packages)):

| Type | What is inside |
|---|---|
| `sdf` | one `ALC<n>.sdf` per compound, the canonical 3D structure |
| `pdbqt` | one `ALC<n>.pdbqt` per compound, derived from the SDF for docking |
| `descriptors` | 2D physicochemical properties, one row per compound |
| `descriptors3d` | 3D shape descriptors, one row per compound |
| `admet` | ADMET-AI predictions, one row per compound, with a column that says how many are missing |
| `fingerprints` | Morgan (2048 and 1024 bits), MACCS, atom-pair, torsion and E3FP, in Parquet |

Every bundle also holds `README.md`, `LICENSE`, `ATTRIBUTION.md`, `license_per_row.tsv` and `SHA256SUMS`.
There is no AURORA-NC bundle for Bioactivity Space, because AURORA-NC carries no bioactivity rows.

The platform describes each bundle with these fields (from `GET /v1/bundles`, session only):

| Field | Meaning |
|---|---|
| `id`, `name` | The bundle. The downloaded file is named `<id>.tar.zst` |
| `collection`, `package`, `kind`, `format` | Which collection, which package (`by-sa` or `nc`), which type, which file format |
| `compounds`, `bytes` | How many compounds and how many bytes; `null` when not measured |
| `license` | `spdx`, `label`, `url`, `noncommercial`, `scope` and `per_row_file` (`license_per_row.tsv`, inside the archive) |
| `attribution` | The sources to credit for this bundle |
| `availability`, `legal_review` | `available` only when the file was verified and its legal review approved; otherwise `not_published`, with no link |
| `can_download` | Whether your account may download it: an AURORA-NC bundle needs an account that holds the NC access |

A download is a short-lived signed link, returned with the `sha256` and `bytes` of the archive. Fetch it at once; an expired link answers an error, and you ask the
page for a new one.

### Check and open a bundle

```bash
# 1. The archive: compare with the sha256 returned with its signed link
sha256sum natural-space-descriptors.tar.zst

# 2. Unpack (GNU tar 1.31 or later; otherwise: zstd -dc FILE | tar -xf -)
mkdir natural-space-descriptors && tar --zstd -xf natural-space-descriptors.tar.zst -C natural-space-descriptors

# 3. Every file inside against SHA256SUMS
cd natural-space-descriptors && sha256sum -c SHA256SUMS
```

The bundle name above is an example; use the name of the file you downloaded.

### Read the tables

```python
import pandas as pd

admet = pd.read_csv("admet.tsv", sep="\t")             # columns admet_<task>, one row per compound
licence = pd.read_csv("license_per_row.tsv", sep="\t")  # the licence and attribution of each compound
fps = pd.read_parquet("fingerprints.parquet")           # needs pyarrow
```

The file names inside an archive are listed in its `README.md`. Join tables on `alchemia_id`. The columns of
every table are described in [DATA_DICTIONARY.md](DATA_DICTIONARY.md): the ADMET columns are the group
"ADMET (predictions)", named `admet_<task>` (for example `admet_hERG`).

### What the bundles do not carry

No identity tables (canonical SMILES, InChIKey, names, cross-references), classification, scaffolds,
protonation microstates, drug annotations, embeddings, or a per-source link table beyond
`license_per_row.tsv`. Several of these are in the compound record of the API (`GET /v1/compounds/{id}`):
identity, names, scaffold, classification and sources.

## The package of one compound

For one molecule, the Explorer has a **Download Data** button, and `GET /v1/compounds/{alchemia_id}/package`
returns a signed link to the `.zip` with the session. `ALC<n>.zip` holds `sdf/`, `pdbqt/`,
`descriptors.tsv`, `descriptors3d.tsv`, `admet.tsv`, `fingerprints.tsv`, `license.tsv`, `ATTRIBUTION.md`,
`LICENSE` and `README.md`, and `activities.tsv` only for an AURORA compound that has bioactivity rows the
licence lets us serve.

## Working through the API

The API is the way to work on a list of compounds without downloading whole collections:

- **Filter on the server.** `GET /v1/compounds` and `GET /v1/collections/{slug}/compounds` take bounds on
  molecular weight, logP, TPSA, QED, SA score, donors, acceptors, rotatable bonds and rings, plus the
  Lipinski, Veber, rule-of-three and structural alert flags, and `has_sdf` or `has_pdbqt`. Walk the result with
  the cursor ([QUICKSTART.md](QUICKSTART.md#4-walk-a-listing)).
- **Read many records at once.** `GET /v1/compounds/batch?ids=ALC1,ALC2` returns up to 50 summaries per call,
  and lists in `not_found` the ids your account is not served.
- **Predicted ADMET of one compound** is in `admet_profile` of `GET /v1/compounds/{id}/features`, keyed by
  the ADMET-AI task name.
- **3D structure.** `GET /v1/compounds/{id}/structure.sdf` returns the SDF as stored. Its `ETag` is the
  SHA-256 of the body: compare them to know the file arrived whole. The PDBQT is in the files only.
- **Stay within the limit.** 60 requests per 60 seconds, shared by every key of the account. On 429 wait the
  seconds of `Retry-After`. For a large selection, a bundle is cheaper than thousands of calls.

Recipes, in [`examples/python/`](../examples/python/):

| Script | What it does |
|---|---|
| `aurora_client.py` | A small client: token from `AURORA_TOKEN`, cursors, retry on 429 after `Retry-After`, errors with `request_id` |
| `filter_compounds.py` | Filters a list of compounds by properties, then by predicted ADMET values |
| `docking_set.py` | Builds a docking ligand set from a list: one SDF per compound, one multi-record SDF, `license.tsv` |

## Before you use the values

- **ADMET values are predictions**, from ADMET-AI, never measurements. Use them for triage. Classifiers give a
  probability between 0 and 1, regressors a value in the units of their training set.
- **A file prepared for docking is not target-ready.** It passed the checks of the pipeline; protonation and
  tautomer states are not validated for your target.
- **Stereoisomers are not enumerated.** A compound whose source left stereo undefined keeps it undefined, and
  is flagged.
- **Bioactivity rows** are about the compounds AURORA holds, each with its own licence, and only the rows the
  licence lets us serve are served. AURORA does not replace ChEMBL as a bioactivity reference.

More in [Honest limitations](../README.md#honest-limitations) and [FAQ.md](FAQ.md).

## What is not here

No figures of the corpus (they live in `data/numbers.json` and the root README), no download links, no token
and no pipeline detail. The bundles and the package are described as the platform and the packages manifest
describe them; the platform decides what your account can download.
