# The ATHANOR pipeline, as described in public

[Repository home](../README.md) · [Docs index](README.md)

ATHANOR is the curation pipeline that turns public compound collections into the AURORA database. It is
private. This page says what each stage is for, at the level of a headline. It gives no parameter, no
threshold and no code, and it will not.

## The seven stages

| Stage | What it does | What it gives |
|---|---|---|
| **G1** Collect sources | Each record is collected with its source and license. Every record keeps its own redistribution verdict, so the license is a mark on the data and never a silent filter | A record that carries where it came from |
| **G2** Standardize and identify | Validates and standardizes each structure, merges duplicates across sources and gives each compound an ALC identifier | An `ALC<n>` identifier. Release 2.0.0 renumbered them once, and the old-to-new map is kept (see [SCHEMA.md](SCHEMA.md#identifiers)) |
| **G3** Set protonation | Each molecule is protonated at physiological pH, under a stereochemistry policy | The protonation state of the molecule at physiological pH |
| **G4** Build 3D conformers | A 3D conformer is embedded, minimized and then validated by a validity gate | An approved 3D conformer, or a mark that none was approved |
| **G5** Compute properties | Physicochemical descriptors, fingerprints, structural alerts and predicted ADMET are computed for each molecule, with an applicability domain, scaffolds and a learned embedding | Computed descriptors, fingerprints, alerts and ADMET predictions, never laboratory measurements |
| **G6** Prepare for docking | A PDBQT file is prepared for docking and checked against readiness rules | A PDBQT file that passes the readiness checks |
| **G7** Release and load | The release is assembled with a checksum manifest, loaded and reconciled with the registry and with the files and the manifest | A release whose loaded rows match its manifest |

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
- A file prepared for docking is a statement about a file that passed the checks. It does not claim that protonation and
  tautomer states are validated for any target.

## Where ATHANOR sits in the Great Work

Alchemia names its phases after the stages of the alchemical Great Work. The whole of ATHANOR is the
Albedo, the purification, and AURORA is the Citrinitas, the yellowing that comes out of it. The stages
themselves carry no alchemical phase.
