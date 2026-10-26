# Data dictionary (public columns)

[Repository home](../README.md) · [Docs index](README.md)

This page documents the columns a consumer is most likely to meet. It is a selection, not the whole
schema. The complete dictionary, generated from a live query against the database, ships with each
release. Where a column is not listed here, do not assume what it means.

## `compounds`

| Column | Meaning |
|---|---|
| `alchemia_id` | The public identifier, `ALC<n>`. Append-only: never reassigned or reused |
| `alchemia_seq` | The number inside `alchemia_id` |
| `inchi`, `inchikey` | Standard InChI of the curated structure, and its InChIKey. The InChIKey is deliberately not unique: two different InChIs can share a key |
| `canonical_smiles` | Isomeric canonical SMILES. Undefined stereo stays undefined |
| `mol` | The RDKit cartridge molecule built from the SMILES |
| `formula` | Molecular formula |
| `heavy_atom_count`, `formal_charge` | Count of non-hydrogen atoms, and net formal charge |
| `stereo_undefined_in_source` | True when the curated structure leaves a tetrahedral centre or a double bond without defined stereo. The 3D file then realizes one configuration |
| `partial_reason` | Empty for a complete compound. Filled in the incomplete area, with the reason there is no approved 3D geometry |
| `license_tier` | Which package the compound belongs to: `cc_by_sa` for AURORA (CC BY-SA 4.0), `cc_by_nc` for AURORA-NC (CC BY-NC 4.0) |
| `is_redistributable` | True when at least one source link of the compound may be redistributed |

## `descriptors`

| Column | Meaning |
|---|---|
| `molecular_weight`, `logp`, `tpsa`, `num_h_donors`, `num_h_acceptors`, `qed` | One-dimensional and two-dimensional descriptors of common use |
| `values_2d` | Exhaustive 2D descriptors, as a JSON object. A descriptor can be absent for a molecule that lacks the environment it measures, so not every key is on every compound |
| `values_3d` | Eleven 3D shape descriptors, as a JSON object |

## `fingerprints`

| Column | Meaning |
|---|---|
| `morgan` | Morgan, radius 2, 2048 bits |
| `morgan_ulvs` | Morgan, radius 2, 1024 bits |
| `maccs` | MACCS keys |
| `atompair_bv`, `torsion_bv` | Atom-Pair and Topological-Torsion, 2048 bits |
| `e3fp` | E3FP, a 3D fingerprint |

Generate a query fingerprint the same way as the column you compare it with.

## `structure_files` and `compound_structures_3d`

| Column | Meaning |
|---|---|
| `file_format` | `sdf` or `pdbqt`. SDF is canonical and PDBQT is derived from it. If they disagree, the SDF is right |
| `sha256` | Checksum of the file, verified at load |
| `sdf_molblock`, `pdbqt_text` | The geometry of a complete compound, each checked against its checksum |

## `sources`

| Column | Meaning |
|---|---|
| `source_key`, `display_name` | Stable key and the name shown |
| `license_declared` | The terms of the source as recorded |
| `license_tier` | The package a link to this source belongs to |

## Predictions are not measurements

ADMET values in `compound_scores` are model predictions, each with an applicability domain. Use them for
triage. They are not evidence.
