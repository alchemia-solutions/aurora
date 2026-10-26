# The ATHANOR pipeline, as described in public

[Repository home](../README.md) · [Docs index](README.md)

ATHANOR is the curation pipeline that turns public compound collections into the AURORA database. It is
private. This page says what each stage is for, at the level of a headline. It gives no parameter, no
threshold and no code, and it will not.

## The seven stages

| Stage | What it does | What it gives |
|---|---|---|
| **S1** Collect sources | Each record is collected with its source and license. Every record keeps its own redistribution verdict, so the license is a mark on the data and never a silent filter | A record that carries where it came from |
| **S2** Standardize and identify | Validates and standardizes each structure, merges duplicates across sources and gives each unique compound a permanent identifier | A stable `ALC<n>` identifier, never reassigned or reused |
| **S3** Set protonation | Each molecule is prepared in the forms used for modeling, at physiological pH, under a stereochemistry policy | The prepared forms of the molecule |
| **S4** Build 3D conformers | A 3D geometry is generated and checked by a validity gate | An approved geometry, or a mark that none was approved |
| **S5** Compute properties | Each molecule is described by its properties: descriptors, fingerprints, structural alerts, ADMET predictions with an applicability domain, scaffolds and a learned embedding | The descriptors and properties of the compound |
| **S6** Prepare for docking | Files are prepared for docking and checked | Files that a docking program can read |
| **S7** Release and load | The release is assembled with a checksum manifest, loaded and checked against the record | A release that matches its record |

## Principles

1. Completeness is not correctness. Every stage has a chemical correctness gate, not only a count.
2. A stage is done only after its artifact is read back and its real row count matches.
3. One identifier and one append-only record, from the first molecule.

## What the pipeline is honest about

- A compound whose checks do not pass stays in the incomplete area until it is reviewed.
- Compounds without approved 3D geometry are kept in a separate area with their full chemical identity.
  Hiding them would have been easier and wrong.
- Stereoisomers are not enumerated. Undefined stereo stays undefined and is flagged.
- A subset of compounds has no computed protonation variant. The column is nullable and means what it says.
- "Docking-ready" is a statement about files that passed the checks. It does not claim that protonation and
  tautomer states are validated for any target.

## Where ATHANOR sits in the Great Work

Alchemia names its phases after the stages of the alchemical Great Work. The whole of ATHANOR is the
Albedo, the purification, and AURORA is the Citrinitas, the yellowing that comes out of it. The stages
themselves carry no alchemical phase.
