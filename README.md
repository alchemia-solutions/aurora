<div align="center">

<img src="assets/hero.svg" alt="ATHANOR and AURORA, by Alchemia Solutions" width="100%">

<br>

<!-- numbers:begin badges -->
[![Data licence: CC BY-SA 4.0 and CC BY-NC 4.0](https://img.shields.io/badge/Data_licence-CC_BY--SA_4.0_%2B_CC_BY--NC_4.0-FF9E00?style=for-the-badge&labelColor=000000)](LICENSE)
[![Registry: 1.9.0 (unreleased)](https://img.shields.io/badge/Registry-1.9.0_(unreleased)-FF9E00?style=for-the-badge&labelColor=000000)](CITATION.cff)
[![Compounds: 935,338](https://img.shields.io/badge/Compounds-935%2C338-FF9E00?style=for-the-badge&labelColor=000000)](#at-a-glance)
[![Sources: 9](https://img.shields.io/badge/Sources-9-808080?style=for-the-badge&labelColor=000000)](docs/SOURCES.md)
<!-- numbers:end badges -->

**ATHANOR curates the data. AURORA is the database it produces.**

[![Home (public)](https://img.shields.io/badge/Home_(public)-aurora.alchemia.solutions-FF9E00?style=for-the-badge&labelColor=000000)](https://aurora.alchemia.solutions/home)
[![Collections (beta)](https://img.shields.io/badge/Collections_(beta)-808080?style=for-the-badge&labelColor=000000)](https://aurora.alchemia.solutions/collections)
[![Explorer (beta)](https://img.shields.io/badge/Explorer_(beta)-808080?style=for-the-badge&labelColor=000000)](https://aurora.alchemia.solutions/explorer)
[![Documents (beta)](https://img.shields.io/badge/Documents_(beta)-808080?style=for-the-badge&labelColor=000000)](https://aurora.alchemia.solutions/docs)
[![API notes](https://img.shields.io/badge/API_notes-docs%2FAPI.md-808080?style=for-the-badge&labelColor=000000)](docs/API.md)

The platform is in closed beta. Only the Home is public. Collections, Explorer and Documents ask for an
invitation token.

[What it is](#what-it-is) · [The pipeline](#the-athanor-pipeline) · [At a glance](#at-a-glance) · [Collections](#the-five-collections) · [Sources](docs/SOURCES.md) · [Read the API](#read-aurora-through-the-api) · [Limits](#honest-limitations) · [Cite](#citing) · [Contribute](#contributing)

</div>

---

## What it is

**AURORA** (Alchemia Unified Repository for Open Research Applications) is a molecular database for
computer-aided drug design, built and maintained by [Alchemia Solutions](https://alchemia.solutions)
(legal entity Alchemia LTDA, Barretos, São Paulo, Brazil). Its main package is licensed under CC BY-SA 4.0
and a companion package, AURORA-NC, under CC BY-NC 4.0. No package is published yet.

This repository describes the database: a standardized structure with a permanent identifier, a
protonation state at physiological pH, a 3D conformer, a docking file, computed descriptors,
fingerprints, ADMET predictions and the provenance of each compound.

**ATHANOR** is the curation pipeline that produces it. It is private. The data is released under
Creative Commons licences, the furnace is not, and this repository says so plainly: it holds the
description of the database, the list of its sources, the data model and examples that read the API. It
holds no pipeline code, no configuration and no per-compound data.

AURORA does not compete on scale. Every complete compound has an approved 3D
conformer, a docking file and the core feature tables. Some exhaustive descriptors are missing on some
compounds, and some compounds have no computed protonation variant. The collection leans toward natural
products and Brazilian biodiversity.

<table>
<tr><td width="50%" valign="top">

**A good fit if you want to**

- study natural-product chemical space with consistent descriptors
- search by substructure or similarity through the API, during the closed beta and with a token
- prepare ligands from complete compounds, once a package is released (docking-ready is not target-ready)

</td><td width="50%" valign="top">

**Not a fit if you want**

- billions of make-on-demand compounds
- bioactivity at the depth of [ChEMBL](https://www.ebi.ac.uk/chembl/)
- the curation source code

</td></tr>
</table>

## The ATHANOR pipeline

An athanor is the alchemist's slow furnace, built to hold a constant heat for months. The pipeline has
seven macro-stages, each with a quality gate rather than a bare count.

<div align="center">
<img src="assets/flow.svg" alt="The ATHANOR pipeline in seven stages, S1 to S7, from source acquisition to release reconciliation" width="100%">
</div>

| Stage | What it does |
|---|---|
| **S1** Source acquisition and provenance | Every source passes a licence gate and every record keeps its own redistribution verdict |
| **S2** Structure curation and identity | Validates and standardizes each structure and gives it a permanent `ALC<n>` identifier |
| **S3** Ligand state preparation | Sets the protonation state at physiological pH and applies a stereochemistry policy |
| **S4** 3D structure generation and validation | One force-field-optimized conformer per compound, checked by a validity gate |
| **S5** Molecular characterization | Descriptors, fingerprints, structural alerts, ADMET predictions, scaffolds and a learned embedding |
| **S6** Docking-ready preparation | Converts the 3D structure to a docking file and checks it |
| **S7** Release assembly, loading and reconciliation | Packages with a checksum manifest and reconciles the files against the database |

More in [docs/PIPELINE.md](docs/PIPELINE.md). The pipeline exists because its predecessor reported
near-total coverage while most of its files carried wrong stereochemistry. The lesson is the rule of the
project: no coverage metric detects a correctness error.

## At a glance

<!-- numbers:begin glance -->
| | |
|---|---:|
| Compounds in the registry (both areas) | 935,338 |
| Complete: approved 3D geometry, SDF and PDBQT | 919,819 |
| Incomplete: full identity, no approved 3D geometry | 15,519 |
| In the AURORA package (CC BY-SA 4.0) | 903,515 |
| In the AURORA-NC package (CC BY-NC 4.0) | 16,304 |
| Public sources | 9 |
| Raw source records read | 1,136,429 |
| Names and synonyms | 8,546,241 |
| Learned embeddings (768 dimensions) | 926,622 |
| Bioactivity measurements | 1,250 |

*Population: the AURORA registry, release 1.9.0, unpublished. Read on 2026-10-17. Source: Alchemia registry, release 1.9.0, local database, read by query on that date; the database behind the platform was not read again. Complete and incomplete add up to the registry; a compound is in exactly one package.*
<!-- numbers:end glance -->

The complete set is what the platform and the download packages are meant to serve. The incomplete area is
kept, marked, and never mixed into them. Every figure above is copied from `data/numbers.json` with its
date by `scripts/gen_numbers.py`; none is typed by hand.

## The five collections

AURORA, Natural Space, Drug Space, Bioactivity Space and Diversity Space. See
[docs/COLLECTIONS.md](docs/COLLECTIONS.md).

## What a release will carry

Structure packages (one SDF and one PDBQT per compound), feature tables in Parquet, a manifest with a
SHA-256 for every file, the SQL schema and the citation files. SDF is the canonical format and PDBQT is
derived from it. Detail in [docs/SCHEMA.md](docs/SCHEMA.md) and
[docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md). No release package is published yet (see
[Availability](#availability)).

## Sources

AURORA draws on public collections. The list, with references, is in [docs/SOURCES.md](docs/SOURCES.md).
Attribution names Alchemia LTDA and the original sources: the curation does not replace them, and if you
publish work built on a subset, cite the upstream projects too.

## Read AURORA through the API

The platform exposes a versioned REST API at `https://aurora.alchemia.solutions/v1/`. During the closed
beta it needs an invitation token. Examples that only read are in [`examples/`](examples/) (Python and
curl), and [docs/API.md](docs/API.md) says what they call. Nobody gets direct database access, not even
read-only: the product is meant to be file download plus the API.

## Availability

- **The platform** is in **closed beta**, for approved testers. Only the Home is public.
- **The API** answers in the same beta. Without a token, `/v1/` answers 401.
- **Download packages** are not published. The object storage that will serve them holds no public
  package yet.
- **This repository** describes the database. It is not the database.

## Honest limitations

- Scale is not the selling point. The registry is small next to the billion-compound libraries.
- Bioactivity coverage is thin, and AURORA is a structure and property database, not a bioactivity one.
- ADMET values are predictions, never measurements. Treat them as triage.
- Stereoisomers are not enumerated. A compound whose source left stereo undefined keeps it undefined, and
  is flagged.
- Some compounds have no approved 3D geometry. They live in a separate, marked area and are not mixed
  into the packages or the API.
- Each source has its own terms, and some allow only non-commercial use. That is why a second package,
  AURORA-NC, exists. The licence status of some sources is under review (see docs/SOURCES.md). Read the
  terms at the source before you build on a subset.
- No DOI is minted for the dataset yet.
- "Docking-ready" means the files passed the checks of the pipeline. It does not mean that protonation and
  tautomer states are validated for every target.

## Licence

| What | Licence | File |
|---|---|---|
| Main package, documentation, figures | CC BY-SA 4.0 | [LICENSE](LICENSE) |
| AURORA-NC package | CC BY-NC 4.0 | [LICENSE](LICENSE) |
| Code in `examples/` and `scripts/` | Apache-2.0 | [LICENSE-CODE](LICENSE-CODE) |

No package is published yet. The ATHANOR pipeline is not in this repository and no licence here grants any
right in it. The Alchemia, ATHANOR and AURORA names and symbols are trademarks of Alchemia LTDA (see
[LICENSE](LICENSE)).

## Citing

Cite the database and the upstream sources you used. A machine-readable form is in
[`CITATION.cff`](CITATION.cff). Cite it as registry release 1.9.0, unpublished: there is no package and no
DOI yet.

## Contributing

Issues and pull requests are welcome, within what this repository holds: documentation, examples,
corrections to the source list and questions. See [CONTRIBUTING.md](CONTRIBUTING.md), the
[Code of Conduct](CODE_OF_CONDUCT.md) and [SECURITY.md](SECURITY.md). Questions and proposals for
partnerships: contact@alchemia.solutions. The organization is at
[github.com/alchemia-solutions](https://github.com/alchemia-solutions).

## Layout

```
README.md  LICENSE  LICENSE-CODE  CITATION.cff
CONTRIBUTING.md  CODE_OF_CONDUCT.md  SECURITY.md
assets/      figures and symbols from the brand system (placed, never redrawn)
data/        numbers.json, the only place the figures of this repository live
docs/        SOURCES, PIPELINE, SCHEMA, DATA_DICTIONARY, COLLECTIONS, API, FAQ
examples/    read-only calls to the API (Python, curl)
scripts/     gen_numbers.py, which writes the figures into the documents
.github/     issue and pull request templates
```
