# The ATHANOR pipeline, as described in public

ATHANOR is the curation pipeline that turns public compound collections into the AURORA database. It is
private. This page says what each stage is for, at the level of a headline. It gives no parameter, no
threshold and no code, and it will not.

## The seven stages

| Stage | Purpose |
|---|---|
| **S1** Source acquisition and provenance | Bring each source in under a declared licence gate. Every record keeps its own redistribution verdict, so the licence is a mark on the data and never a silent filter |
| **S2** Structure curation and identity | Validate and standardize each structure, merge duplicates across sources, and give each unique compound a permanent `ALC<n>` identifier that is never reassigned or reused |
| **S3** Ligand state preparation | Set the protonation state at physiological pH and apply a stereochemistry policy |
| **S4** 3D structure generation and validation | Produce one force-field-optimized 3D conformer per compound and check it with a validity gate |
| **S5** Molecular characterization | Compute descriptors, fingerprints, structural alerts, ADMET predictions with an applicability domain, scaffolds and a learned embedding |
| **S6** Docking-ready preparation | Convert the 3D structure into a docking file and check the file |
| **S7** Release assembly, loading and reconciliation | Package the release with a checksum manifest, load the database and reconcile files against it |

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
