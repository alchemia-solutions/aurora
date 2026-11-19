# AURORA variable dictionary

Generated on 2026-11-18 from `docs/qc/2026-11-18-dicionario-de-variaveis.json` by `scripts/gen_data_dictionary_variables.py`. Release 2.0.0, status: not released. Do not edit by hand: change the generator and run it again.

Every variable we hold for a compound, in the bundle files and in the database, has one entry here. The bundles are still a candidate manifest, not a published download. The same text is kept in the AURORA repository and in the public repository.

## How to read an entry

- **Served**: the API is built to return the field today (API role can read it and the platform returns it). `no` means the field is in the database and not served in this release.
- **In the files**: the field is in a file of the bundles (SDF, PDBQT, fingerprint Parquet, descriptors, descriptors3d and ADMET TSV). The bundles are a candidate manifest; this mark does not say a file can be downloaded today.
- **In aurora_prod**: the field exists in the production schema, from the schema and migrations. Not rechecked on the VM today.
- **Package**: AURORA is CC BY-SA 4.0. AURORA-NC is CC BY-NC 4.0 and adds compounds; it carries the same fields. No NC value, id or per-collection count is published here.
- **Population**: the AURORA package has 983,687 compounds and the NC package adds 16,313 (source: `docs/qc/2026-11-18-numeros-para-stats.json`). A field that exists for every compound can still be empty for some of them; the NULL line says when.
- **Predictions** (ADMET, applicability, natural-product likeness, learned embeddings, drug-likeness flags) are computed estimates, never measurements of the compound.

## Summary

| Group | Variables |
|---|---|
| Identity and names | 38 |
| 2D and 3D structure, geometry gates | 40 |
| Physico-chemical descriptors | 1461 |
| Drug-likeness and structural alerts | 23 |
| ADMET (predictions) | 150 |
| Fingerprints | 7 |
| Embeddings and MinHash | 9 |
| Docking preparation (PDBQT) | 11 |
| Scaffolds, classification, organisms | 57 |
| Activities | 46 |
| Drug annotations (ChEMBL and sources) | 75 |
| Sources, provenance and licence | 13 |
| Collections and membership | 4 |
| Quality flags | 34 |
| Version and identifier history | 13 |
| **All groups** | **1981** |

Variables marked not served in this release: 187.

## Drug-likeness rules in plain words

Lipinski violations, the Veber pass, the three structural-alert flags (PAINS, Brenk, NIH) and the combined alert list are served as marks on every compound. The further rules of the rule catalogue (the question names Egan, Ghose and Muegge) are stored as one row per compound and rule, and the rule catalogue marks a rule as publishable only when its cutoffs were confirmed against a source. When the aggregate was measured on 2026-11-18 none of those rules was publishable, so the rule-flag view returned no row. `publishable = false` therefore means: the rule is not shown to users yet. It says nothing about the compound. See OQ4.

## Identity and names

### `inchi` (V0001)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Standard InChI of the curated structure.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated by the ATHANOR pipeline (compound_identity_v1); the SDF only confirms it. Stereo left undefined in the source stays undefined here.
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `inchikey` (V0002)

- Relation: `public.compounds`. Type: char(27) or char(64). Unit: none stated.
- What it is: InChIKey of the curated InChI, 27 characters.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Computed from the curated InChI. Two different InChIs can share a key, so the key is not unique in the table.
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `alchemia_id` (V0003)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Public compound identifier, ALC followed by the sequence number.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Generated column: the text ALC joined to alchemia_seq. The sequence comes from an append-only InChI to sequence registry, never recomputed by order.
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: ALC8.
- Files: admet_tsv, descriptors_tsv, descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `mol` (V0004)

- Relation: `public.compounds`. Type: mol. Unit: none stated.
- What it is: RDKit cartridge molecule built from canonical_smiles, for substructure search.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: mol_from_smiles over canonical_smiles at load. Not a file format: it is the in-database object behind substructure search.
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `canonical_smiles` (V0005)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Isomeric canonical SMILES of the curated structure.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated by the pipeline; the cartridge mol column is built from it. Undefined stereo stays undefined, unlike the 3D SDF.
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `formula` (V0006)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Molecular formula.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Derived from the curated structure.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `inchi_sha256` (V0017)

- Relation: `public.compounds`. Type: bytea. Unit: none stated.
- What it is: a direct UNIQUE on inchi itself overflows PostgreSQL's ~2704-byte B-tree entry limit for a real macrocycle InChI.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `name` (V0033)

- Relation: `public.compound_names`. Type: text. Unit: none stated.
- What it is: The name as the source gives it.
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `name_type` (V0034)

- Relation: `public.compound_names`. Type: text. Unit: none stated.
- What it is: common | iupac | trade | synonym | code.
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: Closed list: common, iupac, trade, synonym, code.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `name_type_rule` (V0035)

- Relation: `public.compound_names`. Type: text. Unit: none stated.
- What it is: How name_type was assigned: field (the source field says it) | pattern:code | pattern:cas.
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: Closed list: code, pattern.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_key` (V0036)

- Relation: `public.compound_names`. Type: text. Unit: none stated.
- What it is: Source of the name (sources.source_key).
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_field` (V0037)

- Relation: `public.compound_names`. Type: text. Unit: none stated.
- What it is: Field of the source record the name was read from.
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `rank` (V0038)

- Relation: `public.compound_names`. Type: integer. Unit: none stated.
- What it is: Order of the name among the compound's names (1 = first).
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_preferred` (V0039)

- Relation: `public.compound_names`. Type: boolean. Unit: none stated.
- What it is: The name ATHANOR prefers to show for the compound.
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `names_version` (V0041)

- Relation: `public.compound_names`. Type: text. Unit: none stated.
- What it is: Version of the S2.8 stage.
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `xref_db` (V0042)

- Relation: `public.compound_xrefs`. Type: text. Unit: none stated.
- What it is: Name of the external database this identifier belongs to (e.g. 'chembl', 'pubchem_cid', 'zinc', 'drugbank', 'npatlas', per the inline DDL comment). Part of the composite
- Origin: Identifiers read from the source records.
- How: Identifiers read from the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `xref_id` (V0043)

- Relation: `public.compound_xrefs`. Type: text. Unit: none stated.
- What it is: Identifier value in the external database. Part of the composite
- Origin: Identifiers read from the source records.
- How: Identifiers read from the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `xref_db` (V0044)

- Relation: `public.compound_xrefs_resolved`. Type: text. Unit: none stated.
- What it is: pubchem_cid | chembl | chebi | wikidata | pdb_ccd.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: Never NULL. Domain: Closed list: pubchem_cid, chembl, chebi, wikidata, pdb_ccd.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `xref_id` (V0045)

- Relation: `public.compound_xrefs_resolved`. Type: text. Unit: none stated.
- What it is: The identifier in that database, in its canonical form: CHEBI:<n>, CHEMBL<n> or the CID as plain digits.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `method` (V0046)

- Relation: `public.compound_xrefs_resolved`. Type: text. Unit: none stated.
- What it is: How the id was obtained (CHECKed list).
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_version` (V0047)

- Relation: `public.compound_xrefs_resolved`. Type: text. Unit: none stated.
- What it is: Version or date of the service answer, when known.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `xref_version` (V0049)

- Relation: `public.compound_xrefs_resolved`. Type: text. Unit: none stated.
- What it is: Version of the S2.10 stage.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_primary` (V0050)

- Relation: `public.compound_xrefs_resolved`. Type: boolean. Unit: none stated.
- What it is: True for the one id of this database that the compound shows as its public id (D-CARD 2): at most one per (compound, xref_db), enforced by a partial unique index.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_shared` (V0051)

- Relation: `public.compound_xrefs_resolved`. Type: boolean. Unit: none stated.
- What it is: True when the same (xref_db, xref_id) is held by more than one compound of the AURORA, in either area (D-CARD 4). A mark, never a merge: the identity of a compound is its InChI. Kept by refresh_xref_shared.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `looked_up_on` (V0052)

- Relation: `public.compound_xrefs_resolved`. Type: date. Unit: none stated.
- What it is: Date of the lookup that produced the row; NULL on the rows written before migration 010, whose date is in source_version.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: May be NULL. NULL on the rows written before migration 010, whose date is in source_version. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_sha256` (V0053)

- Relation: `public.compound_xrefs_resolved`. Type: text. Unit: none stated.
- What it is: sha256 of the source file (or of the saved query result) the id was read from (decision (an), migration 032); required for wikidata and pdb_ccd, NULL on rows written before 032.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: May be NULL. required for wikidata and pdb_ccd, NULL on rows written before 032. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `tautomer_group_key` (V0054)

- Relation: `public.compound_tautomers`. Type: text. Unit: none stated.
- What it is: InChIKey of the canonical tautomer (RDKit TautomerEnumerator); a molecule over the enumeration limit or the time limit keeps its own InChIKey. Indexed: WHERE tautomer_group_key =... lists the group.
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `tautomer_group_size` (V0055)

- Relation: `public.compound_tautomers`. Type: integer. Unit: count.
- What it is: Number of registry compounds that share the key (1 = singleton).
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `tautomer_group_kind` (V0056)

- Relation: `public.compound_tautomers`. Type: text. Unit: none stated.
- What it is: singleton | stereo_only | constitutional | mixed (what separates the members of the group).
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: Never NULL. Domain: Closed list: singleton, stereo_only, constitutional, mixed.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `tautomer_status` (V0057)

- Relation: `public.compound_tautomers`. Type: text. Unit: none stated.
- What it is: ok | limit_reached | timeout | error (how the enumeration ended for this molecule).
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: Never NULL. Domain: Closed list: ok, limit_reached, timeout, error.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `canonical_tautomer_smiles` (V0058)

- Relation: `public.compound_tautomers`. Type: text. Unit: none stated.
- What it is: SMILES of the canonical tautomer; NULL when the enumeration timed out.
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: May be NULL. NULL when the enumeration timed out. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `ket15t_inchikey` (V0059)

- Relation: `public.compound_tautomers`. Type: text. Unit: none stated.
- What it is: Non-standard InChIKey computed by ATHANOR S2.6 with the InChI options /KET /15T (keto-enol and 1,5-tautomerism; flag N, version A), from compound_tautomer_ket15t_v1. A second tautomer key, a mark only: tautomer_group_key stays the grouping (decision (hp)).
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `ket15t_group_size` (V0060)

- Relation: `public.compound_tautomers`. Type: integer. Unit: count.
- What it is: Number of compounds of the release that wrote the row sharing ket15t_inchikey (ATHANOR's count over its whole release, this compound included; >= 1). Null exactly when ket15t_inchikey is null. A later release that does not carry the compound does not recount it.
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: May be NULL. Null exactly when ket15t_inchikey is null. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `ket15t_options` (V0061)

- Relation: `public.compound_tautomers`. Type: text. Unit: none stated.
- What it is: The InChI options of ket15t_inchikey, always '/KET /15T'. Null exactly when the release did not carry compound_tautomer_ket15t_v1 for the compound.
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `ket15t_version` (V0062)

- Relation: `public.compound_tautomers`. Type: text. Unit: none stated.
- What it is: ATHANOR's tautomer version that computed the /KET /15T key (tautomer_version of compound_tautomer_ket15t_v1). Null exactly when ket15t_options is null.
- Origin: RDKit canonical tautomer, S2.6 stage of the pipeline.
- How: RDKit canonical tautomer, S2.6 stage of the pipeline
- NULL: May be NULL. Null exactly when ket15t_options is null. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `connectivity_key` (V0063)

- Relation: `public.compound_stereo_groups`. Type: text. Unit: none stated.
- What it is: Key of the connectivity (stereo removed).
- Origin: Connectivity grouping, S2.9 stage of the pipeline.
- How: Connectivity grouping, S2.9 stage of the pipeline
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `stereo_group_size` (V0064)

- Relation: `public.compound_stereo_groups`. Type: integer. Unit: count.
- What it is: Compounds of the registry in this group (>= 1).
- Origin: Connectivity grouping, S2.9 stage of the pipeline.
- How: Connectivity grouping, S2.9 stage of the pipeline
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `stereo_group_version` (V0065)

- Relation: `public.compound_stereo_groups`. Type: text. Unit: none stated.
- What it is: Version of the S2.9 stage.
- Origin: Connectivity grouping, S2.9 stage of the pipeline.
- How: Connectivity grouping, S2.9 stage of the pipeline
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

## 2D and 3D structure, geometry gates

### `ph_modeled_min` (V0014)

- Relation: `public.compounds`. Type: real. Unit: pH units.
- What it is: Minimum pH this compound's protonation state was modeled across (REAL).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ph_modeled_max` (V0015)

- Relation: `public.compounds`. Type: real. Unit: pH units.
- What it is: Maximum pH this compound's protonation state was modeled across (REAL).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `variant_smiles` (V0075)

- Relation: `public.protonation_variants`. Type: text. Unit: none stated.
- What it is: SMILES of this protonation variant. Unique together with compound_uuid.
- Origin: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions).
- How: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ph_used` (V0076)

- Relation: `public.protonation_variants`. Type: real. Unit: pH units.
- What it is: pH at which the dominant microstate was selected (protonation_dominant_v1.ph_used); NULL for the other microstates of the compound.
- Origin: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions).
- How: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions)
- NULL: May be NULL. NULL for the other microstates of the compound. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_dominant` (V0077)

- Relation: `public.protonation_variants`. Type: boolean. Unit: none stated.
- What it is: Whether this is the single canonical/distributed variant for the compound. Enforced to be unique per compound via a partial UNIQUE index (idx_protonation_one_dominant).
- Origin: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions).
- How: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `charge` (V0078)

- Relation: `public.protonation_variants`. Type: smallint. Unit: none stated.
- What it is: Net formal charge of this microstate. Nullable since v1.8.0 (the contract allows a microstate whose charge the pipeline could not compute); the v1.8.0 release has none.
- Origin: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions).
- How: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions)
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ph_min` (V0079)

- Relation: `public.protonation_variants`. Type: real. Unit: pH units.
- What it is: Lower bound of the pH range this variant was generated for (REAL).
- Origin: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions).
- How: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ph_max` (V0080)

- Relation: `public.protonation_variants`. Type: real. Unit: pH units.
- What it is: Upper bound of the pH range this variant was generated for (REAL).
- Origin: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions).
- How: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `protonation_version` (V0081)

- Relation: `public.protonation_variants`. Type: text. Unit: none stated.
- What it is: Version tag of the protonation tool/pipeline run that produced this variant.
- Origin: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions).
- How: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `created_at` (V0082)

- Relation: `public.protonation_variants`. Type: timestamp with time zone. Unit: none stated.
- What it is: Row insertion timestamp.
- Origin: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions).
- How: Dimorphite-DL microstates, S3.1 and S3.2 stages (version conflict, see open questions)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `minimizer_used` (V0083)

- Relation: `public.conformers`. Type: text. Unit: none stated.
- What it is: Minimizer that produced this geometry. CHECK originally allowed 'aimnet2','mmff94s','uff','source_3d'; tightened by migration 013 (public) / 014 (private) to 'mmff94s','uff','source_3d',  AIMNet2 was permanently removed from the pipeline and never had a real production row.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `embed_method` (V0084)

- Relation: `public.conformers`. Type: text. Unit: none stated.
- What it is: Free-text 3D embedding method (e.g. ETKDGv3, srETKDGv3, or 'source' when coordinates came from the source file); no CHECK constraint.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `energy_kcal_mol` (V0086)

- Relation: `public.conformers`. Type: double precision. Unit: kcal/mol.
- What it is: Minimized conformer energy in kcal/mol, as reported by the minimizer.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `rmsd_from_input` (V0087)

- Relation: `public.conformers`. Type: real. Unit: none stated.
- What it is: RMSD between the generated/minimized conformer and the input geometry.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `posebusters_report` (V0090)

- Relation: `public.conformers`. Type: jsonb. Unit: none stated.
- What it is: JSONB reserved for a per-molecule PoseBusters report; same vestigial, never-populated status as posebusters_pass.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `ph_modeled` (V0091)

- Relation: `public.conformers`. Type: real. Unit: pH units.
- What it is: pH value used when modeling this conformer's protonation state, if applicable.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_canonical` (V0092)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Marks which conformer_index is the canonical one for the compound.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `created_at` (V0093)

- Relation: `public.conformers`. Type: timestamp with time zone. Unit: none stated.
- What it is: Row insertion timestamp.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `conformer_version` (V0103)

- Relation: `public.conformers`. Type: text. Unit: none stated.
- What it is: Version tag of the conformer-generation/gate code that produced this row (e.g. distinguishing gate v1.0.0 output from v1.1.0).
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `geometry_source` (V0112)

- Relation: `public.geometry_validity`. Type: text. Unit: none stated.
- What it is: conformer (the production conformer) | rescue (a geometry from the S4.3 rescue ladder).
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `rescue_strategy` (V0113)

- Relation: `public.geometry_validity`. Type: text. Unit: none stated.
- What it is: The rescue rung that produced the geometry (S4.3); NULL for geometry_source = conformer.
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: May be NULL. NULL for geometry_source = conformer. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `geometry_sha256` (V0114)

- Relation: `public.geometry_validity`. Type: char(27) or char(64). Unit: none stated.
- What it is: sha256 of the geometry that was judged; NULL when there is no geometry (embedding failed).
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: May be NULL. NULL when there is no geometry (embedding failed). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `validity_version` (V0115)

- Relation: `public.geometry_validity`. Type: text. Unit: none stated.
- What it is: Version of the validity stage.
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `pmi1` (V1810)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: First principal moment of inertia of the minimized conformer.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 3166.523014340843.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `pmi2` (V1811)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Second principal moment of inertia.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 5552.395850984317.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `pmi3` (V1812)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Third principal moment of inertia.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 7709.899421455164.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `npr1` (V1813)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Normalized principal moments ratio 1 (shape).
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.4107087318842344.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `npr2` (V1814)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Normalized principal moments ratio 2 (shape).
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.7201644985838687.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `asphericity` (V1815)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Asphericity of the conformer.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.22963158991941518.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `eccentricity` (V1816)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Eccentricity of the conformer.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.9117666025656149.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `inertialshapefactor` (V1817)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Inertial shape factor.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.0002274306851149734.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `radiusofgyration` (V1818)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Radius of gyration of the conformer.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 4.205831595226146.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `spherocityindex` (V1819)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Spherocity index.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.23056273726341334.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `pbf` (V1820)

- Relation: `public.descriptors.values_3d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Plane of best fit: mean distance of the atoms from the best-fit plane.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md) shape descriptors over the minimized conformer.
- How: Computed over the minimized conformer that passed the geometry gate; compounds without an approved conformer have none.
- NULL: Absent when the compound has no approved 3D conformer. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 1.0068938753072263.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_3d).

### `n_conformer_atoms` (V1821)

- Relation: `descriptors3d TSV column (from descriptors3d_v1)`. Type: integer. Unit: count.
- What it is: Atoms of the conformer the 3D descriptors were computed on, hydrogens included.
- Origin: descriptors3d_v1 Parquet of the release.
- How: Carried from the pipeline into the TSV of the bundle.
- NULL: Empty means absent. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 53.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `sdf_title` (V1969)

- Relation: `file content: SDF header line (molecule name)`. Type: text. Unit: none stated.
- What it is: The ALC identifier of the compound, for example ALC1. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md).
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: ALC1 sample of the v2.0.0 release.
- Files: sdf. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (per-compound SDF and PDBQT endpoints).

### `sdf_atom_block` (V1970)

- Relation: `file content: SDF atom block: element and x, y, z coordinates`. Type: text. Unit: angstrom.
- What it is: 3D coordinates of the minimized conformer, hydrogens included, in angstrom as RDKit writes them. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md).
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: sdf. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (per-compound SDF and PDBQT endpoints).

### `sdf_bond_block` (V1971)

- Relation: `file content: SDF bond block: bond table with bond orders`. Type: text. Unit: none stated.
- What it is: Bond table of the 3D structure. The SDF is the neutral parent (decision of 2026-11-12): protonation is declared in tags, not applied to the coordinates. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md).
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: sdf. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (per-compound SDF and PDBQT endpoints).

### `tag_stereo_undefined_in_source` (V1972)

- Relation: `file content: SDF tag stereo_undefined_in_source`. Type: boolean as text. Unit: none stated.
- What it is: True when the curated structure leaves a tetrahedral centre or a double bond without defined stereo, so the 3D file is one stereoisomer chosen by the embedding. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md).
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: sdf, pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the files, not served as a separate field in this release (the SDF endpoint returns the file whole).

### `tag_n_stereo_undefined` (V1973)

- Relation: `file content: SDF tag n_stereo_undefined`. Type: integer as text. Unit: none stated.
- What it is: Number of stereo elements left undefined in the curated structure. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md).
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: sdf, pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the files, not served as a separate field in this release (the SDF endpoint returns the file whole).

## Physico-chemical descriptors

### `heavy_atom_count` (V0007)

- Relation: `public.compounds`. Type: smallint. Unit: count.
- What it is: Number of heavy (non-hydrogen) atoms.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Copied by the loader from descriptors_v1 of the same compound.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 33.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `formal_charge` (V0008)

- Relation: `public.compounds`. Type: smallint. Unit: none stated.
- What it is: Net formal charge of the curated structure.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Copied by the loader from descriptors_v1 of the same compound.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `molecular_weight` (V0121)

- Relation: `public.descriptors`. Type: double precision. Unit: Da (g/mol).
- What it is: Average molecular weight.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit molecular weight of the curated structure.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 464.3790000000002.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `exact_mass` (V0122)

- Relation: `public.descriptors`. Type: double precision. Unit: Da (monoisotopic).
- What it is: Exact (monoisotopic) mass.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit exact molecular weight of the curated structure.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 464.09547607999986.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `logp` (V0123)

- Relation: `public.descriptors`. Type: double precision. Unit: log units.
- What it is: Calculated logP (octanol-water), Crippen model of RDKit.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit Crippen logP of the curated structure.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: -0.5389000000000002.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `tpsa` (V0124)

- Relation: `public.descriptors`. Type: double precision. Unit: square angstrom.
- What it is: Topological polar surface area.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit TPSA (Ertl, Rohde and Selzer 2000, in docs/REFERENCES.md).
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 210.50999999999996.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `num_h_donors` (V0125)

- Relation: `public.descriptors`. Type: smallint. Unit: count.
- What it is: Count of hydrogen-bond donors.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit Lipinski-style donor count.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 8.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `num_h_acceptors` (V0126)

- Relation: `public.descriptors`. Type: smallint. Unit: count.
- What it is: Count of hydrogen-bond acceptors.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit Lipinski-style acceptor count.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 12.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `num_rotatable_bonds` (V0127)

- Relation: `public.descriptors`. Type: smallint. Unit: count.
- What it is: Count of rotatable bonds.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit rotatable-bond count.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 4.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `num_rings` (V0128)

- Relation: `public.descriptors`. Type: smallint. Unit: count.
- What it is: Count of rings.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit ring count.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 4.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `num_aromatic_rings` (V0129)

- Relation: `public.descriptors`. Type: smallint. Unit: count.
- What it is: Count of aromatic rings.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit aromatic ring count.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 3.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `fraction_csp3` (V0130)

- Relation: `public.descriptors`. Type: real. Unit: fraction, 0 to 1.
- What it is: Fraction of carbon atoms that are sp3.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit FractionCSP3.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.2857142857142857.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `qed` (V0131)

- Relation: `public.descriptors`. Type: real. Unit: 0 to 1.
- What it is: Quantitative Estimate of Drug-likeness (Bickerton et al. 2012, in docs/REFERENCES.md).
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: RDKit QED.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.2288751447852227.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `sascore` (V0132)

- Relation: `public.descriptors`. Type: real. Unit: 1 (easy) to 10 (hard).
- What it is: Synthetic accessibility score.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: Synthetic accessibility score as the pipeline computes it; a computed estimate, not a measured property.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 4.007675084390859.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `descriptor_version` (V0133)

- Relation: `public.descriptors`. Type: text. Unit: none stated.
- What it is: Version tag of the descriptor-computation code that produced this row.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: athanor-descriptors-1.0.0.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `n_mordred_null` (V0134)

- Relation: `public.descriptors`. Type: integer. Unit: count.
- What it is: Number of Mordred names with a code (the entries of mordred_null_codes).
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `n_mordred_unexplained` (V0135)

- Relation: `public.descriptors`. Type: integer. Unit: count.
- What it is: ATHANOR's n_unexplained: on the staged release of 2026-10-28, the number of not_reproduced codes of the compound.
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `mordred_null_codes_version` (V0136)

- Relation: `public.descriptors`. Type: text. Unit: none stated.
- What it is: The Mordred version the codes were written with (mordredcommunity).
- Origin: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7.
- How: ATHANOR descriptors_v1 stage, computed with RDKit 2026.03.4 (see docs/REFERENCES.md); Mordred from mordredcommunity 2.0.7
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `heavy_atom_count` (V1802)

- Relation: `public.descriptors.values_2d (JSONB key)`. Type: number (JSON). Unit: count.
- What it is: Number of heavy atoms.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md), descriptors_v1 stage.
- How: Computed over the curated structure at the descriptors stage.
- NULL: Absent only when the descriptor stage gave no value. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 33.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_2d).

### `molar_refractivity` (V1803)

- Relation: `public.descriptors.values_2d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Molar refractivity (Crippen model of RDKit).
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md), descriptors_v1 stage.
- How: Computed over the curated structure at the descriptors stage.
- NULL: Absent only when the descriptor stage gave no value. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 108.97439999999999.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_2d).

### `num_aliphatic_rings` (V1804)

- Relation: `public.descriptors.values_2d (JSONB key)`. Type: number (JSON). Unit: count.
- What it is: Count of aliphatic rings.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md), descriptors_v1 stage.
- How: Computed over the curated structure at the descriptors stage.
- NULL: Absent only when the descriptor stage gave no value. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 1.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_2d).

### `num_heteroatoms` (V1805)

- Relation: `public.descriptors.values_2d (JSONB key)`. Type: number (JSON). Unit: count.
- What it is: Count of heteroatoms (non carbon, non hydrogen).
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md), descriptors_v1 stage.
- How: Computed over the curated structure at the descriptors stage.
- NULL: Absent only when the descriptor stage gave no value. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 12.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_2d).

### `num_stereocenters` (V1806)

- Relation: `public.descriptors.values_2d (JSONB key)`. Type: number (JSON). Unit: count.
- What it is: Count of stereocentres in the curated structure.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md), descriptors_v1 stage.
- How: Computed over the curated structure at the descriptors stage.
- NULL: Absent only when the descriptor stage gave no value. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 5.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_2d).

### `formal_charge` (V1807)

- Relation: `public.descriptors.values_2d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Net formal charge.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md), descriptors_v1 stage.
- How: Computed over the curated structure at the descriptors stage.
- NULL: Absent only when the descriptor stage gave no value. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 0.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_2d).

### `num_valence_electrons` (V1808)

- Relation: `public.descriptors.values_2d (JSONB key)`. Type: number (JSON). Unit: count.
- What it is: Count of valence electrons.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md), descriptors_v1 stage.
- How: Computed over the curated structure at the descriptors stage.
- NULL: Absent only when the descriptor stage gave no value. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 176.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_2d).

### `bertz_complexity` (V1809)

- Relation: `public.descriptors.values_2d (JSONB key)`. Type: number (JSON). Unit: none stated.
- What it is: Bertz molecular complexity index (RDKit BertzCT).
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md), descriptors_v1 stage.
- How: Computed over the curated structure at the descriptors stage.
- NULL: Absent only when the descriptor stage gave no value. Domain: open.
- Example: first data row of the v2.0.0 bioactivity-space TSV: 1250.2041776678584.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (through the features endpoint, JSON block values_2d).

### 11 variables in `public.descriptors.values_2d (JSONB key)`: Graph-theory topological index

Graph-theory topological index. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V0367 | `mord_ABC` | none | yes | no | yes |
| V0368 | `mord_ABCGG` | none | yes | no | yes |
| V0996 | `mord_BalabanJ` | none | yes | no | yes |
| V0997 | `mord_BertzCT` | none | yes | no | yes |
| V1767 | `mord_Diameter` | none | yes | no | yes |
| V1768 | `mord_Radius` | none | yes | no | yes |
| V1769 | `mord_TopoShapeIndex` | none | yes | no | yes |
| V1770 | `mord_PetitjeanIndex` | none | yes | no | yes |
| V1772 | `mord_VAdjMat` | none | yes | no | yes |
| V1796 | `mord_WPath` | none | yes | no | yes |
| V1797 | `mord_WPol` | none | yes | no | yes |

### 24 variables in `public.descriptors.values_2d (JSONB key)`: Count of an atom, bond or substructure kind

Count of an atom, bond or substructure kind. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V0369 | `mord_nAcid` | none | yes | no | yes |
| V0370 | `mord_nBase` | none | yes | no | yes |
| V0371 | `mord_nAromAtom` | none | yes | no | yes |
| V0372 | `mord_nAromBond` | none | yes | no | yes |
| V0373 | `mord_nAtom` | none | yes | no | yes |
| V0374 | `mord_nHeavyAtom` | none | yes | no | yes |
| V0375 | `mord_nSpiro` | none | yes | no | yes |
| V0376 | `mord_nBridgehead` | none | yes | no | yes |
| V0377 | `mord_nHetero` | none | yes | no | yes |
| V0378 | `mord_nH` | none | yes | no | yes |
| V0379 | `mord_nB` | none | yes | no | yes |
| V0380 | `mord_nC` | none | yes | no | yes |
| V0381 | `mord_nN` | none | yes | no | yes |
| V0382 | `mord_nO` | none | yes | no | yes |
| V0383 | `mord_nS` | none | yes | no | yes |
| V0384 | `mord_nP` | none | yes | no | yes |
| V0385 | `mord_nF` | none | yes | no | yes |
| V0386 | `mord_nCl` | none | yes | no | yes |
| V0387 | `mord_nBr` | none | yes | no | yes |
| V0388 | `mord_nI` | none | yes | no | yes |
| V0389 | `mord_nX` | none | yes | no | yes |
| V1456 | `mord_nHBAcc` | none | yes | no | yes |
| V1457 | `mord_nHBDon` | none | yes | no | yes |
| V1740 | `mord_nRot` | none | yes | no | yes |

### 606 variables in `public.descriptors.values_2d (JSONB key)`: Moreau-Broto, Moran or Geary topological autocorrelation of a weighted atom property at a 

Moreau-Broto, Moran or Geary topological autocorrelation of a weighted atom property at a given lag. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V0390 | `mord_ATS0dv` | none | yes | no | yes |
| V0391 | `mord_ATS1dv` | none | yes | no | yes |
| V0392 | `mord_ATS2dv` | none | yes | no | yes |
| V0393 | `mord_ATS3dv` | none | yes | no | yes |
| V0394 | `mord_ATS4dv` | none | yes | no | yes |
| V0395 | `mord_ATS5dv` | none | yes | no | yes |
| V0396 | `mord_ATS6dv` | none | yes | no | yes |
| V0397 | `mord_ATS7dv` | none | yes | no | yes |
| V0398 | `mord_ATS8dv` | none | yes | no | yes |
| V0399 | `mord_ATS0d` | none | yes | no | yes |
| V0400 | `mord_ATS1d` | none | yes | no | yes |
| V0401 | `mord_ATS2d` | none | yes | no | yes |
| V0402 | `mord_ATS3d` | none | yes | no | yes |
| V0403 | `mord_ATS4d` | none | yes | no | yes |
| V0404 | `mord_ATS5d` | none | yes | no | yes |
| V0405 | `mord_ATS6d` | none | yes | no | yes |
| V0406 | `mord_ATS7d` | none | yes | no | yes |
| V0407 | `mord_ATS8d` | none | yes | no | yes |
| V0408 | `mord_ATS0s` | none | yes | no | yes |
| V0409 | `mord_ATS1s` | none | yes | no | yes |
| V0410 | `mord_ATS2s` | none | yes | no | yes |
| V0411 | `mord_ATS3s` | none | yes | no | yes |
| V0412 | `mord_ATS4s` | none | yes | no | yes |
| V0413 | `mord_ATS5s` | none | yes | no | yes |
| V0414 | `mord_ATS6s` | none | yes | no | yes |
| V0415 | `mord_ATS7s` | none | yes | no | yes |
| V0416 | `mord_ATS8s` | none | yes | no | yes |
| V0417 | `mord_ATS0Z` | none | yes | no | yes |
| V0418 | `mord_ATS1Z` | none | yes | no | yes |
| V0419 | `mord_ATS2Z` | none | yes | no | yes |
| V0420 | `mord_ATS3Z` | none | yes | no | yes |
| V0421 | `mord_ATS4Z` | none | yes | no | yes |
| V0422 | `mord_ATS5Z` | none | yes | no | yes |
| V0423 | `mord_ATS6Z` | none | yes | no | yes |
| V0424 | `mord_ATS7Z` | none | yes | no | yes |
| V0425 | `mord_ATS8Z` | none | yes | no | yes |
| V0426 | `mord_ATS0m` | none | yes | no | yes |
| V0427 | `mord_ATS1m` | none | yes | no | yes |
| V0428 | `mord_ATS2m` | none | yes | no | yes |
| V0429 | `mord_ATS3m` | none | yes | no | yes |
| V0430 | `mord_ATS4m` | none | yes | no | yes |
| V0431 | `mord_ATS5m` | none | yes | no | yes |
| V0432 | `mord_ATS6m` | none | yes | no | yes |
| V0433 | `mord_ATS7m` | none | yes | no | yes |
| V0434 | `mord_ATS8m` | none | yes | no | yes |
| V0435 | `mord_ATS0v` | none | yes | no | yes |
| V0436 | `mord_ATS1v` | none | yes | no | yes |
| V0437 | `mord_ATS2v` | none | yes | no | yes |
| V0438 | `mord_ATS3v` | none | yes | no | yes |
| V0439 | `mord_ATS4v` | none | yes | no | yes |
| V0440 | `mord_ATS5v` | none | yes | no | yes |
| V0441 | `mord_ATS6v` | none | yes | no | yes |
| V0442 | `mord_ATS7v` | none | yes | no | yes |
| V0443 | `mord_ATS8v` | none | yes | no | yes |
| V0444 | `mord_ATS0se` | none | yes | no | yes |
| V0445 | `mord_ATS1se` | none | yes | no | yes |
| V0446 | `mord_ATS2se` | none | yes | no | yes |
| V0447 | `mord_ATS3se` | none | yes | no | yes |
| V0448 | `mord_ATS4se` | none | yes | no | yes |
| V0449 | `mord_ATS5se` | none | yes | no | yes |
| V0450 | `mord_ATS6se` | none | yes | no | yes |
| V0451 | `mord_ATS7se` | none | yes | no | yes |
| V0452 | `mord_ATS8se` | none | yes | no | yes |
| V0453 | `mord_ATS0pe` | none | yes | no | yes |
| V0454 | `mord_ATS1pe` | none | yes | no | yes |
| V0455 | `mord_ATS2pe` | none | yes | no | yes |
| V0456 | `mord_ATS3pe` | none | yes | no | yes |
| V0457 | `mord_ATS4pe` | none | yes | no | yes |
| V0458 | `mord_ATS5pe` | none | yes | no | yes |
| V0459 | `mord_ATS6pe` | none | yes | no | yes |
| V0460 | `mord_ATS7pe` | none | yes | no | yes |
| V0461 | `mord_ATS8pe` | none | yes | no | yes |
| V0462 | `mord_ATS0are` | none | yes | no | yes |
| V0463 | `mord_ATS1are` | none | yes | no | yes |
| V0464 | `mord_ATS2are` | none | yes | no | yes |
| V0465 | `mord_ATS3are` | none | yes | no | yes |
| V0466 | `mord_ATS4are` | none | yes | no | yes |
| V0467 | `mord_ATS5are` | none | yes | no | yes |
| V0468 | `mord_ATS6are` | none | yes | no | yes |
| V0469 | `mord_ATS7are` | none | yes | no | yes |
| V0470 | `mord_ATS8are` | none | yes | no | yes |
| V0471 | `mord_ATS0p` | none | yes | no | yes |
| V0472 | `mord_ATS1p` | none | yes | no | yes |
| V0473 | `mord_ATS2p` | none | yes | no | yes |
| V0474 | `mord_ATS3p` | none | yes | no | yes |
| V0475 | `mord_ATS4p` | none | yes | no | yes |
| V0476 | `mord_ATS5p` | none | yes | no | yes |
| V0477 | `mord_ATS6p` | none | yes | no | yes |
| V0478 | `mord_ATS7p` | none | yes | no | yes |
| V0479 | `mord_ATS8p` | none | yes | no | yes |
| V0480 | `mord_ATS0i` | none | yes | no | yes |
| V0481 | `mord_ATS1i` | none | yes | no | yes |
| V0482 | `mord_ATS2i` | none | yes | no | yes |
| V0483 | `mord_ATS3i` | none | yes | no | yes |
| V0484 | `mord_ATS4i` | none | yes | no | yes |
| V0485 | `mord_ATS5i` | none | yes | no | yes |
| V0486 | `mord_ATS6i` | none | yes | no | yes |
| V0487 | `mord_ATS7i` | none | yes | no | yes |
| V0488 | `mord_ATS8i` | none | yes | no | yes |
| V0489 | `mord_AATS0dv` | none | yes | no | yes |
| V0490 | `mord_AATS1dv` | none | yes | no | yes |
| V0491 | `mord_AATS2dv` | none | yes | no | yes |
| V0492 | `mord_AATS3dv` | none | yes | no | yes |
| V0493 | `mord_AATS4dv` | none | yes | no | yes |
| V0494 | `mord_AATS5dv` | none | yes | no | yes |
| V0495 | `mord_AATS6dv` | none | yes | no | yes |
| V0496 | `mord_AATS7dv` | none | yes | no | yes |
| V0497 | `mord_AATS8dv` | none | yes | no | yes |
| V0498 | `mord_AATS0d` | none | yes | no | yes |
| V0499 | `mord_AATS1d` | none | yes | no | yes |
| V0500 | `mord_AATS2d` | none | yes | no | yes |
| V0501 | `mord_AATS3d` | none | yes | no | yes |
| V0502 | `mord_AATS4d` | none | yes | no | yes |
| V0503 | `mord_AATS5d` | none | yes | no | yes |
| V0504 | `mord_AATS6d` | none | yes | no | yes |
| V0505 | `mord_AATS7d` | none | yes | no | yes |
| V0506 | `mord_AATS8d` | none | yes | no | yes |
| V0507 | `mord_AATS0s` | none | yes | no | yes |
| V0508 | `mord_AATS1s` | none | yes | no | yes |
| V0509 | `mord_AATS2s` | none | yes | no | yes |
| V0510 | `mord_AATS3s` | none | yes | no | yes |
| V0511 | `mord_AATS4s` | none | yes | no | yes |
| V0512 | `mord_AATS5s` | none | yes | no | yes |
| V0513 | `mord_AATS6s` | none | yes | no | yes |
| V0514 | `mord_AATS7s` | none | yes | no | yes |
| V0515 | `mord_AATS8s` | none | yes | no | yes |
| V0516 | `mord_AATS0Z` | none | yes | no | yes |
| V0517 | `mord_AATS1Z` | none | yes | no | yes |
| V0518 | `mord_AATS2Z` | none | yes | no | yes |
| V0519 | `mord_AATS3Z` | none | yes | no | yes |
| V0520 | `mord_AATS4Z` | none | yes | no | yes |
| V0521 | `mord_AATS5Z` | none | yes | no | yes |
| V0522 | `mord_AATS6Z` | none | yes | no | yes |
| V0523 | `mord_AATS7Z` | none | yes | no | yes |
| V0524 | `mord_AATS8Z` | none | yes | no | yes |
| V0525 | `mord_AATS0m` | none | yes | no | yes |
| V0526 | `mord_AATS1m` | none | yes | no | yes |
| V0527 | `mord_AATS2m` | none | yes | no | yes |
| V0528 | `mord_AATS3m` | none | yes | no | yes |
| V0529 | `mord_AATS4m` | none | yes | no | yes |
| V0530 | `mord_AATS5m` | none | yes | no | yes |
| V0531 | `mord_AATS6m` | none | yes | no | yes |
| V0532 | `mord_AATS7m` | none | yes | no | yes |
| V0533 | `mord_AATS8m` | none | yes | no | yes |
| V0534 | `mord_AATS0v` | none | yes | no | yes |
| V0535 | `mord_AATS1v` | none | yes | no | yes |
| V0536 | `mord_AATS2v` | none | yes | no | yes |
| V0537 | `mord_AATS3v` | none | yes | no | yes |
| V0538 | `mord_AATS4v` | none | yes | no | yes |
| V0539 | `mord_AATS5v` | none | yes | no | yes |
| V0540 | `mord_AATS6v` | none | yes | no | yes |
| V0541 | `mord_AATS7v` | none | yes | no | yes |
| V0542 | `mord_AATS8v` | none | yes | no | yes |
| V0543 | `mord_AATS0se` | none | yes | no | yes |
| V0544 | `mord_AATS1se` | none | yes | no | yes |
| V0545 | `mord_AATS2se` | none | yes | no | yes |
| V0546 | `mord_AATS3se` | none | yes | no | yes |
| V0547 | `mord_AATS4se` | none | yes | no | yes |
| V0548 | `mord_AATS5se` | none | yes | no | yes |
| V0549 | `mord_AATS6se` | none | yes | no | yes |
| V0550 | `mord_AATS7se` | none | yes | no | yes |
| V0551 | `mord_AATS8se` | none | yes | no | yes |
| V0552 | `mord_AATS0pe` | none | yes | no | yes |
| V0553 | `mord_AATS1pe` | none | yes | no | yes |
| V0554 | `mord_AATS2pe` | none | yes | no | yes |
| V0555 | `mord_AATS3pe` | none | yes | no | yes |
| V0556 | `mord_AATS4pe` | none | yes | no | yes |
| V0557 | `mord_AATS5pe` | none | yes | no | yes |
| V0558 | `mord_AATS6pe` | none | yes | no | yes |
| V0559 | `mord_AATS7pe` | none | yes | no | yes |
| V0560 | `mord_AATS8pe` | none | yes | no | yes |
| V0561 | `mord_AATS0are` | none | yes | no | yes |
| V0562 | `mord_AATS1are` | none | yes | no | yes |
| V0563 | `mord_AATS2are` | none | yes | no | yes |
| V0564 | `mord_AATS3are` | none | yes | no | yes |
| V0565 | `mord_AATS4are` | none | yes | no | yes |
| V0566 | `mord_AATS5are` | none | yes | no | yes |
| V0567 | `mord_AATS6are` | none | yes | no | yes |
| V0568 | `mord_AATS7are` | none | yes | no | yes |
| V0569 | `mord_AATS8are` | none | yes | no | yes |
| V0570 | `mord_AATS0p` | none | yes | no | yes |
| V0571 | `mord_AATS1p` | none | yes | no | yes |
| V0572 | `mord_AATS2p` | none | yes | no | yes |
| V0573 | `mord_AATS3p` | none | yes | no | yes |
| V0574 | `mord_AATS4p` | none | yes | no | yes |
| V0575 | `mord_AATS5p` | none | yes | no | yes |
| V0576 | `mord_AATS6p` | none | yes | no | yes |
| V0577 | `mord_AATS7p` | none | yes | no | yes |
| V0578 | `mord_AATS8p` | none | yes | no | yes |
| V0579 | `mord_AATS0i` | none | yes | no | yes |
| V0580 | `mord_AATS1i` | none | yes | no | yes |
| V0581 | `mord_AATS2i` | none | yes | no | yes |
| V0582 | `mord_AATS3i` | none | yes | no | yes |
| V0583 | `mord_AATS4i` | none | yes | no | yes |
| V0584 | `mord_AATS5i` | none | yes | no | yes |
| V0585 | `mord_AATS6i` | none | yes | no | yes |
| V0586 | `mord_AATS7i` | none | yes | no | yes |
| V0587 | `mord_AATS8i` | none | yes | no | yes |
| V0588 | `mord_ATSC0c` | none | yes | no | yes |
| V0589 | `mord_ATSC1c` | none | yes | no | yes |
| V0590 | `mord_ATSC2c` | none | yes | no | yes |
| V0591 | `mord_ATSC3c` | none | yes | no | yes |
| V0592 | `mord_ATSC4c` | none | yes | no | yes |
| V0593 | `mord_ATSC5c` | none | yes | no | yes |
| V0594 | `mord_ATSC6c` | none | yes | no | yes |
| V0595 | `mord_ATSC7c` | none | yes | no | yes |
| V0596 | `mord_ATSC8c` | none | yes | no | yes |
| V0597 | `mord_ATSC0dv` | none | yes | no | yes |
| V0598 | `mord_ATSC1dv` | none | yes | no | yes |
| V0599 | `mord_ATSC2dv` | none | yes | no | yes |
| V0600 | `mord_ATSC3dv` | none | yes | no | yes |
| V0601 | `mord_ATSC4dv` | none | yes | no | yes |
| V0602 | `mord_ATSC5dv` | none | yes | no | yes |
| V0603 | `mord_ATSC6dv` | none | yes | no | yes |
| V0604 | `mord_ATSC7dv` | none | yes | no | yes |
| V0605 | `mord_ATSC8dv` | none | yes | no | yes |
| V0606 | `mord_ATSC0d` | none | yes | no | yes |
| V0607 | `mord_ATSC1d` | none | yes | no | yes |
| V0608 | `mord_ATSC2d` | none | yes | no | yes |
| V0609 | `mord_ATSC3d` | none | yes | no | yes |
| V0610 | `mord_ATSC4d` | none | yes | no | yes |
| V0611 | `mord_ATSC5d` | none | yes | no | yes |
| V0612 | `mord_ATSC6d` | none | yes | no | yes |
| V0613 | `mord_ATSC7d` | none | yes | no | yes |
| V0614 | `mord_ATSC8d` | none | yes | no | yes |
| V0615 | `mord_ATSC0s` | none | yes | no | yes |
| V0616 | `mord_ATSC1s` | none | yes | no | yes |
| V0617 | `mord_ATSC2s` | none | yes | no | yes |
| V0618 | `mord_ATSC3s` | none | yes | no | yes |
| V0619 | `mord_ATSC4s` | none | yes | no | yes |
| V0620 | `mord_ATSC5s` | none | yes | no | yes |
| V0621 | `mord_ATSC6s` | none | yes | no | yes |
| V0622 | `mord_ATSC7s` | none | yes | no | yes |
| V0623 | `mord_ATSC8s` | none | yes | no | yes |
| V0624 | `mord_ATSC0Z` | none | yes | no | yes |
| V0625 | `mord_ATSC1Z` | none | yes | no | yes |
| V0626 | `mord_ATSC2Z` | none | yes | no | yes |
| V0627 | `mord_ATSC3Z` | none | yes | no | yes |
| V0628 | `mord_ATSC4Z` | none | yes | no | yes |
| V0629 | `mord_ATSC5Z` | none | yes | no | yes |
| V0630 | `mord_ATSC6Z` | none | yes | no | yes |
| V0631 | `mord_ATSC7Z` | none | yes | no | yes |
| V0632 | `mord_ATSC8Z` | none | yes | no | yes |
| V0633 | `mord_ATSC0m` | none | yes | no | yes |
| V0634 | `mord_ATSC1m` | none | yes | no | yes |
| V0635 | `mord_ATSC2m` | none | yes | no | yes |
| V0636 | `mord_ATSC3m` | none | yes | no | yes |
| V0637 | `mord_ATSC4m` | none | yes | no | yes |
| V0638 | `mord_ATSC5m` | none | yes | no | yes |
| V0639 | `mord_ATSC6m` | none | yes | no | yes |
| V0640 | `mord_ATSC7m` | none | yes | no | yes |
| V0641 | `mord_ATSC8m` | none | yes | no | yes |
| V0642 | `mord_ATSC0v` | none | yes | no | yes |
| V0643 | `mord_ATSC1v` | none | yes | no | yes |
| V0644 | `mord_ATSC2v` | none | yes | no | yes |
| V0645 | `mord_ATSC3v` | none | yes | no | yes |
| V0646 | `mord_ATSC4v` | none | yes | no | yes |
| V0647 | `mord_ATSC5v` | none | yes | no | yes |
| V0648 | `mord_ATSC6v` | none | yes | no | yes |
| V0649 | `mord_ATSC7v` | none | yes | no | yes |
| V0650 | `mord_ATSC8v` | none | yes | no | yes |
| V0651 | `mord_ATSC0se` | none | yes | no | yes |
| V0652 | `mord_ATSC1se` | none | yes | no | yes |
| V0653 | `mord_ATSC2se` | none | yes | no | yes |
| V0654 | `mord_ATSC3se` | none | yes | no | yes |
| V0655 | `mord_ATSC4se` | none | yes | no | yes |
| V0656 | `mord_ATSC5se` | none | yes | no | yes |
| V0657 | `mord_ATSC6se` | none | yes | no | yes |
| V0658 | `mord_ATSC7se` | none | yes | no | yes |
| V0659 | `mord_ATSC8se` | none | yes | no | yes |
| V0660 | `mord_ATSC0pe` | none | yes | no | yes |
| V0661 | `mord_ATSC1pe` | none | yes | no | yes |
| V0662 | `mord_ATSC2pe` | none | yes | no | yes |
| V0663 | `mord_ATSC3pe` | none | yes | no | yes |
| V0664 | `mord_ATSC4pe` | none | yes | no | yes |
| V0665 | `mord_ATSC5pe` | none | yes | no | yes |
| V0666 | `mord_ATSC6pe` | none | yes | no | yes |
| V0667 | `mord_ATSC7pe` | none | yes | no | yes |
| V0668 | `mord_ATSC8pe` | none | yes | no | yes |
| V0669 | `mord_ATSC0are` | none | yes | no | yes |
| V0670 | `mord_ATSC1are` | none | yes | no | yes |
| V0671 | `mord_ATSC2are` | none | yes | no | yes |
| V0672 | `mord_ATSC3are` | none | yes | no | yes |
| V0673 | `mord_ATSC4are` | none | yes | no | yes |
| V0674 | `mord_ATSC5are` | none | yes | no | yes |
| V0675 | `mord_ATSC6are` | none | yes | no | yes |
| V0676 | `mord_ATSC7are` | none | yes | no | yes |
| V0677 | `mord_ATSC8are` | none | yes | no | yes |
| V0678 | `mord_ATSC0p` | none | yes | no | yes |
| V0679 | `mord_ATSC1p` | none | yes | no | yes |
| V0680 | `mord_ATSC2p` | none | yes | no | yes |
| V0681 | `mord_ATSC3p` | none | yes | no | yes |
| V0682 | `mord_ATSC4p` | none | yes | no | yes |
| V0683 | `mord_ATSC5p` | none | yes | no | yes |
| V0684 | `mord_ATSC6p` | none | yes | no | yes |
| V0685 | `mord_ATSC7p` | none | yes | no | yes |
| V0686 | `mord_ATSC8p` | none | yes | no | yes |
| V0687 | `mord_ATSC0i` | none | yes | no | yes |
| V0688 | `mord_ATSC1i` | none | yes | no | yes |
| V0689 | `mord_ATSC2i` | none | yes | no | yes |
| V0690 | `mord_ATSC3i` | none | yes | no | yes |
| V0691 | `mord_ATSC4i` | none | yes | no | yes |
| V0692 | `mord_ATSC5i` | none | yes | no | yes |
| V0693 | `mord_ATSC6i` | none | yes | no | yes |
| V0694 | `mord_ATSC7i` | none | yes | no | yes |
| V0695 | `mord_ATSC8i` | none | yes | no | yes |
| V0696 | `mord_AATSC0c` | none | yes | no | yes |
| V0697 | `mord_AATSC1c` | none | yes | no | yes |
| V0698 | `mord_AATSC2c` | none | yes | no | yes |
| V0699 | `mord_AATSC3c` | none | yes | no | yes |
| V0700 | `mord_AATSC4c` | none | yes | no | yes |
| V0701 | `mord_AATSC5c` | none | yes | no | yes |
| V0702 | `mord_AATSC6c` | none | yes | no | yes |
| V0703 | `mord_AATSC7c` | none | yes | no | yes |
| V0704 | `mord_AATSC8c` | none | yes | no | yes |
| V0705 | `mord_AATSC0dv` | none | yes | no | yes |
| V0706 | `mord_AATSC1dv` | none | yes | no | yes |
| V0707 | `mord_AATSC2dv` | none | yes | no | yes |
| V0708 | `mord_AATSC3dv` | none | yes | no | yes |
| V0709 | `mord_AATSC4dv` | none | yes | no | yes |
| V0710 | `mord_AATSC5dv` | none | yes | no | yes |
| V0711 | `mord_AATSC6dv` | none | yes | no | yes |
| V0712 | `mord_AATSC7dv` | none | yes | no | yes |
| V0713 | `mord_AATSC8dv` | none | yes | no | yes |
| V0714 | `mord_AATSC0d` | none | yes | no | yes |
| V0715 | `mord_AATSC1d` | none | yes | no | yes |
| V0716 | `mord_AATSC2d` | none | yes | no | yes |
| V0717 | `mord_AATSC3d` | none | yes | no | yes |
| V0718 | `mord_AATSC4d` | none | yes | no | yes |
| V0719 | `mord_AATSC5d` | none | yes | no | yes |
| V0720 | `mord_AATSC6d` | none | yes | no | yes |
| V0721 | `mord_AATSC7d` | none | yes | no | yes |
| V0722 | `mord_AATSC8d` | none | yes | no | yes |
| V0723 | `mord_AATSC0s` | none | yes | no | yes |
| V0724 | `mord_AATSC1s` | none | yes | no | yes |
| V0725 | `mord_AATSC2s` | none | yes | no | yes |
| V0726 | `mord_AATSC3s` | none | yes | no | yes |
| V0727 | `mord_AATSC4s` | none | yes | no | yes |
| V0728 | `mord_AATSC5s` | none | yes | no | yes |
| V0729 | `mord_AATSC6s` | none | yes | no | yes |
| V0730 | `mord_AATSC7s` | none | yes | no | yes |
| V0731 | `mord_AATSC8s` | none | yes | no | yes |
| V0732 | `mord_AATSC0Z` | none | yes | no | yes |
| V0733 | `mord_AATSC1Z` | none | yes | no | yes |
| V0734 | `mord_AATSC2Z` | none | yes | no | yes |
| V0735 | `mord_AATSC3Z` | none | yes | no | yes |
| V0736 | `mord_AATSC4Z` | none | yes | no | yes |
| V0737 | `mord_AATSC5Z` | none | yes | no | yes |
| V0738 | `mord_AATSC6Z` | none | yes | no | yes |
| V0739 | `mord_AATSC7Z` | none | yes | no | yes |
| V0740 | `mord_AATSC8Z` | none | yes | no | yes |
| V0741 | `mord_AATSC0m` | none | yes | no | yes |
| V0742 | `mord_AATSC1m` | none | yes | no | yes |
| V0743 | `mord_AATSC2m` | none | yes | no | yes |
| V0744 | `mord_AATSC3m` | none | yes | no | yes |
| V0745 | `mord_AATSC4m` | none | yes | no | yes |
| V0746 | `mord_AATSC5m` | none | yes | no | yes |
| V0747 | `mord_AATSC6m` | none | yes | no | yes |
| V0748 | `mord_AATSC7m` | none | yes | no | yes |
| V0749 | `mord_AATSC8m` | none | yes | no | yes |
| V0750 | `mord_AATSC0v` | none | yes | no | yes |
| V0751 | `mord_AATSC1v` | none | yes | no | yes |
| V0752 | `mord_AATSC2v` | none | yes | no | yes |
| V0753 | `mord_AATSC3v` | none | yes | no | yes |
| V0754 | `mord_AATSC4v` | none | yes | no | yes |
| V0755 | `mord_AATSC5v` | none | yes | no | yes |
| V0756 | `mord_AATSC6v` | none | yes | no | yes |
| V0757 | `mord_AATSC7v` | none | yes | no | yes |
| V0758 | `mord_AATSC8v` | none | yes | no | yes |
| V0759 | `mord_AATSC0se` | none | yes | no | yes |
| V0760 | `mord_AATSC1se` | none | yes | no | yes |
| V0761 | `mord_AATSC2se` | none | yes | no | yes |
| V0762 | `mord_AATSC3se` | none | yes | no | yes |
| V0763 | `mord_AATSC4se` | none | yes | no | yes |
| V0764 | `mord_AATSC5se` | none | yes | no | yes |
| V0765 | `mord_AATSC6se` | none | yes | no | yes |
| V0766 | `mord_AATSC7se` | none | yes | no | yes |
| V0767 | `mord_AATSC8se` | none | yes | no | yes |
| V0768 | `mord_AATSC0pe` | none | yes | no | yes |
| V0769 | `mord_AATSC1pe` | none | yes | no | yes |
| V0770 | `mord_AATSC2pe` | none | yes | no | yes |
| V0771 | `mord_AATSC3pe` | none | yes | no | yes |
| V0772 | `mord_AATSC4pe` | none | yes | no | yes |
| V0773 | `mord_AATSC5pe` | none | yes | no | yes |
| V0774 | `mord_AATSC6pe` | none | yes | no | yes |
| V0775 | `mord_AATSC7pe` | none | yes | no | yes |
| V0776 | `mord_AATSC8pe` | none | yes | no | yes |
| V0777 | `mord_AATSC0are` | none | yes | no | yes |
| V0778 | `mord_AATSC1are` | none | yes | no | yes |
| V0779 | `mord_AATSC2are` | none | yes | no | yes |
| V0780 | `mord_AATSC3are` | none | yes | no | yes |
| V0781 | `mord_AATSC4are` | none | yes | no | yes |
| V0782 | `mord_AATSC5are` | none | yes | no | yes |
| V0783 | `mord_AATSC6are` | none | yes | no | yes |
| V0784 | `mord_AATSC7are` | none | yes | no | yes |
| V0785 | `mord_AATSC8are` | none | yes | no | yes |
| V0786 | `mord_AATSC0p` | none | yes | no | yes |
| V0787 | `mord_AATSC1p` | none | yes | no | yes |
| V0788 | `mord_AATSC2p` | none | yes | no | yes |
| V0789 | `mord_AATSC3p` | none | yes | no | yes |
| V0790 | `mord_AATSC4p` | none | yes | no | yes |
| V0791 | `mord_AATSC5p` | none | yes | no | yes |
| V0792 | `mord_AATSC6p` | none | yes | no | yes |
| V0793 | `mord_AATSC7p` | none | yes | no | yes |
| V0794 | `mord_AATSC8p` | none | yes | no | yes |
| V0795 | `mord_AATSC0i` | none | yes | no | yes |
| V0796 | `mord_AATSC1i` | none | yes | no | yes |
| V0797 | `mord_AATSC2i` | none | yes | no | yes |
| V0798 | `mord_AATSC3i` | none | yes | no | yes |
| V0799 | `mord_AATSC4i` | none | yes | no | yes |
| V0800 | `mord_AATSC5i` | none | yes | no | yes |
| V0801 | `mord_AATSC6i` | none | yes | no | yes |
| V0802 | `mord_AATSC7i` | none | yes | no | yes |
| V0803 | `mord_AATSC8i` | none | yes | no | yes |
| V0804 | `mord_MATS1c` | none | yes | no | yes |
| V0805 | `mord_MATS2c` | none | yes | no | yes |
| V0806 | `mord_MATS3c` | none | yes | no | yes |
| V0807 | `mord_MATS4c` | none | yes | no | yes |
| V0808 | `mord_MATS5c` | none | yes | no | yes |
| V0809 | `mord_MATS6c` | none | yes | no | yes |
| V0810 | `mord_MATS7c` | none | yes | no | yes |
| V0811 | `mord_MATS8c` | none | yes | no | yes |
| V0812 | `mord_MATS1dv` | none | yes | no | yes |
| V0813 | `mord_MATS2dv` | none | yes | no | yes |
| V0814 | `mord_MATS3dv` | none | yes | no | yes |
| V0815 | `mord_MATS4dv` | none | yes | no | yes |
| V0816 | `mord_MATS5dv` | none | yes | no | yes |
| V0817 | `mord_MATS6dv` | none | yes | no | yes |
| V0818 | `mord_MATS7dv` | none | yes | no | yes |
| V0819 | `mord_MATS8dv` | none | yes | no | yes |
| V0820 | `mord_MATS1d` | none | yes | no | yes |
| V0821 | `mord_MATS2d` | none | yes | no | yes |
| V0822 | `mord_MATS3d` | none | yes | no | yes |
| V0823 | `mord_MATS4d` | none | yes | no | yes |
| V0824 | `mord_MATS5d` | none | yes | no | yes |
| V0825 | `mord_MATS6d` | none | yes | no | yes |
| V0826 | `mord_MATS7d` | none | yes | no | yes |
| V0827 | `mord_MATS8d` | none | yes | no | yes |
| V0828 | `mord_MATS1s` | none | yes | no | yes |
| V0829 | `mord_MATS2s` | none | yes | no | yes |
| V0830 | `mord_MATS3s` | none | yes | no | yes |
| V0831 | `mord_MATS4s` | none | yes | no | yes |
| V0832 | `mord_MATS5s` | none | yes | no | yes |
| V0833 | `mord_MATS6s` | none | yes | no | yes |
| V0834 | `mord_MATS7s` | none | yes | no | yes |
| V0835 | `mord_MATS8s` | none | yes | no | yes |
| V0836 | `mord_MATS1Z` | none | yes | no | yes |
| V0837 | `mord_MATS2Z` | none | yes | no | yes |
| V0838 | `mord_MATS3Z` | none | yes | no | yes |
| V0839 | `mord_MATS4Z` | none | yes | no | yes |
| V0840 | `mord_MATS5Z` | none | yes | no | yes |
| V0841 | `mord_MATS6Z` | none | yes | no | yes |
| V0842 | `mord_MATS7Z` | none | yes | no | yes |
| V0843 | `mord_MATS8Z` | none | yes | no | yes |
| V0844 | `mord_MATS1m` | none | yes | no | yes |
| V0845 | `mord_MATS2m` | none | yes | no | yes |
| V0846 | `mord_MATS3m` | none | yes | no | yes |
| V0847 | `mord_MATS4m` | none | yes | no | yes |
| V0848 | `mord_MATS5m` | none | yes | no | yes |
| V0849 | `mord_MATS6m` | none | yes | no | yes |
| V0850 | `mord_MATS7m` | none | yes | no | yes |
| V0851 | `mord_MATS8m` | none | yes | no | yes |
| V0852 | `mord_MATS1v` | none | yes | no | yes |
| V0853 | `mord_MATS2v` | none | yes | no | yes |
| V0854 | `mord_MATS3v` | none | yes | no | yes |
| V0855 | `mord_MATS4v` | none | yes | no | yes |
| V0856 | `mord_MATS5v` | none | yes | no | yes |
| V0857 | `mord_MATS6v` | none | yes | no | yes |
| V0858 | `mord_MATS7v` | none | yes | no | yes |
| V0859 | `mord_MATS8v` | none | yes | no | yes |
| V0860 | `mord_MATS1se` | none | yes | no | yes |
| V0861 | `mord_MATS2se` | none | yes | no | yes |
| V0862 | `mord_MATS3se` | none | yes | no | yes |
| V0863 | `mord_MATS4se` | none | yes | no | yes |
| V0864 | `mord_MATS5se` | none | yes | no | yes |
| V0865 | `mord_MATS6se` | none | yes | no | yes |
| V0866 | `mord_MATS7se` | none | yes | no | yes |
| V0867 | `mord_MATS8se` | none | yes | no | yes |
| V0868 | `mord_MATS1pe` | none | yes | no | yes |
| V0869 | `mord_MATS2pe` | none | yes | no | yes |
| V0870 | `mord_MATS3pe` | none | yes | no | yes |
| V0871 | `mord_MATS4pe` | none | yes | no | yes |
| V0872 | `mord_MATS5pe` | none | yes | no | yes |
| V0873 | `mord_MATS6pe` | none | yes | no | yes |
| V0874 | `mord_MATS7pe` | none | yes | no | yes |
| V0875 | `mord_MATS8pe` | none | yes | no | yes |
| V0876 | `mord_MATS1are` | none | yes | no | yes |
| V0877 | `mord_MATS2are` | none | yes | no | yes |
| V0878 | `mord_MATS3are` | none | yes | no | yes |
| V0879 | `mord_MATS4are` | none | yes | no | yes |
| V0880 | `mord_MATS5are` | none | yes | no | yes |
| V0881 | `mord_MATS6are` | none | yes | no | yes |
| V0882 | `mord_MATS7are` | none | yes | no | yes |
| V0883 | `mord_MATS8are` | none | yes | no | yes |
| V0884 | `mord_MATS1p` | none | yes | no | yes |
| V0885 | `mord_MATS2p` | none | yes | no | yes |
| V0886 | `mord_MATS3p` | none | yes | no | yes |
| V0887 | `mord_MATS4p` | none | yes | no | yes |
| V0888 | `mord_MATS5p` | none | yes | no | yes |
| V0889 | `mord_MATS6p` | none | yes | no | yes |
| V0890 | `mord_MATS7p` | none | yes | no | yes |
| V0891 | `mord_MATS8p` | none | yes | no | yes |
| V0892 | `mord_MATS1i` | none | yes | no | yes |
| V0893 | `mord_MATS2i` | none | yes | no | yes |
| V0894 | `mord_MATS3i` | none | yes | no | yes |
| V0895 | `mord_MATS4i` | none | yes | no | yes |
| V0896 | `mord_MATS5i` | none | yes | no | yes |
| V0897 | `mord_MATS6i` | none | yes | no | yes |
| V0898 | `mord_MATS7i` | none | yes | no | yes |
| V0899 | `mord_MATS8i` | none | yes | no | yes |
| V0900 | `mord_GATS1c` | none | yes | no | yes |
| V0901 | `mord_GATS2c` | none | yes | no | yes |
| V0902 | `mord_GATS3c` | none | yes | no | yes |
| V0903 | `mord_GATS4c` | none | yes | no | yes |
| V0904 | `mord_GATS5c` | none | yes | no | yes |
| V0905 | `mord_GATS6c` | none | yes | no | yes |
| V0906 | `mord_GATS7c` | none | yes | no | yes |
| V0907 | `mord_GATS8c` | none | yes | no | yes |
| V0908 | `mord_GATS1dv` | none | yes | no | yes |
| V0909 | `mord_GATS2dv` | none | yes | no | yes |
| V0910 | `mord_GATS3dv` | none | yes | no | yes |
| V0911 | `mord_GATS4dv` | none | yes | no | yes |
| V0912 | `mord_GATS5dv` | none | yes | no | yes |
| V0913 | `mord_GATS6dv` | none | yes | no | yes |
| V0914 | `mord_GATS7dv` | none | yes | no | yes |
| V0915 | `mord_GATS8dv` | none | yes | no | yes |
| V0916 | `mord_GATS1d` | none | yes | no | yes |
| V0917 | `mord_GATS2d` | none | yes | no | yes |
| V0918 | `mord_GATS3d` | none | yes | no | yes |
| V0919 | `mord_GATS4d` | none | yes | no | yes |
| V0920 | `mord_GATS5d` | none | yes | no | yes |
| V0921 | `mord_GATS6d` | none | yes | no | yes |
| V0922 | `mord_GATS7d` | none | yes | no | yes |
| V0923 | `mord_GATS8d` | none | yes | no | yes |
| V0924 | `mord_GATS1s` | none | yes | no | yes |
| V0925 | `mord_GATS2s` | none | yes | no | yes |
| V0926 | `mord_GATS3s` | none | yes | no | yes |
| V0927 | `mord_GATS4s` | none | yes | no | yes |
| V0928 | `mord_GATS5s` | none | yes | no | yes |
| V0929 | `mord_GATS6s` | none | yes | no | yes |
| V0930 | `mord_GATS7s` | none | yes | no | yes |
| V0931 | `mord_GATS8s` | none | yes | no | yes |
| V0932 | `mord_GATS1Z` | none | yes | no | yes |
| V0933 | `mord_GATS2Z` | none | yes | no | yes |
| V0934 | `mord_GATS3Z` | none | yes | no | yes |
| V0935 | `mord_GATS4Z` | none | yes | no | yes |
| V0936 | `mord_GATS5Z` | none | yes | no | yes |
| V0937 | `mord_GATS6Z` | none | yes | no | yes |
| V0938 | `mord_GATS7Z` | none | yes | no | yes |
| V0939 | `mord_GATS8Z` | none | yes | no | yes |
| V0940 | `mord_GATS1m` | none | yes | no | yes |
| V0941 | `mord_GATS2m` | none | yes | no | yes |
| V0942 | `mord_GATS3m` | none | yes | no | yes |
| V0943 | `mord_GATS4m` | none | yes | no | yes |
| V0944 | `mord_GATS5m` | none | yes | no | yes |
| V0945 | `mord_GATS6m` | none | yes | no | yes |
| V0946 | `mord_GATS7m` | none | yes | no | yes |
| V0947 | `mord_GATS8m` | none | yes | no | yes |
| V0948 | `mord_GATS1v` | none | yes | no | yes |
| V0949 | `mord_GATS2v` | none | yes | no | yes |
| V0950 | `mord_GATS3v` | none | yes | no | yes |
| V0951 | `mord_GATS4v` | none | yes | no | yes |
| V0952 | `mord_GATS5v` | none | yes | no | yes |
| V0953 | `mord_GATS6v` | none | yes | no | yes |
| V0954 | `mord_GATS7v` | none | yes | no | yes |
| V0955 | `mord_GATS8v` | none | yes | no | yes |
| V0956 | `mord_GATS1se` | none | yes | no | yes |
| V0957 | `mord_GATS2se` | none | yes | no | yes |
| V0958 | `mord_GATS3se` | none | yes | no | yes |
| V0959 | `mord_GATS4se` | none | yes | no | yes |
| V0960 | `mord_GATS5se` | none | yes | no | yes |
| V0961 | `mord_GATS6se` | none | yes | no | yes |
| V0962 | `mord_GATS7se` | none | yes | no | yes |
| V0963 | `mord_GATS8se` | none | yes | no | yes |
| V0964 | `mord_GATS1pe` | none | yes | no | yes |
| V0965 | `mord_GATS2pe` | none | yes | no | yes |
| V0966 | `mord_GATS3pe` | none | yes | no | yes |
| V0967 | `mord_GATS4pe` | none | yes | no | yes |
| V0968 | `mord_GATS5pe` | none | yes | no | yes |
| V0969 | `mord_GATS6pe` | none | yes | no | yes |
| V0970 | `mord_GATS7pe` | none | yes | no | yes |
| V0971 | `mord_GATS8pe` | none | yes | no | yes |
| V0972 | `mord_GATS1are` | none | yes | no | yes |
| V0973 | `mord_GATS2are` | none | yes | no | yes |
| V0974 | `mord_GATS3are` | none | yes | no | yes |
| V0975 | `mord_GATS4are` | none | yes | no | yes |
| V0976 | `mord_GATS5are` | none | yes | no | yes |
| V0977 | `mord_GATS6are` | none | yes | no | yes |
| V0978 | `mord_GATS7are` | none | yes | no | yes |
| V0979 | `mord_GATS8are` | none | yes | no | yes |
| V0980 | `mord_GATS1p` | none | yes | no | yes |
| V0981 | `mord_GATS2p` | none | yes | no | yes |
| V0982 | `mord_GATS3p` | none | yes | no | yes |
| V0983 | `mord_GATS4p` | none | yes | no | yes |
| V0984 | `mord_GATS5p` | none | yes | no | yes |
| V0985 | `mord_GATS6p` | none | yes | no | yes |
| V0986 | `mord_GATS7p` | none | yes | no | yes |
| V0987 | `mord_GATS8p` | none | yes | no | yes |
| V0988 | `mord_GATS1i` | none | yes | no | yes |
| V0989 | `mord_GATS2i` | none | yes | no | yes |
| V0990 | `mord_GATS3i` | none | yes | no | yes |
| V0991 | `mord_GATS4i` | none | yes | no | yes |
| V0992 | `mord_GATS5i` | none | yes | no | yes |
| V0993 | `mord_GATS6i` | none | yes | no | yes |
| V0994 | `mord_GATS7i` | none | yes | no | yes |
| V0995 | `mord_GATS8i` | none | yes | no | yes |

### 9 variables in `public.descriptors.values_2d (JSONB key)`: Bond count, optionally restricted to a bond type

Bond count, optionally restricted to a bond type. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V0998 | `mord_nBonds` | none | yes | no | yes |
| V0999 | `mord_nBondsO` | none | yes | no | yes |
| V1000 | `mord_nBondsS` | none | yes | no | yes |
| V1001 | `mord_nBondsD` | none | yes | no | yes |
| V1002 | `mord_nBondsT` | none | yes | no | yes |
| V1003 | `mord_nBondsA` | none | yes | no | yes |
| V1004 | `mord_nBondsM` | none | yes | no | yes |
| V1005 | `mord_nBondsKS` | none | yes | no | yes |
| V1006 | `mord_nBondsKD` | none | yes | no | yes |

### 475 variables in `public.descriptors.values_2d (JSONB key)`: Mordred 2D descriptor; no family-level description is written for this name (open question

Mordred 2D descriptor; no family-level description is written for this name (open question OQ5). Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1007 | `mord_RNCG` | none | yes | no | yes |
| V1008 | `mord_RPCG` | none | yes | no | yes |
| V1009 | `mord_C1SP1` | none | yes | no | yes |
| V1010 | `mord_C2SP1` | none | yes | no | yes |
| V1011 | `mord_C1SP2` | none | yes | no | yes |
| V1012 | `mord_C2SP2` | none | yes | no | yes |
| V1013 | `mord_C3SP2` | none | yes | no | yes |
| V1014 | `mord_C1SP3` | none | yes | no | yes |
| V1015 | `mord_C2SP3` | none | yes | no | yes |
| V1016 | `mord_C3SP3` | none | yes | no | yes |
| V1017 | `mord_C4SP3` | none | yes | no | yes |
| V1018 | `mord_HybRatio` | none | yes | no | yes |
| V1019 | `mord_FCSP3` | none | yes | no | yes |
| V1020 | `mord_Xch_3d` | none | yes | no | yes |
| V1021 | `mord_Xch_4d` | none | yes | no | yes |
| V1022 | `mord_Xch_5d` | none | yes | no | yes |
| V1023 | `mord_Xch_6d` | none | yes | no | yes |
| V1024 | `mord_Xch_7d` | none | yes | no | yes |
| V1025 | `mord_Xch_3dv` | none | yes | no | yes |
| V1026 | `mord_Xch_4dv` | none | yes | no | yes |
| V1027 | `mord_Xch_5dv` | none | yes | no | yes |
| V1028 | `mord_Xch_6dv` | none | yes | no | yes |
| V1029 | `mord_Xch_7dv` | none | yes | no | yes |
| V1030 | `mord_Xc_3d` | none | yes | no | yes |
| V1031 | `mord_Xc_4d` | none | yes | no | yes |
| V1032 | `mord_Xc_5d` | none | yes | no | yes |
| V1033 | `mord_Xc_6d` | none | yes | no | yes |
| V1034 | `mord_Xc_3dv` | none | yes | no | yes |
| V1035 | `mord_Xc_4dv` | none | yes | no | yes |
| V1036 | `mord_Xc_5dv` | none | yes | no | yes |
| V1037 | `mord_Xc_6dv` | none | yes | no | yes |
| V1038 | `mord_Xpc_4d` | none | yes | no | yes |
| V1039 | `mord_Xpc_5d` | none | yes | no | yes |
| V1040 | `mord_Xpc_6d` | none | yes | no | yes |
| V1041 | `mord_Xpc_4dv` | none | yes | no | yes |
| V1042 | `mord_Xpc_5dv` | none | yes | no | yes |
| V1043 | `mord_Xpc_6dv` | none | yes | no | yes |
| V1044 | `mord_Xp_0d` | none | yes | no | yes |
| V1045 | `mord_Xp_1d` | none | yes | no | yes |
| V1046 | `mord_Xp_2d` | none | yes | no | yes |
| V1047 | `mord_Xp_3d` | none | yes | no | yes |
| V1048 | `mord_Xp_4d` | none | yes | no | yes |
| V1049 | `mord_Xp_5d` | none | yes | no | yes |
| V1050 | `mord_Xp_6d` | none | yes | no | yes |
| V1051 | `mord_Xp_7d` | none | yes | no | yes |
| V1052 | `mord_AXp_0d` | none | yes | no | yes |
| V1053 | `mord_AXp_1d` | none | yes | no | yes |
| V1054 | `mord_AXp_2d` | none | yes | no | yes |
| V1055 | `mord_AXp_3d` | none | yes | no | yes |
| V1056 | `mord_AXp_4d` | none | yes | no | yes |
| V1057 | `mord_AXp_5d` | none | yes | no | yes |
| V1058 | `mord_AXp_6d` | none | yes | no | yes |
| V1059 | `mord_AXp_7d` | none | yes | no | yes |
| V1060 | `mord_Xp_0dv` | none | yes | no | yes |
| V1061 | `mord_Xp_1dv` | none | yes | no | yes |
| V1062 | `mord_Xp_2dv` | none | yes | no | yes |
| V1063 | `mord_Xp_3dv` | none | yes | no | yes |
| V1064 | `mord_Xp_4dv` | none | yes | no | yes |
| V1065 | `mord_Xp_5dv` | none | yes | no | yes |
| V1066 | `mord_Xp_6dv` | none | yes | no | yes |
| V1067 | `mord_Xp_7dv` | none | yes | no | yes |
| V1068 | `mord_AXp_0dv` | none | yes | no | yes |
| V1069 | `mord_AXp_1dv` | none | yes | no | yes |
| V1070 | `mord_AXp_2dv` | none | yes | no | yes |
| V1071 | `mord_AXp_3dv` | none | yes | no | yes |
| V1072 | `mord_AXp_4dv` | none | yes | no | yes |
| V1073 | `mord_AXp_5dv` | none | yes | no | yes |
| V1074 | `mord_AXp_6dv` | none | yes | no | yes |
| V1075 | `mord_AXp_7dv` | none | yes | no | yes |
| V1076 | `mord_SZ` | none | yes | no | yes |
| V1077 | `mord_Sm` | none | yes | no | yes |
| V1078 | `mord_Sv` | none | yes | no | yes |
| V1079 | `mord_Sse` | none | yes | no | yes |
| V1080 | `mord_Spe` | none | yes | no | yes |
| V1081 | `mord_Sare` | none | yes | no | yes |
| V1082 | `mord_Sp` | none | yes | no | yes |
| V1083 | `mord_Si` | none | yes | no | yes |
| V1084 | `mord_MZ` | none | yes | no | yes |
| V1085 | `mord_Mm` | none | yes | no | yes |
| V1086 | `mord_Mv` | none | yes | no | yes |
| V1087 | `mord_Mse` | none | yes | no | yes |
| V1088 | `mord_Mpe` | none | yes | no | yes |
| V1089 | `mord_Mare` | none | yes | no | yes |
| V1090 | `mord_Mp` | none | yes | no | yes |
| V1091 | `mord_Mi` | none | yes | no | yes |
| V1124 | `mord_NssssN` | none | yes | no | yes |
| V1135 | `mord_NssPH` | none | yes | no | yes |
| V1171 | `mord_SsLi` | none | yes | no | yes |
| V1172 | `mord_SssBe` | none | yes | no | yes |
| V1173 | `mord_SssssBe` | none | yes | no | yes |
| V1174 | `mord_SssBH` | none | yes | no | yes |
| V1175 | `mord_SsssB` | none | yes | no | yes |
| V1176 | `mord_SssssB` | none | yes | no | yes |
| V1190 | `mord_SsNH3` | none | yes | no | yes |
| V1192 | `mord_SssNH2` | none | yes | no | yes |
| V1195 | `mord_SaaNH` | none | yes | no | yes |
| V1197 | `mord_SsssNH` | none | yes | no | yes |
| V1198 | `mord_SdsN` | none | yes | no | yes |
| V1201 | `mord_SddsN` | none | yes | no | yes |
| V1202 | `mord_SaasN` | none | yes | no | yes |
| V1203 | `mord_SssssN` | none | yes | no | yes |
| V1209 | `mord_SsSiH3` | none | yes | no | yes |
| V1210 | `mord_SssSiH2` | none | yes | no | yes |
| V1211 | `mord_SsssSiH` | none | yes | no | yes |
| V1212 | `mord_SssssSi` | none | yes | no | yes |
| V1213 | `mord_SsPH2` | none | yes | no | yes |
| V1214 | `mord_SssPH` | none | yes | no | yes |
| V1215 | `mord_SsssP` | none | yes | no | yes |
| V1216 | `mord_SdsssP` | none | yes | no | yes |
| V1217 | `mord_SsssssP` | none | yes | no | yes |
| V1222 | `mord_SdssS` | none | yes | no | yes |
| V1225 | `mord_SsGeH3` | none | yes | no | yes |
| V1226 | `mord_SssGeH2` | none | yes | no | yes |
| V1227 | `mord_SsssGeH` | none | yes | no | yes |
| V1228 | `mord_SssssGe` | none | yes | no | yes |
| V1229 | `mord_SsAsH2` | none | yes | no | yes |
| V1230 | `mord_SssAsH` | none | yes | no | yes |
| V1231 | `mord_SsssAs` | none | yes | no | yes |
| V1232 | `mord_SsssdAs` | none | yes | no | yes |
| V1233 | `mord_SsssssAs` | none | yes | no | yes |
| V1234 | `mord_SsSeH` | none | yes | no | yes |
| V1235 | `mord_SdSe` | none | yes | no | yes |
| V1236 | `mord_SssSe` | none | yes | no | yes |
| V1237 | `mord_SaaSe` | none | yes | no | yes |
| V1238 | `mord_SdssSe` | none | yes | no | yes |
| V1239 | `mord_SddssSe` | none | yes | no | yes |
| V1241 | `mord_SsSnH3` | none | yes | no | yes |
| V1242 | `mord_SssSnH2` | none | yes | no | yes |
| V1243 | `mord_SsssSnH` | none | yes | no | yes |
| V1244 | `mord_SssssSn` | none | yes | no | yes |
| V1246 | `mord_SsPbH3` | none | yes | no | yes |
| V1247 | `mord_SssPbH2` | none | yes | no | yes |
| V1248 | `mord_SsssPbH` | none | yes | no | yes |
| V1249 | `mord_SssssPb` | none | yes | no | yes |
| V1250 | `mord_MAXsLi` | none | yes | no | yes |
| V1251 | `mord_MAXssBe` | none | yes | no | yes |
| V1252 | `mord_MAXssssBe` | none | yes | no | yes |
| V1253 | `mord_MAXssBH` | none | yes | no | yes |
| V1254 | `mord_MAXsssB` | none | yes | no | yes |
| V1255 | `mord_MAXssssB` | none | yes | no | yes |
| V1256 | `mord_MAXsCH3` | none | yes | no | yes |
| V1257 | `mord_MAXdCH2` | none | yes | no | yes |
| V1258 | `mord_MAXssCH2` | none | yes | no | yes |
| V1259 | `mord_MAXtCH` | none | yes | no | yes |
| V1260 | `mord_MAXdsCH` | none | yes | no | yes |
| V1261 | `mord_MAXaaCH` | none | yes | no | yes |
| V1262 | `mord_MAXsssCH` | none | yes | no | yes |
| V1263 | `mord_MAXddC` | none | yes | no | yes |
| V1264 | `mord_MAXtsC` | none | yes | no | yes |
| V1265 | `mord_MAXdssC` | none | yes | no | yes |
| V1266 | `mord_MAXaasC` | none | yes | no | yes |
| V1267 | `mord_MAXaaaC` | none | yes | no | yes |
| V1268 | `mord_MAXssssC` | none | yes | no | yes |
| V1269 | `mord_MAXsNH3` | none | yes | no | yes |
| V1270 | `mord_MAXsNH2` | none | yes | no | yes |
| V1271 | `mord_MAXssNH2` | none | yes | no | yes |
| V1272 | `mord_MAXdNH` | none | yes | no | yes |
| V1273 | `mord_MAXssNH` | none | yes | no | yes |
| V1274 | `mord_MAXaaNH` | none | yes | no | yes |
| V1275 | `mord_MAXtN` | none | yes | no | yes |
| V1276 | `mord_MAXsssNH` | none | yes | no | yes |
| V1277 | `mord_MAXdsN` | none | yes | no | yes |
| V1278 | `mord_MAXaaN` | none | yes | no | yes |
| V1279 | `mord_MAXsssN` | none | yes | no | yes |
| V1280 | `mord_MAXddsN` | none | yes | no | yes |
| V1281 | `mord_MAXaasN` | none | yes | no | yes |
| V1282 | `mord_MAXssssN` | none | yes | no | yes |
| V1283 | `mord_MAXsOH` | none | yes | no | yes |
| V1284 | `mord_MAXdO` | none | yes | no | yes |
| V1285 | `mord_MAXssO` | none | yes | no | yes |
| V1286 | `mord_MAXaaO` | none | yes | no | yes |
| V1287 | `mord_MAXsF` | none | yes | no | yes |
| V1288 | `mord_MAXsSiH3` | none | yes | no | yes |
| V1289 | `mord_MAXssSiH2` | none | yes | no | yes |
| V1290 | `mord_MAXsssSiH` | none | yes | no | yes |
| V1291 | `mord_MAXssssSi` | none | yes | no | yes |
| V1292 | `mord_MAXsPH2` | none | yes | no | yes |
| V1293 | `mord_MAXssPH` | none | yes | no | yes |
| V1294 | `mord_MAXsssP` | none | yes | no | yes |
| V1295 | `mord_MAXdsssP` | none | yes | no | yes |
| V1296 | `mord_MAXsssssP` | none | yes | no | yes |
| V1297 | `mord_MAXsSH` | none | yes | no | yes |
| V1298 | `mord_MAXdS` | none | yes | no | yes |
| V1299 | `mord_MAXssS` | none | yes | no | yes |
| V1300 | `mord_MAXaaS` | none | yes | no | yes |
| V1301 | `mord_MAXdssS` | none | yes | no | yes |
| V1302 | `mord_MAXddssS` | none | yes | no | yes |
| V1303 | `mord_MAXsCl` | none | yes | no | yes |
| V1304 | `mord_MAXsGeH3` | none | yes | no | yes |
| V1305 | `mord_MAXssGeH2` | none | yes | no | yes |
| V1306 | `mord_MAXsssGeH` | none | yes | no | yes |
| V1307 | `mord_MAXssssGe` | none | yes | no | yes |
| V1308 | `mord_MAXsAsH2` | none | yes | no | yes |
| V1309 | `mord_MAXssAsH` | none | yes | no | yes |
| V1310 | `mord_MAXsssAs` | none | yes | no | yes |
| V1311 | `mord_MAXsssdAs` | none | yes | no | yes |
| V1312 | `mord_MAXsssssAs` | none | yes | no | yes |
| V1313 | `mord_MAXsSeH` | none | yes | no | yes |
| V1314 | `mord_MAXdSe` | none | yes | no | yes |
| V1315 | `mord_MAXssSe` | none | yes | no | yes |
| V1316 | `mord_MAXaaSe` | none | yes | no | yes |
| V1317 | `mord_MAXdssSe` | none | yes | no | yes |
| V1318 | `mord_MAXddssSe` | none | yes | no | yes |
| V1319 | `mord_MAXsBr` | none | yes | no | yes |
| V1320 | `mord_MAXsSnH3` | none | yes | no | yes |
| V1321 | `mord_MAXssSnH2` | none | yes | no | yes |
| V1322 | `mord_MAXsssSnH` | none | yes | no | yes |
| V1323 | `mord_MAXssssSn` | none | yes | no | yes |
| V1324 | `mord_MAXsI` | none | yes | no | yes |
| V1325 | `mord_MAXsPbH3` | none | yes | no | yes |
| V1326 | `mord_MAXssPbH2` | none | yes | no | yes |
| V1327 | `mord_MAXsssPbH` | none | yes | no | yes |
| V1328 | `mord_MAXssssPb` | none | yes | no | yes |
| V1329 | `mord_MINsLi` | none | yes | no | yes |
| V1330 | `mord_MINssBe` | none | yes | no | yes |
| V1331 | `mord_MINssssBe` | none | yes | no | yes |
| V1332 | `mord_MINssBH` | none | yes | no | yes |
| V1333 | `mord_MINsssB` | none | yes | no | yes |
| V1334 | `mord_MINssssB` | none | yes | no | yes |
| V1335 | `mord_MINsCH3` | none | yes | no | yes |
| V1336 | `mord_MINdCH2` | none | yes | no | yes |
| V1337 | `mord_MINssCH2` | none | yes | no | yes |
| V1338 | `mord_MINtCH` | none | yes | no | yes |
| V1339 | `mord_MINdsCH` | none | yes | no | yes |
| V1340 | `mord_MINaaCH` | none | yes | no | yes |
| V1341 | `mord_MINsssCH` | none | yes | no | yes |
| V1342 | `mord_MINddC` | none | yes | no | yes |
| V1343 | `mord_MINtsC` | none | yes | no | yes |
| V1344 | `mord_MINdssC` | none | yes | no | yes |
| V1345 | `mord_MINaasC` | none | yes | no | yes |
| V1346 | `mord_MINaaaC` | none | yes | no | yes |
| V1347 | `mord_MINssssC` | none | yes | no | yes |
| V1348 | `mord_MINsNH3` | none | yes | no | yes |
| V1349 | `mord_MINsNH2` | none | yes | no | yes |
| V1350 | `mord_MINssNH2` | none | yes | no | yes |
| V1351 | `mord_MINdNH` | none | yes | no | yes |
| V1352 | `mord_MINssNH` | none | yes | no | yes |
| V1353 | `mord_MINaaNH` | none | yes | no | yes |
| V1354 | `mord_MINtN` | none | yes | no | yes |
| V1355 | `mord_MINsssNH` | none | yes | no | yes |
| V1356 | `mord_MINdsN` | none | yes | no | yes |
| V1357 | `mord_MINaaN` | none | yes | no | yes |
| V1358 | `mord_MINsssN` | none | yes | no | yes |
| V1359 | `mord_MINddsN` | none | yes | no | yes |
| V1360 | `mord_MINaasN` | none | yes | no | yes |
| V1361 | `mord_MINssssN` | none | yes | no | yes |
| V1362 | `mord_MINsOH` | none | yes | no | yes |
| V1363 | `mord_MINdO` | none | yes | no | yes |
| V1364 | `mord_MINssO` | none | yes | no | yes |
| V1365 | `mord_MINaaO` | none | yes | no | yes |
| V1366 | `mord_MINsF` | none | yes | no | yes |
| V1367 | `mord_MINsSiH3` | none | yes | no | yes |
| V1368 | `mord_MINssSiH2` | none | yes | no | yes |
| V1369 | `mord_MINsssSiH` | none | yes | no | yes |
| V1370 | `mord_MINssssSi` | none | yes | no | yes |
| V1371 | `mord_MINsPH2` | none | yes | no | yes |
| V1372 | `mord_MINssPH` | none | yes | no | yes |
| V1373 | `mord_MINsssP` | none | yes | no | yes |
| V1374 | `mord_MINdsssP` | none | yes | no | yes |
| V1375 | `mord_MINsssssP` | none | yes | no | yes |
| V1376 | `mord_MINsSH` | none | yes | no | yes |
| V1377 | `mord_MINdS` | none | yes | no | yes |
| V1378 | `mord_MINssS` | none | yes | no | yes |
| V1379 | `mord_MINaaS` | none | yes | no | yes |
| V1380 | `mord_MINdssS` | none | yes | no | yes |
| V1381 | `mord_MINddssS` | none | yes | no | yes |
| V1382 | `mord_MINsCl` | none | yes | no | yes |
| V1383 | `mord_MINsGeH3` | none | yes | no | yes |
| V1384 | `mord_MINssGeH2` | none | yes | no | yes |
| V1385 | `mord_MINsssGeH` | none | yes | no | yes |
| V1386 | `mord_MINssssGe` | none | yes | no | yes |
| V1387 | `mord_MINsAsH2` | none | yes | no | yes |
| V1388 | `mord_MINssAsH` | none | yes | no | yes |
| V1389 | `mord_MINsssAs` | none | yes | no | yes |
| V1390 | `mord_MINsssdAs` | none | yes | no | yes |
| V1391 | `mord_MINsssssAs` | none | yes | no | yes |
| V1392 | `mord_MINsSeH` | none | yes | no | yes |
| V1393 | `mord_MINdSe` | none | yes | no | yes |
| V1394 | `mord_MINssSe` | none | yes | no | yes |
| V1395 | `mord_MINaaSe` | none | yes | no | yes |
| V1396 | `mord_MINdssSe` | none | yes | no | yes |
| V1397 | `mord_MINddssSe` | none | yes | no | yes |
| V1398 | `mord_MINsBr` | none | yes | no | yes |
| V1399 | `mord_MINsSnH3` | none | yes | no | yes |
| V1400 | `mord_MINssSnH2` | none | yes | no | yes |
| V1401 | `mord_MINsssSnH` | none | yes | no | yes |
| V1402 | `mord_MINssssSn` | none | yes | no | yes |
| V1403 | `mord_MINsI` | none | yes | no | yes |
| V1404 | `mord_MINsPbH3` | none | yes | no | yes |
| V1405 | `mord_MINssPbH2` | none | yes | no | yes |
| V1406 | `mord_MINsssPbH` | none | yes | no | yes |
| V1407 | `mord_MINssssPb` | none | yes | no | yes |
| V1408 | `mord_ECIndex` | none | yes | no | yes |
| V1409 | `mord_ETA_alpha` | none | yes | no | yes |
| V1410 | `mord_AETA_alpha` | none | yes | no | yes |
| V1411 | `mord_ETA_shape_p` | none | yes | no | yes |
| V1412 | `mord_ETA_shape_y` | none | yes | no | yes |
| V1413 | `mord_ETA_shape_x` | none | yes | no | yes |
| V1414 | `mord_ETA_beta` | none | yes | no | yes |
| V1415 | `mord_AETA_beta` | none | yes | no | yes |
| V1416 | `mord_ETA_beta_s` | none | yes | no | yes |
| V1417 | `mord_AETA_beta_s` | none | yes | no | yes |
| V1418 | `mord_ETA_beta_ns` | none | yes | no | yes |
| V1419 | `mord_AETA_beta_ns` | none | yes | no | yes |
| V1420 | `mord_ETA_beta_ns_d` | none | yes | no | yes |
| V1421 | `mord_AETA_beta_ns_d` | none | yes | no | yes |
| V1422 | `mord_ETA_eta` | none | yes | no | yes |
| V1423 | `mord_AETA_eta` | none | yes | no | yes |
| V1424 | `mord_ETA_eta_L` | none | yes | no | yes |
| V1425 | `mord_AETA_eta_L` | none | yes | no | yes |
| V1426 | `mord_ETA_eta_R` | none | yes | no | yes |
| V1427 | `mord_AETA_eta_R` | none | yes | no | yes |
| V1428 | `mord_ETA_eta_RL` | none | yes | no | yes |
| V1429 | `mord_AETA_eta_RL` | none | yes | no | yes |
| V1430 | `mord_ETA_eta_F` | none | yes | no | yes |
| V1431 | `mord_AETA_eta_F` | none | yes | no | yes |
| V1432 | `mord_ETA_eta_FL` | none | yes | no | yes |
| V1433 | `mord_AETA_eta_FL` | none | yes | no | yes |
| V1434 | `mord_ETA_eta_B` | none | yes | no | yes |
| V1435 | `mord_AETA_eta_B` | none | yes | no | yes |
| V1436 | `mord_ETA_eta_BR` | none | yes | no | yes |
| V1437 | `mord_AETA_eta_BR` | none | yes | no | yes |
| V1438 | `mord_ETA_dAlpha_A` | none | yes | no | yes |
| V1439 | `mord_ETA_dAlpha_B` | none | yes | no | yes |
| V1440 | `mord_ETA_epsilon_1` | none | yes | no | yes |
| V1441 | `mord_ETA_epsilon_2` | none | yes | no | yes |
| V1442 | `mord_ETA_epsilon_3` | none | yes | no | yes |
| V1443 | `mord_ETA_epsilon_4` | none | yes | no | yes |
| V1444 | `mord_ETA_epsilon_5` | none | yes | no | yes |
| V1445 | `mord_ETA_dEpsilon_A` | none | yes | no | yes |
| V1446 | `mord_ETA_dEpsilon_B` | none | yes | no | yes |
| V1447 | `mord_ETA_dEpsilon_C` | none | yes | no | yes |
| V1448 | `mord_ETA_dEpsilon_D` | none | yes | no | yes |
| V1449 | `mord_ETA_dBeta` | none | yes | no | yes |
| V1450 | `mord_AETA_dBeta` | none | yes | no | yes |
| V1451 | `mord_ETA_psi_1` | none | yes | no | yes |
| V1452 | `mord_ETA_dPsi_A` | none | yes | no | yes |
| V1453 | `mord_ETA_dPsi_B` | none | yes | no | yes |
| V1454 | `mord_fragCpx` | none | yes | no | yes |
| V1455 | `mord_fMF` | none | yes | no | yes |
| V1505 | `mord_FilterItLogS` | none | yes | no | yes |
| V1560 | `mord_MDEC_11` | none | yes | no | yes |
| V1561 | `mord_MDEC_12` | none | yes | no | yes |
| V1562 | `mord_MDEC_13` | none | yes | no | yes |
| V1563 | `mord_MDEC_14` | none | yes | no | yes |
| V1564 | `mord_MDEC_22` | none | yes | no | yes |
| V1565 | `mord_MDEC_23` | none | yes | no | yes |
| V1566 | `mord_MDEC_24` | none | yes | no | yes |
| V1567 | `mord_MDEC_33` | none | yes | no | yes |
| V1568 | `mord_MDEC_34` | none | yes | no | yes |
| V1569 | `mord_MDEC_44` | none | yes | no | yes |
| V1570 | `mord_MDEO_11` | none | yes | no | yes |
| V1571 | `mord_MDEO_12` | none | yes | no | yes |
| V1572 | `mord_MDEO_22` | none | yes | no | yes |
| V1573 | `mord_MDEN_11` | none | yes | no | yes |
| V1574 | `mord_MDEN_12` | none | yes | no | yes |
| V1575 | `mord_MDEN_13` | none | yes | no | yes |
| V1576 | `mord_MDEN_22` | none | yes | no | yes |
| V1577 | `mord_MDEN_23` | none | yes | no | yes |
| V1578 | `mord_MDEN_33` | none | yes | no | yes |
| V1603 | `mord_n3Ring` | none | yes | no | yes |
| V1604 | `mord_n4Ring` | none | yes | no | yes |
| V1605 | `mord_n5Ring` | none | yes | no | yes |
| V1606 | `mord_n6Ring` | none | yes | no | yes |
| V1607 | `mord_n7Ring` | none | yes | no | yes |
| V1608 | `mord_n8Ring` | none | yes | no | yes |
| V1609 | `mord_n9Ring` | none | yes | no | yes |
| V1610 | `mord_n10Ring` | none | yes | no | yes |
| V1611 | `mord_n11Ring` | none | yes | no | yes |
| V1612 | `mord_n12Ring` | none | yes | no | yes |
| V1615 | `mord_n3HRing` | none | yes | no | yes |
| V1616 | `mord_n4HRing` | none | yes | no | yes |
| V1617 | `mord_n5HRing` | none | yes | no | yes |
| V1618 | `mord_n6HRing` | none | yes | no | yes |
| V1619 | `mord_n7HRing` | none | yes | no | yes |
| V1620 | `mord_n8HRing` | none | yes | no | yes |
| V1621 | `mord_n9HRing` | none | yes | no | yes |
| V1622 | `mord_n10HRing` | none | yes | no | yes |
| V1623 | `mord_n11HRing` | none | yes | no | yes |
| V1624 | `mord_n12HRing` | none | yes | no | yes |
| V1627 | `mord_n3aRing` | none | yes | no | yes |
| V1628 | `mord_n4aRing` | none | yes | no | yes |
| V1629 | `mord_n5aRing` | none | yes | no | yes |
| V1630 | `mord_n6aRing` | none | yes | no | yes |
| V1631 | `mord_n7aRing` | none | yes | no | yes |
| V1632 | `mord_n8aRing` | none | yes | no | yes |
| V1633 | `mord_n9aRing` | none | yes | no | yes |
| V1634 | `mord_n10aRing` | none | yes | no | yes |
| V1635 | `mord_n11aRing` | none | yes | no | yes |
| V1636 | `mord_n12aRing` | none | yes | no | yes |
| V1639 | `mord_n3aHRing` | none | yes | no | yes |
| V1640 | `mord_n4aHRing` | none | yes | no | yes |
| V1641 | `mord_n5aHRing` | none | yes | no | yes |
| V1642 | `mord_n6aHRing` | none | yes | no | yes |
| V1643 | `mord_n7aHRing` | none | yes | no | yes |
| V1644 | `mord_n8aHRing` | none | yes | no | yes |
| V1645 | `mord_n9aHRing` | none | yes | no | yes |
| V1646 | `mord_n10aHRing` | none | yes | no | yes |
| V1647 | `mord_n11aHRing` | none | yes | no | yes |
| V1648 | `mord_n12aHRing` | none | yes | no | yes |
| V1651 | `mord_n3ARing` | none | yes | no | yes |
| V1652 | `mord_n4ARing` | none | yes | no | yes |
| V1653 | `mord_n5ARing` | none | yes | no | yes |
| V1654 | `mord_n6ARing` | none | yes | no | yes |
| V1655 | `mord_n7ARing` | none | yes | no | yes |
| V1656 | `mord_n8ARing` | none | yes | no | yes |
| V1657 | `mord_n9ARing` | none | yes | no | yes |
| V1658 | `mord_n10ARing` | none | yes | no | yes |
| V1659 | `mord_n11ARing` | none | yes | no | yes |
| V1660 | `mord_n12ARing` | none | yes | no | yes |
| V1663 | `mord_n3AHRing` | none | yes | no | yes |
| V1664 | `mord_n4AHRing` | none | yes | no | yes |
| V1665 | `mord_n5AHRing` | none | yes | no | yes |
| V1666 | `mord_n6AHRing` | none | yes | no | yes |
| V1667 | `mord_n7AHRing` | none | yes | no | yes |
| V1668 | `mord_n8AHRing` | none | yes | no | yes |
| V1669 | `mord_n9AHRing` | none | yes | no | yes |
| V1670 | `mord_n10AHRing` | none | yes | no | yes |
| V1671 | `mord_n11AHRing` | none | yes | no | yes |
| V1672 | `mord_n12AHRing` | none | yes | no | yes |
| V1675 | `mord_n4FRing` | none | yes | no | yes |
| V1676 | `mord_n5FRing` | none | yes | no | yes |
| V1677 | `mord_n6FRing` | none | yes | no | yes |
| V1678 | `mord_n7FRing` | none | yes | no | yes |
| V1679 | `mord_n8FRing` | none | yes | no | yes |
| V1680 | `mord_n9FRing` | none | yes | no | yes |
| V1681 | `mord_n10FRing` | none | yes | no | yes |
| V1682 | `mord_n11FRing` | none | yes | no | yes |
| V1683 | `mord_n12FRing` | none | yes | no | yes |
| V1686 | `mord_n4FHRing` | none | yes | no | yes |
| V1687 | `mord_n5FHRing` | none | yes | no | yes |
| V1688 | `mord_n6FHRing` | none | yes | no | yes |
| V1689 | `mord_n7FHRing` | none | yes | no | yes |
| V1690 | `mord_n8FHRing` | none | yes | no | yes |
| V1691 | `mord_n9FHRing` | none | yes | no | yes |
| V1692 | `mord_n10FHRing` | none | yes | no | yes |
| V1693 | `mord_n11FHRing` | none | yes | no | yes |
| V1694 | `mord_n12FHRing` | none | yes | no | yes |
| V1697 | `mord_n4FaRing` | none | yes | no | yes |
| V1698 | `mord_n5FaRing` | none | yes | no | yes |
| V1699 | `mord_n6FaRing` | none | yes | no | yes |
| V1700 | `mord_n7FaRing` | none | yes | no | yes |
| V1701 | `mord_n8FaRing` | none | yes | no | yes |
| V1702 | `mord_n9FaRing` | none | yes | no | yes |
| V1703 | `mord_n10FaRing` | none | yes | no | yes |
| V1704 | `mord_n11FaRing` | none | yes | no | yes |
| V1705 | `mord_n12FaRing` | none | yes | no | yes |
| V1708 | `mord_n4FaHRing` | none | yes | no | yes |
| V1709 | `mord_n5FaHRing` | none | yes | no | yes |
| V1710 | `mord_n6FaHRing` | none | yes | no | yes |
| V1711 | `mord_n7FaHRing` | none | yes | no | yes |
| V1712 | `mord_n8FaHRing` | none | yes | no | yes |
| V1713 | `mord_n9FaHRing` | none | yes | no | yes |
| V1714 | `mord_n10FaHRing` | none | yes | no | yes |
| V1715 | `mord_n11FaHRing` | none | yes | no | yes |
| V1716 | `mord_n12FaHRing` | none | yes | no | yes |
| V1719 | `mord_n4FARing` | none | yes | no | yes |
| V1720 | `mord_n5FARing` | none | yes | no | yes |
| V1721 | `mord_n6FARing` | none | yes | no | yes |
| V1722 | `mord_n7FARing` | none | yes | no | yes |
| V1723 | `mord_n8FARing` | none | yes | no | yes |
| V1724 | `mord_n9FARing` | none | yes | no | yes |
| V1725 | `mord_n10FARing` | none | yes | no | yes |
| V1726 | `mord_n11FARing` | none | yes | no | yes |
| V1727 | `mord_n12FARing` | none | yes | no | yes |
| V1730 | `mord_n4FAHRing` | none | yes | no | yes |
| V1731 | `mord_n5FAHRing` | none | yes | no | yes |
| V1732 | `mord_n6FAHRing` | none | yes | no | yes |
| V1733 | `mord_n7FAHRing` | none | yes | no | yes |
| V1734 | `mord_n8FAHRing` | none | yes | no | yes |
| V1735 | `mord_n9FAHRing` | none | yes | no | yes |
| V1736 | `mord_n10FAHRing` | none | yes | no | yes |
| V1737 | `mord_n11FAHRing` | none | yes | no | yes |
| V1738 | `mord_n12FAHRing` | none | yes | no | yes |
| V1741 | `mord_RotRatio` | none | yes | no | yes |

### 77 variables in `public.descriptors.values_2d (JSONB key)`: E-State atom-type count: how many atoms of one electrotopological atom type the molecule h

E-State atom-type count: how many atoms of one electrotopological atom type the molecule has. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1092 | `mord_NsLi` | none | yes | no | yes |
| V1093 | `mord_NssBe` | none | yes | no | yes |
| V1094 | `mord_NssssBe` | none | yes | no | yes |
| V1095 | `mord_NssBH` | none | yes | no | yes |
| V1096 | `mord_NsssB` | none | yes | no | yes |
| V1097 | `mord_NssssB` | none | yes | no | yes |
| V1098 | `mord_NsCH3` | none | yes | no | yes |
| V1099 | `mord_NdCH2` | none | yes | no | yes |
| V1100 | `mord_NssCH2` | none | yes | no | yes |
| V1101 | `mord_NtCH` | none | yes | no | yes |
| V1102 | `mord_NdsCH` | none | yes | no | yes |
| V1103 | `mord_NaaCH` | none | yes | no | yes |
| V1104 | `mord_NsssCH` | none | yes | no | yes |
| V1105 | `mord_NddC` | none | yes | no | yes |
| V1106 | `mord_NtsC` | none | yes | no | yes |
| V1107 | `mord_NdssC` | none | yes | no | yes |
| V1108 | `mord_NaasC` | none | yes | no | yes |
| V1109 | `mord_NaaaC` | none | yes | no | yes |
| V1110 | `mord_NssssC` | none | yes | no | yes |
| V1111 | `mord_NsNH3` | none | yes | no | yes |
| V1112 | `mord_NsNH2` | none | yes | no | yes |
| V1113 | `mord_NssNH2` | none | yes | no | yes |
| V1114 | `mord_NdNH` | none | yes | no | yes |
| V1115 | `mord_NssNH` | none | yes | no | yes |
| V1116 | `mord_NaaNH` | none | yes | no | yes |
| V1117 | `mord_NtN` | none | yes | no | yes |
| V1118 | `mord_NsssNH` | none | yes | no | yes |
| V1119 | `mord_NdsN` | none | yes | no | yes |
| V1120 | `mord_NaaN` | none | yes | no | yes |
| V1121 | `mord_NsssN` | none | yes | no | yes |
| V1122 | `mord_NddsN` | none | yes | no | yes |
| V1123 | `mord_NaasN` | none | yes | no | yes |
| V1125 | `mord_NsOH` | none | yes | no | yes |
| V1126 | `mord_NdO` | none | yes | no | yes |
| V1127 | `mord_NssO` | none | yes | no | yes |
| V1128 | `mord_NaaO` | none | yes | no | yes |
| V1129 | `mord_NsF` | none | yes | no | yes |
| V1130 | `mord_NsSiH3` | none | yes | no | yes |
| V1131 | `mord_NssSiH2` | none | yes | no | yes |
| V1132 | `mord_NsssSiH` | none | yes | no | yes |
| V1133 | `mord_NssssSi` | none | yes | no | yes |
| V1134 | `mord_NsPH2` | none | yes | no | yes |
| V1136 | `mord_NsssP` | none | yes | no | yes |
| V1137 | `mord_NdsssP` | none | yes | no | yes |
| V1138 | `mord_NsssssP` | none | yes | no | yes |
| V1139 | `mord_NsSH` | none | yes | no | yes |
| V1140 | `mord_NdS` | none | yes | no | yes |
| V1141 | `mord_NssS` | none | yes | no | yes |
| V1142 | `mord_NaaS` | none | yes | no | yes |
| V1143 | `mord_NdssS` | none | yes | no | yes |
| V1144 | `mord_NddssS` | none | yes | no | yes |
| V1145 | `mord_NsCl` | none | yes | no | yes |
| V1146 | `mord_NsGeH3` | none | yes | no | yes |
| V1147 | `mord_NssGeH2` | none | yes | no | yes |
| V1148 | `mord_NsssGeH` | none | yes | no | yes |
| V1149 | `mord_NssssGe` | none | yes | no | yes |
| V1150 | `mord_NsAsH2` | none | yes | no | yes |
| V1151 | `mord_NssAsH` | none | yes | no | yes |
| V1152 | `mord_NsssAs` | none | yes | no | yes |
| V1153 | `mord_NsssdAs` | none | yes | no | yes |
| V1154 | `mord_NsssssAs` | none | yes | no | yes |
| V1155 | `mord_NsSeH` | none | yes | no | yes |
| V1156 | `mord_NdSe` | none | yes | no | yes |
| V1157 | `mord_NssSe` | none | yes | no | yes |
| V1158 | `mord_NaaSe` | none | yes | no | yes |
| V1159 | `mord_NdssSe` | none | yes | no | yes |
| V1160 | `mord_NddssSe` | none | yes | no | yes |
| V1161 | `mord_NsBr` | none | yes | no | yes |
| V1162 | `mord_NsSnH3` | none | yes | no | yes |
| V1163 | `mord_NssSnH2` | none | yes | no | yes |
| V1164 | `mord_NsssSnH` | none | yes | no | yes |
| V1165 | `mord_NssssSn` | none | yes | no | yes |
| V1166 | `mord_NsI` | none | yes | no | yes |
| V1167 | `mord_NsPbH3` | none | yes | no | yes |
| V1168 | `mord_NssPbH2` | none | yes | no | yes |
| V1169 | `mord_NsssPbH` | none | yes | no | yes |
| V1170 | `mord_NssssPb` | none | yes | no | yes |

### 32 variables in `public.descriptors.values_2d (JSONB key)`: E-State atom-type sum: sum of the electrotopological state of the atoms of one atom type

E-State atom-type sum: sum of the electrotopological state of the atoms of one atom type. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1177 | `mord_SsCH3` | none | yes | no | yes |
| V1178 | `mord_SdCH2` | none | yes | no | yes |
| V1179 | `mord_SssCH2` | none | yes | no | yes |
| V1180 | `mord_StCH` | none | yes | no | yes |
| V1181 | `mord_SdsCH` | none | yes | no | yes |
| V1182 | `mord_SaaCH` | none | yes | no | yes |
| V1183 | `mord_SsssCH` | none | yes | no | yes |
| V1184 | `mord_SddC` | none | yes | no | yes |
| V1185 | `mord_StsC` | none | yes | no | yes |
| V1186 | `mord_SdssC` | none | yes | no | yes |
| V1187 | `mord_SaasC` | none | yes | no | yes |
| V1188 | `mord_SaaaC` | none | yes | no | yes |
| V1189 | `mord_SssssC` | none | yes | no | yes |
| V1191 | `mord_SsNH2` | none | yes | no | yes |
| V1193 | `mord_SdNH` | none | yes | no | yes |
| V1194 | `mord_SssNH` | none | yes | no | yes |
| V1196 | `mord_StN` | none | yes | no | yes |
| V1199 | `mord_SaaN` | none | yes | no | yes |
| V1200 | `mord_SsssN` | none | yes | no | yes |
| V1204 | `mord_SsOH` | none | yes | no | yes |
| V1205 | `mord_SdO` | none | yes | no | yes |
| V1206 | `mord_SssO` | none | yes | no | yes |
| V1207 | `mord_SaaO` | none | yes | no | yes |
| V1208 | `mord_SsF` | none | yes | no | yes |
| V1218 | `mord_SsSH` | none | yes | no | yes |
| V1219 | `mord_SdS` | none | yes | no | yes |
| V1220 | `mord_SssS` | none | yes | no | yes |
| V1221 | `mord_SaaS` | none | yes | no | yes |
| V1223 | `mord_SddssS` | none | yes | no | yes |
| V1224 | `mord_SsCl` | none | yes | no | yes |
| V1240 | `mord_SsBr` | none | yes | no | yes |
| V1245 | `mord_SsI` | none | yes | no | yes |

### 42 variables in `public.descriptors.values_2d (JSONB key)`: Information-content descriptor of a given neighbourhood order

Information-content descriptor of a given neighbourhood order. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1458 | `mord_IC0` | none | yes | no | yes |
| V1459 | `mord_IC1` | none | yes | no | yes |
| V1460 | `mord_IC2` | none | yes | no | yes |
| V1461 | `mord_IC3` | none | yes | no | yes |
| V1462 | `mord_IC4` | none | yes | no | yes |
| V1463 | `mord_IC5` | none | yes | no | yes |
| V1464 | `mord_TIC0` | none | yes | no | yes |
| V1465 | `mord_TIC1` | none | yes | no | yes |
| V1466 | `mord_TIC2` | none | yes | no | yes |
| V1467 | `mord_TIC3` | none | yes | no | yes |
| V1468 | `mord_TIC4` | none | yes | no | yes |
| V1469 | `mord_TIC5` | none | yes | no | yes |
| V1470 | `mord_SIC0` | none | yes | no | yes |
| V1471 | `mord_SIC1` | none | yes | no | yes |
| V1472 | `mord_SIC2` | none | yes | no | yes |
| V1473 | `mord_SIC3` | none | yes | no | yes |
| V1474 | `mord_SIC4` | none | yes | no | yes |
| V1475 | `mord_SIC5` | none | yes | no | yes |
| V1476 | `mord_BIC0` | none | yes | no | yes |
| V1477 | `mord_BIC1` | none | yes | no | yes |
| V1478 | `mord_BIC2` | none | yes | no | yes |
| V1479 | `mord_BIC3` | none | yes | no | yes |
| V1480 | `mord_BIC4` | none | yes | no | yes |
| V1481 | `mord_BIC5` | none | yes | no | yes |
| V1482 | `mord_CIC0` | none | yes | no | yes |
| V1483 | `mord_CIC1` | none | yes | no | yes |
| V1484 | `mord_CIC2` | none | yes | no | yes |
| V1485 | `mord_CIC3` | none | yes | no | yes |
| V1486 | `mord_CIC4` | none | yes | no | yes |
| V1487 | `mord_CIC5` | none | yes | no | yes |
| V1488 | `mord_MIC0` | none | yes | no | yes |
| V1489 | `mord_MIC1` | none | yes | no | yes |
| V1490 | `mord_MIC2` | none | yes | no | yes |
| V1491 | `mord_MIC3` | none | yes | no | yes |
| V1492 | `mord_MIC4` | none | yes | no | yes |
| V1493 | `mord_MIC5` | none | yes | no | yes |
| V1494 | `mord_ZMIC0` | none | yes | no | yes |
| V1495 | `mord_ZMIC1` | none | yes | no | yes |
| V1496 | `mord_ZMIC2` | none | yes | no | yes |
| V1497 | `mord_ZMIC3` | none | yes | no | yes |
| V1498 | `mord_ZMIC4` | none | yes | no | yes |
| V1499 | `mord_ZMIC5` | none | yes | no | yes |

### 3 variables in `public.descriptors.values_2d (JSONB key)`: Kier shape index

Kier shape index. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1500 | `mord_Kier1` | none | yes | no | yes |
| V1501 | `mord_Kier2` | none | yes | no | yes |
| V1502 | `mord_Kier3` | none | yes | no | yes |

### 2 variables in `public.descriptors.values_2d (JSONB key)`: Mordred implementation of a drug-likeness filter, as a flag

Mordred implementation of a drug-likeness filter, as a flag. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1503 | `mord_Lipinski` | none | yes | no | yes |
| V1504 | `mord_GhoseFilter` | none | yes | no | yes |

### 11 variables in `public.descriptors.values_2d (JSONB key)`: Whole-molecule physico-chemical estimate

Whole-molecule physico-chemical estimate. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1506 | `mord_VMcGowan` | none | yes | no | yes |
| V1507 | `mord_LabuteASA` | none | yes | no | yes |
| V1600 | `mord_apol` | none | yes | no | yes |
| V1601 | `mord_bpol` | none | yes | no | yes |
| V1742 | `mord_SLogP` | none | yes | no | yes |
| V1743 | `mord_SMR` | none | yes | no | yes |
| V1744 | `mord_TopoPSA_NO_` | none | yes | no | yes |
| V1745 | `mord_TopoPSA` | none | yes | no | yes |
| V1771 | `mord_Vabc` | none | yes | no | yes |
| V1794 | `mord_MW` | none | yes | no | yes |
| V1795 | `mord_AMW` | none | yes | no | yes |

### 52 variables in `public.descriptors.values_2d (JSONB key)`: Surface-area descriptor: van der Waals surface area in a bin of a partial-charge, molar-re

Surface-area descriptor: van der Waals surface area in a bin of a partial-charge, molar-refractivity, logP or E-State property. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1508 | `mord_PEOE_VSA1` | none | yes | no | yes |
| V1509 | `mord_PEOE_VSA2` | none | yes | no | yes |
| V1510 | `mord_PEOE_VSA3` | none | yes | no | yes |
| V1511 | `mord_PEOE_VSA4` | none | yes | no | yes |
| V1512 | `mord_PEOE_VSA5` | none | yes | no | yes |
| V1513 | `mord_PEOE_VSA6` | none | yes | no | yes |
| V1514 | `mord_PEOE_VSA7` | none | yes | no | yes |
| V1515 | `mord_PEOE_VSA8` | none | yes | no | yes |
| V1516 | `mord_PEOE_VSA9` | none | yes | no | yes |
| V1517 | `mord_PEOE_VSA10` | none | yes | no | yes |
| V1518 | `mord_PEOE_VSA11` | none | yes | no | yes |
| V1519 | `mord_PEOE_VSA12` | none | yes | no | yes |
| V1520 | `mord_PEOE_VSA13` | none | yes | no | yes |
| V1521 | `mord_SMR_VSA1` | none | yes | no | yes |
| V1522 | `mord_SMR_VSA2` | none | yes | no | yes |
| V1523 | `mord_SMR_VSA3` | none | yes | no | yes |
| V1524 | `mord_SMR_VSA4` | none | yes | no | yes |
| V1525 | `mord_SMR_VSA5` | none | yes | no | yes |
| V1526 | `mord_SMR_VSA6` | none | yes | no | yes |
| V1527 | `mord_SMR_VSA7` | none | yes | no | yes |
| V1528 | `mord_SMR_VSA8` | none | yes | no | yes |
| V1529 | `mord_SMR_VSA9` | none | yes | no | yes |
| V1530 | `mord_SlogP_VSA1` | none | yes | no | yes |
| V1531 | `mord_SlogP_VSA2` | none | yes | no | yes |
| V1532 | `mord_SlogP_VSA3` | none | yes | no | yes |
| V1533 | `mord_SlogP_VSA4` | none | yes | no | yes |
| V1534 | `mord_SlogP_VSA5` | none | yes | no | yes |
| V1535 | `mord_SlogP_VSA6` | none | yes | no | yes |
| V1536 | `mord_SlogP_VSA7` | none | yes | no | yes |
| V1537 | `mord_SlogP_VSA8` | none | yes | no | yes |
| V1538 | `mord_SlogP_VSA9` | none | yes | no | yes |
| V1539 | `mord_SlogP_VSA10` | none | yes | no | yes |
| V1540 | `mord_SlogP_VSA11` | none | yes | no | yes |
| V1541 | `mord_EState_VSA1` | none | yes | no | yes |
| V1542 | `mord_EState_VSA2` | none | yes | no | yes |
| V1543 | `mord_EState_VSA3` | none | yes | no | yes |
| V1544 | `mord_EState_VSA4` | none | yes | no | yes |
| V1545 | `mord_EState_VSA5` | none | yes | no | yes |
| V1546 | `mord_EState_VSA6` | none | yes | no | yes |
| V1547 | `mord_EState_VSA7` | none | yes | no | yes |
| V1548 | `mord_EState_VSA8` | none | yes | no | yes |
| V1549 | `mord_EState_VSA9` | none | yes | no | yes |
| V1550 | `mord_EState_VSA10` | none | yes | no | yes |
| V1551 | `mord_VSA_EState1` | none | yes | no | yes |
| V1552 | `mord_VSA_EState2` | none | yes | no | yes |
| V1553 | `mord_VSA_EState3` | none | yes | no | yes |
| V1554 | `mord_VSA_EState4` | none | yes | no | yes |
| V1555 | `mord_VSA_EState5` | none | yes | no | yes |
| V1556 | `mord_VSA_EState6` | none | yes | no | yes |
| V1557 | `mord_VSA_EState7` | none | yes | no | yes |
| V1558 | `mord_VSA_EState8` | none | yes | no | yes |
| V1559 | `mord_VSA_EState9` | none | yes | no | yes |

### 21 variables in `public.descriptors.values_2d (JSONB key)`: Path-count descriptor of a given length

Path-count descriptor of a given length. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1579 | `mord_MPC2` | none | yes | no | yes |
| V1580 | `mord_MPC3` | none | yes | no | yes |
| V1581 | `mord_MPC4` | none | yes | no | yes |
| V1582 | `mord_MPC5` | none | yes | no | yes |
| V1583 | `mord_MPC6` | none | yes | no | yes |
| V1584 | `mord_MPC7` | none | yes | no | yes |
| V1585 | `mord_MPC8` | none | yes | no | yes |
| V1586 | `mord_MPC9` | none | yes | no | yes |
| V1587 | `mord_MPC10` | none | yes | no | yes |
| V1588 | `mord_TMPC10` | none | yes | no | yes |
| V1589 | `mord_piPC1` | none | yes | no | yes |
| V1590 | `mord_piPC2` | none | yes | no | yes |
| V1591 | `mord_piPC3` | none | yes | no | yes |
| V1592 | `mord_piPC4` | none | yes | no | yes |
| V1593 | `mord_piPC5` | none | yes | no | yes |
| V1594 | `mord_piPC6` | none | yes | no | yes |
| V1595 | `mord_piPC7` | none | yes | no | yes |
| V1596 | `mord_piPC8` | none | yes | no | yes |
| V1597 | `mord_piPC9` | none | yes | no | yes |
| V1598 | `mord_piPC10` | none | yes | no | yes |
| V1599 | `mord_TpiPC10` | none | yes | no | yes |

### 24 variables in `public.descriptors.values_2d (JSONB key)`: Count of rings of a given size, fusion or composition

Count of rings of a given size, fusion or composition. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1602 | `mord_nRing` | none | yes | no | yes |
| V1613 | `mord_nG12Ring` | none | yes | no | yes |
| V1614 | `mord_nHRing` | none | yes | no | yes |
| V1625 | `mord_nG12HRing` | none | yes | no | yes |
| V1626 | `mord_naRing` | none | yes | no | yes |
| V1637 | `mord_nG12aRing` | none | yes | no | yes |
| V1638 | `mord_naHRing` | none | yes | no | yes |
| V1649 | `mord_nG12aHRing` | none | yes | no | yes |
| V1650 | `mord_nARing` | none | yes | no | yes |
| V1661 | `mord_nG12ARing` | none | yes | no | yes |
| V1662 | `mord_nAHRing` | none | yes | no | yes |
| V1673 | `mord_nG12AHRing` | none | yes | no | yes |
| V1674 | `mord_nFRing` | none | yes | no | yes |
| V1684 | `mord_nG12FRing` | none | yes | no | yes |
| V1685 | `mord_nFHRing` | none | yes | no | yes |
| V1695 | `mord_nG12FHRing` | none | yes | no | yes |
| V1696 | `mord_nFaRing` | none | yes | no | yes |
| V1706 | `mord_nG12FaRing` | none | yes | no | yes |
| V1707 | `mord_nFaHRing` | none | yes | no | yes |
| V1717 | `mord_nG12FaHRing` | none | yes | no | yes |
| V1718 | `mord_nFARing` | none | yes | no | yes |
| V1728 | `mord_nG12FARing` | none | yes | no | yes |
| V1729 | `mord_nFAHRing` | none | yes | no | yes |
| V1739 | `mord_nG12FAHRing` | none | yes | no | yes |

### 21 variables in `public.descriptors.values_2d (JSONB key)`: Topological charge descriptor (Galvez charge-index family) of a given order

Topological charge descriptor (Galvez charge-index family) of a given order. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1746 | `mord_GGI1` | none | yes | no | yes |
| V1747 | `mord_GGI2` | none | yes | no | yes |
| V1748 | `mord_GGI3` | none | yes | no | yes |
| V1749 | `mord_GGI4` | none | yes | no | yes |
| V1750 | `mord_GGI5` | none | yes | no | yes |
| V1751 | `mord_GGI6` | none | yes | no | yes |
| V1752 | `mord_GGI7` | none | yes | no | yes |
| V1753 | `mord_GGI8` | none | yes | no | yes |
| V1754 | `mord_GGI9` | none | yes | no | yes |
| V1755 | `mord_GGI10` | none | yes | no | yes |
| V1756 | `mord_JGI1` | none | yes | no | yes |
| V1757 | `mord_JGI2` | none | yes | no | yes |
| V1758 | `mord_JGI3` | none | yes | no | yes |
| V1759 | `mord_JGI4` | none | yes | no | yes |
| V1760 | `mord_JGI5` | none | yes | no | yes |
| V1761 | `mord_JGI6` | none | yes | no | yes |
| V1762 | `mord_JGI7` | none | yes | no | yes |
| V1763 | `mord_JGI8` | none | yes | no | yes |
| V1764 | `mord_JGI9` | none | yes | no | yes |
| V1765 | `mord_JGI10` | none | yes | no | yes |
| V1766 | `mord_JGT10` | none | yes | no | yes |

### 21 variables in `public.descriptors.values_2d (JSONB key)`: Walk-count descriptor of a given length

Walk-count descriptor of a given length. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1773 | `mord_MWC01` | none | yes | no | yes |
| V1774 | `mord_MWC02` | none | yes | no | yes |
| V1775 | `mord_MWC03` | none | yes | no | yes |
| V1776 | `mord_MWC04` | none | yes | no | yes |
| V1777 | `mord_MWC05` | none | yes | no | yes |
| V1778 | `mord_MWC06` | none | yes | no | yes |
| V1779 | `mord_MWC07` | none | yes | no | yes |
| V1780 | `mord_MWC08` | none | yes | no | yes |
| V1781 | `mord_MWC09` | none | yes | no | yes |
| V1782 | `mord_MWC10` | none | yes | no | yes |
| V1783 | `mord_TMWC10` | none | yes | no | yes |
| V1784 | `mord_SRW02` | none | yes | no | yes |
| V1785 | `mord_SRW03` | none | yes | no | yes |
| V1786 | `mord_SRW04` | none | yes | no | yes |
| V1787 | `mord_SRW05` | none | yes | no | yes |
| V1788 | `mord_SRW06` | none | yes | no | yes |
| V1789 | `mord_SRW07` | none | yes | no | yes |
| V1790 | `mord_SRW08` | none | yes | no | yes |
| V1791 | `mord_SRW09` | none | yes | no | yes |
| V1792 | `mord_SRW10` | none | yes | no | yes |
| V1793 | `mord_TSRW10` | none | yes | no | yes |

### 4 variables in `public.descriptors.values_2d (JSONB key)`: Zagreb topological index

Zagreb topological index. Origin: mordredcommunity 2.0.7, 2D Mordred descriptors (Moriwaki et al. 2018, in docs/REFERENCES.md). How: Computed by Mordred over the curated structure; a value that could not be computed is left out of the JSON object and its reason code is in mordred_null_codes. NULL: Absent from the object when Mordred gave no value; mordred_null_codes holds the reason. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1798 | `mord_Zagreb1` | none | yes | no | yes |
| V1799 | `mord_Zagreb2` | none | yes | no | yes |
| V1800 | `mord_mZagreb1` | none | yes | no | yes |
| V1801 | `mord_mZagreb2` | none | yes | no | yes |

## Drug-likeness and structural alerts

### `lipinski_violations` (V0137)

- Relation: `public.compound_scores`. Type: smallint. Unit: none stated.
- What it is: Number of Lipinski rule-of-five violations.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: Computed by the pipeline from the descriptors (S5.4); a mark, never a filter.
- NULL: May be NULL. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 2.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `veber_pass` (V0138)

- Relation: `public.compound_scores`. Type: boolean. Unit: none stated.
- What it is: Whether the compound passes the Veber rule.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: Rotatable bonds and TPSA against the Veber cutoffs (Veber et al. 2002, in docs/REFERENCES.md).
- NULL: May be NULL. Domain: true or false.
- Example: first data row of the v2.0.0 bioactivity-space TSV: false.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `pains_hit` (V0139)

- Relation: `public.compound_scores`. Type: boolean. Unit: none stated.
- What it is: Whether a PAINS structural alert matched.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: RDKit FilterCatalog, PAINS A, B and C (Baell and Holloway 2010, in docs/REFERENCES.md). A structural alert is a warning flag, not a proof of assay interference.
- NULL: May be NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `brenk_hit` (V0140)

- Relation: `public.compound_scores`. Type: boolean. Unit: none stated.
- What it is: Whether a Brenk structural alert matched.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: RDKit FilterCatalog, Brenk catalog (Brenk et al. 2008, in docs/REFERENCES.md).
- NULL: May be NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `nih_hit` (V0141)

- Relation: `public.compound_scores`. Type: boolean. Unit: none stated.
- What it is: Whether an NIH structural alert matched.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: RDKit FilterCatalog, NIH catalog.
- NULL: May be NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `lipinski_pass` (V0143)

- Relation: `public.compound_scores`. Type: boolean. Unit: none stated.
- What it is: Lipinski pass: at most one violation.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: Derived from lipinski_violations; a mark, never a filter.
- NULL: May be NULL. Domain: true or false.
- Example: first data row of the v2.0.0 bioactivity-space TSV: false.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `druglikeness_version` (V0144)

- Relation: `public.compound_scores`. Type: text. Unit: none stated.
- What it is: Version of the drug-likeness/tranche stage (compound_druglikeness_v1).
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: athanor-druglikeness-1.0.0.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `mw_tranche` (V0145)

- Relation: `public.compound_scores`. Type: text. Unit: none stated.
- What it is: S5.6 molecular-weight tranche letter (ZINC 2D scheme, edges in ATHANOR's configs/pipeline.yaml; not re-checked against the live ZINC page in v1.8.0).
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: J.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `logp_tranche` (V0146)

- Relation: `public.compound_scores`. Type: text. Unit: none stated.
- What it is: S5.6 logP tranche letter (same scheme).
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: B.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `tranche` (V0147)

- Relation: `public.compound_scores`. Type: text. Unit: none stated.
- What it is: S5.6 MW x logP tranche (mw_tranche || logp_tranche, CHECKed), indexed, for subsets and counts without scanning descriptors.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: JB.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `alerts` (V0152)

- Relation: `public.compound_scores`. Type: array. Unit: none stated.
- What it is: Names of the structural alerts the compound matches (RDKit FilterCatalog: PAINS A/B/C, Brenk, NIH, ZINC), from descriptors_v1.alerts. Marks, never a filter. NULL = none matched.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. NULL = none matched. Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: catechol;catechol_A(92).
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `alert_catalogs` (V0153)

- Relation: `public.compound_scores`. Type: array. Unit: none stated.
- What it is: Catalog of each entry of alerts, same order (descriptors_v1.alert_catalogs). pains_hit, brenk_hit and nih_hit are derived from it.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: Brenk;PAINS_B.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `n_alerts` (V0154)

- Relation: `public.compound_scores`. Type: integer. Unit: count.
- What it is: Number of alerts matched (descriptors_v1.n_alerts).
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: first data row of the v2.0.0 bioactivity-space TSV: 2.
- Files: descriptors_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `rule_key` (V0155)

- Relation: `public.compound_druglikeness_flags`. Type: text. Unit: none stated.
- What it is: The rule (FK druglikeness_rules).
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `passes` (V0156)

- Relation: `public.compound_druglikeness_flags`. Type: boolean. Unit: none stated.
- What it is: True when the compound meets the rule; NULL exactly when null_reason says why.
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: May be NULL. NULL exactly when null_reason says why. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `n_violations` (V0157)

- Relation: `public.compound_druglikeness_flags`. Type: smallint. Unit: count.
- What it is: For a rule of the desirable region (druglikeness_rules.region), how many criteria the compound fails; for a rule of the risk region (Pfizer 3/75), 1 inside the region and 0 outside. NULL with null_reason.
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: May be NULL. NULL with null_reason. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `null_reason` (V0158)

- Relation: `public.compound_druglikeness_flags`. Type: text. Unit: none stated.
- What it is: Why there is no verdict: descriptor_missing, out_of_domain, or cutoff_not_confirmed (migration 035, decision (az) of 2026-10-29: the rule is blocked, no readable source states its cutoffs; every compound carries the code). NULL exactly when passes holds a verdict.
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: May be NULL. NULL exactly when passes holds a verdict. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `rule_version` (V0159)

- Relation: `public.compound_druglikeness_flags`. Type: text. Unit: none stated.
- What it is: Version of the rule's cutoffs as implemented.
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `calculator` (V0160)

- Relation: `public.compound_druglikeness_flags`. Type: text. Unit: none stated.
- What it is: What computed the flag (rdkit).
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `calculator_version` (V0161)

- Relation: `public.compound_druglikeness_flags`. Type: text. Unit: none stated.
- What it is: Its version.
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_class` (V0162)

- Relation: `public.compound_druglikeness_flags`. Type: text. Unit: none stated.
- What it is: Always alchemia_derived (computed from the structure).
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_redistributable` (V0163)

- Relation: `public.compound_druglikeness_flags`. Type: boolean. Unit: none stated.
- What it is: A mark, never a filter (decision (hp)).
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `basis` (V0164)

- Relation: `public.compound_druglikeness_flags`. Type: text. Unit: none stated.
- What it is: How ATHANOR computed the flag: the descriptors and cutoffs it read. Never empty.
- Origin: ATHANOR S5.4 stage, computed from the structure.
- How: ATHANOR S5.4 stage, computed from the structure
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

## ADMET (predictions)

### `admet_model_version` (V0142)

- Relation: `public.compound_scores`. Type: text. Unit: none stated.
- What it is: Column-level COMMENT already present in migration 001: ADMET-AI v2 does not produce the same predictions as v1 (the version the published paper and public server use); without recording this, comparing predictions across runs would be invalid.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ad_min_max_similarity` (V0148)

- Relation: `public.compound_scores`. Type: real. Unit: Tanimoto similarity, 0 to 1.
- What it is: Minimum over the endpoints of the nearest-neighbour similarity (the least supported endpoint).
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `ad_mean_max_similarity` (V0149)

- Relation: `public.compound_scores`. Type: real. Unit: Tanimoto similarity, 0 to 1.
- What it is: Mean over the endpoints of the nearest-neighbour similarity.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `ad_status` (V0150)

- Relation: `public.compound_scores`. Type: text. Unit: none stated.
- What it is: ok | query structure does not parse (the applicability stage could not read the structure).
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: Closed list: ok, query.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `ad_version` (V0151)

- Relation: `public.compound_scores`. Type: text. Unit: none stated.
- What it is: Version of the applicability-domain stage.
- Origin: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1.
- How: ATHANOR S5.4 to S5.6 stages; ADMET from ADMET-AI 2.0.1
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### 52 variables in `public.compound_scores.admet_profile (JSONB key)`: ADMET-AI 2.0.1 model PREDICTION for this endpoint (or an RDKit property that ADMET-AI repo

ADMET-AI 2.0.1 model PREDICTION for this endpoint (or an RDKit property that ADMET-AI reports with it). A prediction is not a measurement.. Origin: ADMET-AI 2.0.1 (Swanson et al. 2024; v2 is not what that paper benchmarks, see docs/REFERENCES.md). How: Model inference over the curated structure; classifiers give a probability, regressors a value in the units of the training set. NULL: Absent when the model could not read the structure. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1824 | `admet_molecular_weight` | admet_tsv | yes | yes | yes |
| V1825 | `admet_logP` | admet_tsv | yes | yes | yes |
| V1826 | `admet_hydrogen_bond_acceptors` | admet_tsv | yes | yes | yes |
| V1827 | `admet_hydrogen_bond_donors` | admet_tsv | yes | yes | yes |
| V1828 | `admet_Lipinski` | admet_tsv | yes | yes | yes |
| V1829 | `admet_QED` | admet_tsv | yes | yes | yes |
| V1830 | `admet_stereo_centers` | admet_tsv | yes | yes | yes |
| V1831 | `admet_tpsa` | admet_tsv | yes | yes | yes |
| V1832 | `admet_PAINS_alert` | admet_tsv | yes | yes | yes |
| V1833 | `admet_BRENK_alert` | admet_tsv | yes | yes | yes |
| V1834 | `admet_NIH_alert` | admet_tsv | yes | yes | yes |
| V1835 | `admet_AMES` | admet_tsv | yes | yes | yes |
| V1836 | `admet_BBB_Martins` | admet_tsv | yes | yes | yes |
| V1837 | `admet_Bioavailability_Ma` | admet_tsv | yes | yes | yes |
| V1838 | `admet_CYP1A2_Veith` | admet_tsv | yes | yes | yes |
| V1839 | `admet_CYP2C19_Veith` | admet_tsv | yes | yes | yes |
| V1840 | `admet_CYP2C9_Substrate_CarbonMangels` | admet_tsv | yes | yes | yes |
| V1841 | `admet_CYP2C9_Veith` | admet_tsv | yes | yes | yes |
| V1842 | `admet_CYP2D6_Substrate_CarbonMangels` | admet_tsv | yes | yes | yes |
| V1843 | `admet_CYP2D6_Veith` | admet_tsv | yes | yes | yes |
| V1844 | `admet_CYP3A4_Substrate_CarbonMangels` | admet_tsv | yes | yes | yes |
| V1845 | `admet_CYP3A4_Veith` | admet_tsv | yes | yes | yes |
| V1846 | `admet_Carcinogens_Lagunin` | admet_tsv | yes | yes | yes |
| V1847 | `admet_ClinTox` | admet_tsv | yes | yes | yes |
| V1848 | `admet_DILI` | admet_tsv | yes | yes | yes |
| V1849 | `admet_HIA_Hou` | admet_tsv | yes | yes | yes |
| V1850 | `admet_NR_AR_LBD` | admet_tsv | yes | yes | yes |
| V1851 | `admet_NR_AR` | admet_tsv | yes | yes | yes |
| V1852 | `admet_NR_AhR` | admet_tsv | yes | yes | yes |
| V1853 | `admet_NR_Aromatase` | admet_tsv | yes | yes | yes |
| V1854 | `admet_NR_ER_LBD` | admet_tsv | yes | yes | yes |
| V1855 | `admet_NR_ER` | admet_tsv | yes | yes | yes |
| V1856 | `admet_NR_PPAR_gamma` | admet_tsv | yes | yes | yes |
| V1857 | `admet_PAMPA_NCATS` | admet_tsv | yes | yes | yes |
| V1858 | `admet_Pgp_Broccatelli` | admet_tsv | yes | yes | yes |
| V1859 | `admet_SR_ARE` | admet_tsv | yes | yes | yes |
| V1860 | `admet_SR_ATAD5` | admet_tsv | yes | yes | yes |
| V1861 | `admet_SR_HSE` | admet_tsv | yes | yes | yes |
| V1862 | `admet_SR_MMP` | admet_tsv | yes | yes | yes |
| V1863 | `admet_SR_p53` | admet_tsv | yes | yes | yes |
| V1864 | `admet_Skin_Reaction` | admet_tsv | yes | yes | yes |
| V1865 | `admet_hERG` | admet_tsv | yes | yes | yes |
| V1866 | `admet_Caco2_Wang` | admet_tsv | yes | yes | yes |
| V1867 | `admet_Clearance_Hepatocyte_AZ` | admet_tsv | yes | yes | yes |
| V1868 | `admet_Clearance_Microsome_AZ` | admet_tsv | yes | yes | yes |
| V1869 | `admet_Half_Life_Obach` | admet_tsv | yes | yes | yes |
| V1870 | `admet_HydrationFreeEnergy_FreeSolv` | admet_tsv | yes | yes | yes |
| V1871 | `admet_LD50_Zhu` | admet_tsv | yes | yes | yes |
| V1872 | `admet_Lipophilicity_AstraZeneca` | admet_tsv | yes | yes | yes |
| V1873 | `admet_PPBR_AZ` | admet_tsv | yes | yes | yes |
| V1874 | `admet_Solubility_AqSolDB` | admet_tsv | yes | yes | yes |
| V1875 | `admet_VDss_Lombardo` | admet_tsv | yes | yes | yes |

### 52 variables in `public.compound_scores.admet_profile (JSONB key)`: Percentile of the predicted value among the DrugBank approved drugs bundled in ADMET-AI (D

Percentile of the predicted value among the DrugBank approved drugs bundled in ADMET-AI (DrugBank 5.1.14).. Origin: ADMET-AI 2.0.1 (Swanson et al. 2024; v2 is not what that paper benchmarks, see docs/REFERENCES.md). How: Model inference over the curated structure; classifiers give a probability, regressors a value in the units of the training set. NULL: Absent when the model could not read the structure. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1876 | `admet_molecular_weight_drugbank_approved_percentile` | none | yes | no | yes |
| V1877 | `admet_logP_drugbank_approved_percentile` | none | yes | no | yes |
| V1878 | `admet_hydrogen_bond_acceptors_drugbank_approved_percentile` | none | yes | no | yes |
| V1879 | `admet_hydrogen_bond_donors_drugbank_approved_percentile` | none | yes | no | yes |
| V1880 | `admet_Lipinski_drugbank_approved_percentile` | none | yes | no | yes |
| V1881 | `admet_QED_drugbank_approved_percentile` | none | yes | no | yes |
| V1882 | `admet_stereo_centers_drugbank_approved_percentile` | none | yes | no | yes |
| V1883 | `admet_tpsa_drugbank_approved_percentile` | none | yes | no | yes |
| V1884 | `admet_PAINS_alert_drugbank_approved_percentile` | none | yes | no | yes |
| V1885 | `admet_BRENK_alert_drugbank_approved_percentile` | none | yes | no | yes |
| V1886 | `admet_NIH_alert_drugbank_approved_percentile` | none | yes | no | yes |
| V1887 | `admet_AMES_drugbank_approved_percentile` | none | yes | no | yes |
| V1888 | `admet_BBB_Martins_drugbank_approved_percentile` | none | yes | no | yes |
| V1889 | `admet_Bioavailability_Ma_drugbank_approved_percentile` | none | yes | no | yes |
| V1890 | `admet_CYP1A2_Veith_drugbank_approved_percentile` | none | yes | no | yes |
| V1891 | `admet_CYP2C19_Veith_drugbank_approved_percentile` | none | yes | no | yes |
| V1892 | `admet_CYP2C9_Substrate_CarbonMangels_drugbank_approved_percentile` | none | yes | no | yes |
| V1893 | `admet_CYP2C9_Veith_drugbank_approved_percentile` | none | yes | no | yes |
| V1894 | `admet_CYP2D6_Substrate_CarbonMangels_drugbank_approved_percentile` | none | yes | no | yes |
| V1895 | `admet_CYP2D6_Veith_drugbank_approved_percentile` | none | yes | no | yes |
| V1896 | `admet_CYP3A4_Substrate_CarbonMangels_drugbank_approved_percentile` | none | yes | no | yes |
| V1897 | `admet_CYP3A4_Veith_drugbank_approved_percentile` | none | yes | no | yes |
| V1898 | `admet_Carcinogens_Lagunin_drugbank_approved_percentile` | none | yes | no | yes |
| V1899 | `admet_ClinTox_drugbank_approved_percentile` | none | yes | no | yes |
| V1900 | `admet_DILI_drugbank_approved_percentile` | none | yes | no | yes |
| V1901 | `admet_HIA_Hou_drugbank_approved_percentile` | none | yes | no | yes |
| V1902 | `admet_NR_AR_LBD_drugbank_approved_percentile` | none | yes | no | yes |
| V1903 | `admet_NR_AR_drugbank_approved_percentile` | none | yes | no | yes |
| V1904 | `admet_NR_AhR_drugbank_approved_percentile` | none | yes | no | yes |
| V1905 | `admet_NR_Aromatase_drugbank_approved_percentile` | none | yes | no | yes |
| V1906 | `admet_NR_ER_LBD_drugbank_approved_percentile` | none | yes | no | yes |
| V1907 | `admet_NR_ER_drugbank_approved_percentile` | none | yes | no | yes |
| V1908 | `admet_NR_PPAR_gamma_drugbank_approved_percentile` | none | yes | no | yes |
| V1909 | `admet_PAMPA_NCATS_drugbank_approved_percentile` | none | yes | no | yes |
| V1910 | `admet_Pgp_Broccatelli_drugbank_approved_percentile` | none | yes | no | yes |
| V1911 | `admet_SR_ARE_drugbank_approved_percentile` | none | yes | no | yes |
| V1912 | `admet_SR_ATAD5_drugbank_approved_percentile` | none | yes | no | yes |
| V1913 | `admet_SR_HSE_drugbank_approved_percentile` | none | yes | no | yes |
| V1914 | `admet_SR_MMP_drugbank_approved_percentile` | none | yes | no | yes |
| V1915 | `admet_SR_p53_drugbank_approved_percentile` | none | yes | no | yes |
| V1916 | `admet_Skin_Reaction_drugbank_approved_percentile` | none | yes | no | yes |
| V1917 | `admet_hERG_drugbank_approved_percentile` | none | yes | no | yes |
| V1918 | `admet_Caco2_Wang_drugbank_approved_percentile` | none | yes | no | yes |
| V1919 | `admet_Clearance_Hepatocyte_AZ_drugbank_approved_percentile` | none | yes | no | yes |
| V1920 | `admet_Clearance_Microsome_AZ_drugbank_approved_percentile` | none | yes | no | yes |
| V1921 | `admet_Half_Life_Obach_drugbank_approved_percentile` | none | yes | no | yes |
| V1922 | `admet_HydrationFreeEnergy_FreeSolv_drugbank_approved_percentile` | none | yes | no | yes |
| V1923 | `admet_LD50_Zhu_drugbank_approved_percentile` | none | yes | no | yes |
| V1924 | `admet_Lipophilicity_AstraZeneca_drugbank_approved_percentile` | none | yes | no | yes |
| V1925 | `admet_PPBR_AZ_drugbank_approved_percentile` | none | yes | no | yes |
| V1926 | `admet_Solubility_AqSolDB_drugbank_approved_percentile` | none | yes | no | yes |
| V1927 | `admet_VDss_Lombardo_drugbank_approved_percentile` | none | yes | no | yes |

### 41 variables in `public.compound_scores.admet_applicability (JSONB key)`: Applicability domain of the matching ADMET prediction: similarity of the compound to its n

Applicability domain of the matching ADMET prediction: similarity of the compound to its nearest neighbour in that endpoint's training set. No in or out cut is applied; read it next to the prediction.. Origin: ATHANOR S5.5 stage, Morgan fingerprints against the TDC training sets (docs/REFERENCES.md). How: Maximum Tanimoto similarity (Morgan, radius 2) to the training compounds of the endpoint. NULL: Absent for an endpoint the stage withheld. Package: AURORA CC BY-SA yes, AURORA-NC yes.

| Id | Name | Files | Served | In files | In aurora_prod |
|---|---|---|---|---|---|
| V1928 | `ad_AMES` | none | no | no | yes |
| V1929 | `ad_BBB_Martins` | none | no | no | yes |
| V1930 | `ad_Bioavailability_Ma` | none | no | no | yes |
| V1931 | `ad_CYP1A2_Veith` | none | no | no | yes |
| V1932 | `ad_CYP2C19_Veith` | none | no | no | yes |
| V1933 | `ad_CYP2C9_Substrate_CarbonMangels` | none | no | no | yes |
| V1934 | `ad_CYP2C9_Veith` | none | no | no | yes |
| V1935 | `ad_CYP2D6_Substrate_CarbonMangels` | none | no | no | yes |
| V1936 | `ad_CYP2D6_Veith` | none | no | no | yes |
| V1937 | `ad_CYP3A4_Substrate_CarbonMangels` | none | no | no | yes |
| V1938 | `ad_CYP3A4_Veith` | none | no | no | yes |
| V1939 | `ad_Caco2_Wang` | none | no | no | yes |
| V1940 | `ad_Carcinogens_Lagunin` | none | no | no | yes |
| V1941 | `ad_Clearance_Hepatocyte_AZ` | none | no | no | yes |
| V1942 | `ad_Clearance_Microsome_AZ` | none | no | no | yes |
| V1943 | `ad_ClinTox` | none | no | no | yes |
| V1944 | `ad_DILI` | none | no | no | yes |
| V1945 | `ad_HIA_Hou` | none | no | no | yes |
| V1946 | `ad_Half_Life_Obach` | none | no | no | yes |
| V1947 | `ad_HydrationFreeEnergy_FreeSolv` | none | no | no | yes |
| V1948 | `ad_LD50_Zhu` | none | no | no | yes |
| V1949 | `ad_Lipophilicity_AstraZeneca` | none | no | no | yes |
| V1950 | `ad_NR_AR` | none | no | no | yes |
| V1951 | `ad_NR_AR_LBD` | none | no | no | yes |
| V1952 | `ad_NR_AhR` | none | no | no | yes |
| V1953 | `ad_NR_Aromatase` | none | no | no | yes |
| V1954 | `ad_NR_ER` | none | no | no | yes |
| V1955 | `ad_NR_ER_LBD` | none | no | no | yes |
| V1956 | `ad_NR_PPAR_gamma` | none | no | no | yes |
| V1957 | `ad_PAMPA_NCATS` | none | no | no | yes |
| V1958 | `ad_PPBR_AZ` | none | no | no | yes |
| V1959 | `ad_Pgp_Broccatelli` | none | no | no | yes |
| V1960 | `ad_SR_ARE` | none | no | no | yes |
| V1961 | `ad_SR_ATAD5` | none | no | no | yes |
| V1962 | `ad_SR_HSE` | none | no | no | yes |
| V1963 | `ad_SR_MMP` | none | no | no | yes |
| V1964 | `ad_SR_p53` | none | no | no | yes |
| V1965 | `ad_Skin_Reaction` | none | no | no | yes |
| V1966 | `ad_Solubility_AqSolDB` | none | no | no | yes |
| V1967 | `ad_VDss_Lombardo` | none | no | no | yes |
| V1968 | `ad_hERG` | none | no | no | yes |

## Fingerprints

### `morgan` (V0165)

- Relation: `public.fingerprints`. Type: bit vector (RDKit cartridge bfp). Unit: none stated.
- What it is: Morgan fingerprint, r=2, bfp. CHECK enforces exactly 2048 bits when non-NULL. Fixed length 2048.
- Origin: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer.
- How: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer
- NULL: May be NULL. CHECK enforces exactly 2048 bits when non-NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: fingerprints_parquet. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `morgan_ulvs` (V0166)

- Relation: `public.fingerprints`. Type: bit vector (RDKit cartridge bfp). Unit: none stated.
- What it is: Morgan fingerprint, r=2, bfp,  the fixed contract with the ULVS/Deep Docking pipeline. CHECK enforces exactly 1024 bits when non-NULL; same GUC-mismatch trap as morgan, but against 1024. Fixed length 1024.
- Origin: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer.
- How: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer
- NULL: May be NULL. CHECK enforces exactly 1024 bits when non-NULL; Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: fingerprints_parquet. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `maccs` (V0167)

- Relation: `public.fingerprints`. Type: bit vector (RDKit cartridge bfp). Unit: none stated.
- What it is: MACCS keys fingerprint (bfp). Fixed length 168.
- Origin: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer.
- How: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: fingerprints_parquet. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `fp_version` (V0168)

- Relation: `public.fingerprints`. Type: text. Unit: none stated.
- What it is: Version tag of the fingerprint-computation code that produced this row.
- Origin: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer.
- How: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `atompair_bv` (V0169)

- Relation: `public.fingerprints`. Type: bit vector (RDKit cartridge bfp). Unit: none stated.
- What it is: (bfp). Dense 2048-bit atom-pair bit vector, produced in Python via rdFingerprintGenerator.GetAtomPairGenerator(fpSize=2048),  per the migration COMMENT, bfp has no cast to sfp, so this is a distinct column from atompair, not a reinterpretation of it. CHECK enforces exactly 2048 bits when non-NULL. Fixed length 2048.
- Origin: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer.
- How: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer
- NULL: May be NULL. CHECK enforces exactly 2048 bits when non-NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: fingerprints_parquet. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `torsion_bv` (V0170)

- Relation: `public.fingerprints`. Type: bit vector (RDKit cartridge bfp). Unit: none stated.
- What it is: (bfp). Dense 2048-bit topological-torsion bit vector, same rationale as atompair_bv. CHECK enforces exactly 2048 bits when non-NULL. GiST-indexed. Fixed length 2048.
- Origin: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer.
- How: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer
- NULL: May be NULL. CHECK enforces exactly 2048 bits when non-NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: fingerprints_parquet. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `e3fp` (V0171)

- Relation: `public.fingerprints`. Type: bit vector (RDKit cartridge bfp). Unit: none stated.
- What it is: (bfp). E3FP (Extended 3-Dimensional FingerPrint), computed over the minimized conformer by featurize_3d.py, a real fingerprint (not a scalar descriptor), used for 3D similarity search. CHECK enforces exactly 1024 bits when non-NULL; NULL for the few compounds where the E3FP embed failed. Fixed length 1024.
- Origin: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer.
- How: ATHANOR fingerprint stage with RDKit 2026.03.4 (see docs/REFERENCES.md); E3FP 1.2.7 over the minimized conformer
- NULL: May be NULL. CHECK enforces exactly 1024 bits when non-NULL; Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: fingerprints_parquet. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

## Embeddings and MinHash

### `embedding_status` (V0172)

- Relation: `public.compound_embeddings`. Type: text. Unit: none stated.
- What it is: ok | too_long | unknown_token | parse_error.
- Origin: ATHANOR S5.9 stage, learned embedding.
- How: ATHANOR S5.9 stage, learned embedding
- NULL: Never NULL. Domain: Closed list: ok, too_long, unknown_token, parse_error.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `n_tokens` (V0173)

- Relation: `public.compound_embeddings`. Type: integer. Unit: count.
- What it is: Tokens of the structure given to the model.
- Origin: ATHANOR S5.9 stage, learned embedding.
- How: ATHANOR S5.9 stage, learned embedding
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `embedding` (V0174)

- Relation: `public.compound_embeddings`. Type: vector. Unit: none stated.
- What it is: The embedding, vector(768); NULL when embedding_status is not ok. Fixed length 768.
- Origin: ATHANOR S5.9 stage, learned embedding.
- How: ATHANOR S5.9 stage, learned embedding
- NULL: May be NULL. NULL when embedding_status is not ok. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `embedding_model` (V0175)

- Relation: `public.compound_embeddings`. Type: text. Unit: none stated.
- What it is: The model that produced it.
- Origin: ATHANOR S5.9 stage, learned embedding.
- How: ATHANOR S5.9 stage, learned embedding
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `embedding_version` (V0176)

- Relation: `public.compound_embeddings`. Type: text. Unit: none stated.
- What it is: Version of the S5.9 stage.
- Origin: ATHANOR S5.9 stage, learned embedding.
- How: ATHANOR S5.9 stage, learned embedding
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `mhfp` (V0177)

- Relation: `public.compound_mhfp`. Type: array. Unit: none stated.
- What it is: The 512 MinHash values, uint32 stored as int4 (two's complement; mhfp_uint32 reads them back), in permutation order; NULL when mhfp_status is not ok. Fixed length 512.
- Origin: ATHANOR stage, rdMHFPFingerprint of RDKit.
- How: ATHANOR stage, rdMHFPFingerprint of RDKit
- NULL: May be NULL. NULL when mhfp_status is not ok. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `mhfp_status` (V0178)

- Relation: `public.compound_mhfp`. Type: text. Unit: none stated.
- What it is: ok, or the code of why there is no fingerprint: parse_error (RDKit did not read the structure). ATHANOR's mhfp_status.
- Origin: ATHANOR stage, rdMHFPFingerprint of RDKit.
- How: ATHANOR stage, rdMHFPFingerprint of RDKit
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `n_permutations` (V0179)

- Relation: `public.compound_mhfp`. Type: integer. Unit: count.
- What it is: Number of permutations of this fingerprint: 512 (decision (q)); scripts/load.py refuses one that is not its parameter set's. May be NULL when mhfp_status is not ok.
- Origin: ATHANOR stage, rdMHFPFingerprint of RDKit.
- How: ATHANOR stage, rdMHFPFingerprint of RDKit
- NULL: May be NULL. May be NULL when mhfp_status is not ok. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `params_digest` (V0180)

- Relation: `public.compound_mhfp`. Type: text. Unit: none stated.
- What it is: The parameter set it was computed with (mhfp_parameter_sets).
- Origin: ATHANOR stage, rdMHFPFingerprint of RDKit.
- How: ATHANOR stage, rdMHFPFingerprint of RDKit
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

## Docking preparation (PDBQT)

### `sdf_molblock` (V0116)

- Relation: `public.compound_structures_3d`. Type: text. Unit: none stated.
- What it is: The whole SDF file of the compound, byte for byte as distributed (molblock through M END, then its tags and $$$$), original line endings. The molblock alone, for mol_from_ctab, is the text up to and including the line M END. TOAST compression lz4.
- Origin: The SDF and PDBQT of the release, stored byte for byte.
- How: The SDF and PDBQT of the release, stored byte for byte
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: sdf. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `pdbqt_text` (V0117)

- Relation: `public.compound_structures_3d`. Type: text. Unit: none stated.
- What it is: The whole PDBQT file of the compound, byte for byte as distributed (Meeko, Gasteiger charges). TOAST compression lz4.
- Origin: The SDF and PDBQT of the release, stored byte for byte.
- How: The SDF and PDBQT of the release, stored byte for byte
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `sdf_sha256` (V0118)

- Relation: `public.compound_structures_3d`. Type: char(27) or char(64). Unit: none stated.
- What it is: sha256 of sdf_molblock (CHECK recomputes it); equal to structure_files.sha256 and to the MANIFEST.jsonl line of the same SDF, checked by the loader.
- Origin: The SDF and PDBQT of the release, stored byte for byte.
- How: The SDF and PDBQT of the release, stored byte for byte
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `pdbqt_sha256` (V0119)

- Relation: `public.compound_structures_3d`. Type: char(27) or char(64). Unit: none stated.
- What it is: sha256 of pdbqt_text (CHECK recomputes it); equal to structure_files.sha256 and to the MANIFEST.jsonl line of the same PDBQT, checked by the loader.
- Origin: The SDF and PDBQT of the release, stored byte for byte.
- How: The SDF and PDBQT of the release, stored byte for byte
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `conformer_version` (V0120)

- Relation: `public.compound_structures_3d`. Type: text. Unit: none stated.
- What it is: conformers.conformer_version of the compound when the row was written (the conformer stage that produced the geometry); NULL when the release carries no conformer_provenance_v1.
- Origin: The SDF and PDBQT of the release, stored byte for byte.
- How: The SDF and PDBQT of the release, stored byte for byte
- NULL: May be NULL. NULL when the release carries no conformer_provenance_v1. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `tag_protonation_dominant_smiles` (V1974)

- Relation: `file content: SDF tag protonation_dominant_smiles`. Type: text. Unit: none stated.
- What it is: SMILES of the dominant protonation microstate at the modelled pH. The coordinates in the file are the neutral parent. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md).
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: sdf, pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the files, not served as a separate field in this release (the SDF endpoint returns the file whole).

### `tag_protonation_charge` (V1975)

- Relation: `file content: SDF tag protonation_charge`. Type: integer as text. Unit: none stated.
- What it is: Net charge of the dominant microstate. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md).
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: sdf, pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the files, not served as a separate field in this release (the SDF endpoint returns the file whole).

### `tag_protonation_changed_from_neutral` (V1976)

- Relation: `file content: SDF tag protonation_changed_from_neutral`. Type: boolean as text. Unit: none stated.
- What it is: True when the dominant microstate differs from the neutral parent. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: RDKit 2026.03.4 (see docs/REFERENCES.md).
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: sdf, pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the files, not served as a separate field in this release (the SDF endpoint returns the file whole).

### `pdbqt_atom_record` (V1977)

- Relation: `file content: PDBQT ATOM record: coordinates, partial charge and AutoDock atom type`. Type: text. Unit: none stated.
- What it is: One record per atom: 3D coordinates, a Gasteiger partial charge and an AutoDock atom type. Polar hydrogens are kept, non-polar hydrogens are merged. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: Meeko 0.7.1 (PDBQT, Gasteiger charges, docs/REFERENCES.md); RDKit for the SDF.
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (per-compound SDF and PDBQT endpoints).

### `pdbqt_torsion_tree` (V1978)

- Relation: `file content: PDBQT torsion tree (ROOT, BRANCH, ENDBRANCH records)`. Type: text. Unit: none stated.
- What it is: The rigid root and the rotatable branches the docking engine may twist. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: Meeko 0.7.1 (PDBQT, Gasteiger charges, docs/REFERENCES.md); RDKit for the SDF.
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (per-compound SDF and PDBQT endpoints).

### `pdbqt_smiles_remarks` (V1979)

- Relation: `file content: PDBQT REMARK SMILES, SMILES IDX and H PARENT`. Type: text. Unit: none stated.
- What it is: The SMILES that Meeko prepared and the atom index maps back to the input molecule. Present in every SDF and PDBQT of the complete tier; taken from the files of the release.
- Origin: Meeko 0.7.1 (PDBQT, Gasteiger charges, docs/REFERENCES.md); RDKit for the SDF.
- How: Written when the file is prepared; the loader checks the sha256 of each file against the manifest.
- NULL: Not applicable: the record is part of the file format. Domain: open.
- Example: none beyond the file itself.
- Files: pdbqt. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served (per-compound SDF and PDBQT endpoints).

## Scaffolds, classification, organisms

### `smarts_classes` (V0010)

- Relation: `public.compounds`. Type: jsonb. Unit: none stated.
- What it is: JSONB (GIN-indexed.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `scaffold_status` (V0181)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: Outcome of the scaffold stage for this compound.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_acyclic` (V0182)

- Relation: `public.compound_scaffolds`. Type: boolean. Unit: none stated.
- What it is: True when the compound has no ring (no scaffold).
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `scaffold_smiles` (V0183)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: Bemis-Murcko scaffold, SMILES.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `scaffold_key` (V0184)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: Key of the scaffold (groups compounds that share it).
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `generic_scaffold_smiles` (V0185)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: Generic scaffold (atoms and bonds made generic), SMILES.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `generic_scaffold_key` (V0186)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: Key of the generic scaffold.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `n_scaffold_rings` (V0187)

- Relation: `public.compound_scaffolds`. Type: integer. Unit: count.
- What it is: Rings in the scaffold.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `scaffold_version` (V0188)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: Version of the S5.7 stage.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `rdkit_version` (V0189)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: RDKit version that computed the scaffold.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `scaffold_tree_l1_smiles` (V0190)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: Level 1 of the Scaffold Tree (Schuffenhauer 2007, doi:10.1021/ci600338x; Langdon 2011, doi:10.1021/ci2001428), SMILES, as ATHANOR S5.7 computes it with RDKit rdScaffoldNetwork (decision (ab)); NULL for an acyclic compound and for rows written before migration 032.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: May be NULL. NULL for an acyclic compound and for rows written before migration 032. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `scaffold_tree_l1_key` (V0191)

- Relation: `public.compound_scaffolds`. Type: text. Unit: none stated.
- What it is: Key of the Level 1 scaffold (groups the compounds that share it; the key of the Aurora Diversity Set, (ab), and of the Explorer filter, (ar)); indexed.
- Origin: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit.
- How: ATHANOR S5.7 stage, Bemis-Murcko scaffolds with RDKit
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_pathway` (V0192)

- Relation: `public.compound_np_classification`. Type: text. Unit: none stated.
- What it is: NPClassifier pathway classification, sourced from COCONUT's np_classifier_pathway CSV column (~93% coverage of COCONUT-origin compounds per docs/SCHEMA.md).
- Origin: NPClassifier labels declared by COCONUT-origin records.
- How: NPClassifier labels declared by COCONUT-origin records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_superclass` (V0193)

- Relation: `public.compound_np_classification`. Type: text. Unit: none stated.
- What it is: NPClassifier superclass classification, sourced from COCONUT's np_classifier_superclass CSV column (~80% coverage per docs/SCHEMA.md).
- Origin: NPClassifier labels declared by COCONUT-origin records.
- How: NPClassifier labels declared by COCONUT-origin records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_class` (V0194)

- Relation: `public.compound_np_classification`. Type: text. Unit: none stated.
- What it is: NPClassifier class classification, sourced from COCONUT's np_classifier_class CSV column (~75-76% coverage per docs/SCHEMA.md).
- Origin: NPClassifier labels declared by COCONUT-origin records.
- How: NPClassifier labels declared by COCONUT-origin records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_is_glycoside` (V0195)

- Relation: `public.compound_np_classification`. Type: boolean. Unit: none stated.
- What it is: Boolean glycoside flag, sourced from COCONUT's np_classifier_is_glycoside CSV column (~99.99% coverage of COCONUT-origin compounds, per the private Athanor pipeline (CLAUDE.md), 'Implementation,  2026-08-05').
- Origin: NPClassifier labels declared by COCONUT-origin records.
- How: NPClassifier labels declared by COCONUT-origin records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_status` (V0196)

- Relation: `public.compound_np_likeness`. Type: text. Unit: none stated.
- What it is: Outcome of the NP-likeness stage for this compound.
- Origin: ATHANOR S5.8 stage, natural-product likeness model.
- How: ATHANOR S5.8 stage, natural-product likeness model
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_likeness` (V0197)

- Relation: `public.compound_np_likeness`. Type: real. Unit: score, higher is closer to natural products.
- What it is: NP-likeness score (higher = closer to natural products).
- Origin: ATHANOR S5.8 stage, natural-product likeness model.
- How: ATHANOR S5.8 stage, natural-product likeness model
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_confidence` (V0198)

- Relation: `public.compound_np_likeness`. Type: real. Unit: none stated.
- What it is: Confidence of the score, as the model reports it.
- Origin: ATHANOR S5.8 stage, natural-product likeness model.
- How: ATHANOR S5.8 stage, natural-product likeness model
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_model_sha256` (V0199)

- Relation: `public.compound_np_likeness`. Type: text. Unit: none stated.
- What it is: sha256 of the model file that scored the compound.
- Origin: ATHANOR S5.8 stage, natural-product likeness model.
- How: ATHANOR S5.8 stage, natural-product likeness model
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `np_version` (V0200)

- Relation: `public.compound_np_likeness`. Type: text. Unit: none stated.
- What it is: Version of the S5.8 stage.
- Origin: ATHANOR S5.8 stage, natural-product likeness model.
- How: ATHANOR S5.8 stage, natural-product likeness model
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `rdkit_version` (V0201)

- Relation: `public.compound_np_likeness`. Type: text. Unit: none stated.
- What it is: RDKit version used by the stage.
- Origin: ATHANOR S5.8 stage, natural-product likeness model.
- How: ATHANOR S5.8 stage, natural-product likeness model
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `layer` (V0202)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: structural, natural_product or chemont.
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `scheme` (V0203)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: rdkit_functional_group, rdkit_ring_family (layer structural), npclassifier (natural_product), chemont.
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `level` (V0204)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: functional_group, ring_family, pathway, superclass, class, chemont_term; must agree with the scheme (CHECK).
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `label` (V0205)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: The class the classifier gave; NULL exactly when null_reason says why.
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: May be NULL. NULL exactly when null_reason says why. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `score` (V0206)

- Relation: `public.compound_chemical_classification`. Type: real. Unit: confidence, 0 to 1.
- What it is: Confidence the classifier reports, 0 to 1; NULL when it reports none (SMARTS).
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: May be NULL. NULL when it reports none (SMARTS). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `null_reason` (V0207)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: classifier_failed or out_of_domain: why there is no label. NULL when there is one.
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: May be NULL. NULL when there is one. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `basis` (V0208)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: calculated (by ATHANOR S5.10) or declared (carried by a source, such as COCONUT's NPClassifier labels).
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `classifier` (V0209)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: What classified: rdkit_smarts, npclassifier, classyfire.
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `classifier_version` (V0210)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: Version of the classifier and, for SMARTS, of the pattern set.
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `model_sha256` (V0211)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: sha256 of the model or pattern file used, when there is one.
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `license_class` (V0212)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: alchemia_derived (computed here from the structure), cc0_1_0, cc_by_4_0, source_agreement (a declared row, the licence of its source), chemont_restricted (ChemOnt, closed).
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_redistributable` (V0213)

- Relation: `public.compound_chemical_classification`. Type: boolean. Unit: none stated.
- What it is: A mark, never a filter (decision (hp)); always false for ChemOnt (CHECK).
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `classified_on` (V0214)

- Relation: `public.compound_chemical_classification`. Type: date. Unit: none stated.
- What it is: Date the classifier ran (or the source release date, for a declared row).
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `citation` (V0215)

- Relation: `public.compound_chemical_classification`. Type: text. Unit: none stated.
- What it is: The attribution the row carries, as ATHANOR wrote it: the classifier's paper and DOI for NPClassifier, the pattern set and RDKit for the SMARTS rows. Never empty.
- Origin: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed).
- How: ATHANOR S5.10 stage: RDKit SMARTS, NPClassifier, ChemOnt (closed, not distributed)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `sugar_status` (V0216)

- Relation: `public.compound_sugars`. Type: text. Unit: none stated.
- What it is: ok, or error with failure_reason: the code of every NULL in this row (decision (ak)).
- Origin: Sugar Removal Utility over CDK, decision of migration 036.
- How: Sugar Removal Utility over CDK, decision of migration 036
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `contains_sugar` (V0217)

- Relation: `public.compound_sugars`. Type: boolean. Unit: none stated.
- What it is: Whether the compound has a circular or linear sugar moiety; equals n_circular_sugars + n_linear_sugars > 0.
- Origin: Sugar Removal Utility over CDK, decision of migration 036.
- How: Sugar Removal Utility over CDK, decision of migration 036
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `n_circular_sugars` (V0218)

- Relation: `public.compound_sugars`. Type: smallint. Unit: count.
- What it is: Number of circular sugar moieties the utility detects with the settings of sru_version.
- Origin: Sugar Removal Utility over CDK, decision of migration 036.
- How: Sugar Removal Utility over CDK, decision of migration 036
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `n_linear_sugars` (V0219)

- Relation: `public.compound_sugars`. Type: smallint. Unit: count.
- What it is: Number of linear sugar moieties the utility detects with the settings of sru_version.
- Origin: Sugar Removal Utility over CDK, decision of migration 036.
- How: Sugar Removal Utility over CDK, decision of migration 036
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `failure_reason` (V0220)

- Relation: `public.compound_sugars`. Type: text. Unit: none stated.
- What it is: Why the utility failed on this compound; present exactly on an error row.
- Origin: Sugar Removal Utility over CDK, decision of migration 036.
- How: Sugar Removal Utility over CDK, decision of migration 036
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: descriptors_tsv, descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `sru_version` (V0221)

- Relation: `public.compound_sugars`. Type: text. Unit: none stated.
- What it is: The Sugar Removal Utility version and its settings label (1.6 at decision (aq)).
- Origin: Sugar Removal Utility over CDK, decision of migration 036.
- How: Sugar Removal Utility over CDK, decision of migration 036
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `cdk_version` (V0222)

- Relation: `public.compound_sugars`. Type: text. Unit: none stated.
- What it is: The CDK version the utility ran on.
- Origin: Sugar Removal Utility over CDK, decision of migration 036.
- How: Sugar Removal Utility over CDK, decision of migration 036
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `organism_name` (V0223)

- Relation: `public.compound_organisms`. Type: text. Unit: none stated.
- What it is: Species/organism name as provided by the source (e.g. from COCONUT's pipe-separated 'organisms' column).
- Origin: Organism names declared by the sources (COCONUT, Iracema).
- How: Organism names declared by the sources (COCONUT, Iracema)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_key` (V0224)

- Relation: `public.compound_organisms`. Type: text. Unit: none stated.
- What it is: Key of the source this organism attribution came from (e.g. 'coconut', 'iracema').
- Origin: Organism names declared by the sources (COCONUT, Iracema).
- How: Organism names declared by the sources (COCONUT, Iracema)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `created_at` (V0225)

- Relation: `public.compound_organisms`. Type: timestamp with time zone. Unit: none stated.
- What it is: Row insertion timestamp.
- Origin: Organism names declared by the sources (COCONUT, Iracema).
- How: Organism names declared by the sources (COCONUT, Iracema)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `result` (V0226)

- Relation: `public.compound_taxa`. Type: text. Unit: none stated.
- What it is: found, absent (the QID has no P703) or not_applicable (the compound has no Wikidata QID).
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `compound_qid` (V0227)

- Relation: `public.compound_taxa`. Type: text. Unit: none stated.
- What it is: The Wikidata QID read, one of the compound's found QIDs in compound_xrefs_resolved; a compound with several QIDs has its rows, and its absent row, per QID (2026-10-29: no QID is dropped); which QID is primary is compound_xrefs_resolved.is_primary, shown by v_compound_taxa. NULL when not_applicable.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: May be NULL. NULL when not_applicable. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `qid_xref_db` (V0228)

- Relation: `public.compound_taxa`. Type: text. Unit: none stated.
- What it is: Generated, always wikidata: the xref_db half of the foreign key of compound_qid to compound_xrefs_resolved.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `taxon_qid` (V0229)

- Relation: `public.compound_taxa`. Type: text. Unit: none stated.
- What it is: The QID of the taxon (the object of P703); NULL on an absent or not_applicable row.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: May be NULL. NULL on an absent or not_applicable row. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `taxon_name` (V0230)

- Relation: `public.compound_taxa`. Type: text. Unit: none stated.
- What it is: The taxon name of that item (P225), present on every found row.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ncbi_taxid` (V0231)

- Relation: `public.compound_taxa`. Type: integer. Unit: none stated.
- What it is: The NCBI Taxonomy id of the taxon (P685), indexed; NULL where Wikidata has none.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: May be NULL. NULL where Wikidata has none. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `reference_qids` (V0232)

- Relation: `public.compound_taxa`. Type: array. Unit: none stated.
- What it is: The QIDs of the works the P703 statement cites (P248, stated in); empty where it cites none.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_name` (V0233)

- Relation: `public.compound_taxa`. Type: text. Unit: none stated.
- What it is: The reference source (reference_sources): wikidata.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_version` (V0234)

- Relation: `public.compound_taxa`. Type: text. Unit: none stated.
- What it is: The date of the Wikidata dump or of the query.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_sha256` (V0235)

- Relation: `public.compound_taxa`. Type: text. Unit: none stated.
- What it is: sha256 of the query result read.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `looked_up_on` (V0236)

- Relation: `public.compound_taxa`. Type: date. Unit: none stated.
- What it is: The day of the lookup.
- Origin: Wikidata statement P703 of the compound QID.
- How: Wikidata statement P703 of the compound QID
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

## Activities

### `activity_type` (V0245)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Free-text assay/activity type as given by the source (e.g. IC50, %inhibition).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `description` (V0246)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Free-text description of the assay, source-provided.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `organism` (V0247)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Organism the assay was run against/in, source-provided free text.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `target` (V0248)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Biological target of the assay, source-provided free text.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `value_text` (V0249)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Original, unparsed value text as given by the source (e.g. '28 ± 1'), per DDL comment always preserved.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `unit_text` (V0250)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Original unit text as given by the source, including any embedded deviation symbol (e.g. 'μM ± SD').
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `value_num` (V0251)

- Relation: `public.compound_activities`. Type: double precision. Unit: none stated.
- What it is: Parsed numeric value, populated only when the parse from value_text is reliable.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `value_sd` (V0252)

- Relation: `public.compound_activities`. Type: double precision. Unit: none stated.
- What it is: Parsed standard deviation, when present in the source's value_text.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `unit_normalized` (V0253)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: unit_text normalized for parsing/unit conversion (e.g. µ/μ variants reconciled).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `parse_confidence` (V0254)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Enumerated via CHECK: 'exact', 'approximate', 'unparsed', 'source_structured'. source_structured: the source gave the value already structured and the loader marked it so (ChEMBL: relation and standard number); no value_text was interpreted.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: Never NULL. Domain: Closed list: exact, approximate.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `doi` (V0255)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: DOI of the publication reporting this specific activity measurement,  per migration 018/017's COMMENT, distinct from compound_references.doi, which is a general compound reference rather than a citation for one measurement.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `laboratory` (V0256)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Laboratory that performed the assay, source-provided free text.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `institution` (V0257)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Institution associated with the assay, source-provided free text.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `created_at` (V0258)

- Relation: `public.compound_activities`. Type: timestamp with time zone. Unit: none stated.
- What it is: Row insertion timestamp.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `standard_type` (V0259)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: activity_type normalized to a controlled vocabulary (IC50, EC50, CC50, EC90, LC50, MIC90, %INHIBITION), derived from activity_type; NULL when activity_type matches no known pattern.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL when activity_type matches no known pattern. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `standard_relation` (V0260)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Relation sign extracted from the start of value_text, or '=' for a plain number. Enumerated via CHECK: '=','<','>','<=','>=','~'.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: Closed list: '=','<','>','<=','>=','~'.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `standard_value` (V0261)

- Relation: `public.compound_activities`. Type: double precision. Unit: nM for molar types, % for percent inhibition.
- What it is: value_num converted to a single scale (nM, for molar-potency types) based on unit_normalized; NULL when the unit is mass-based, per migration 010 COMMENT (conversion would require a compound molecular weight, out of scope for this column).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL when the unit is mass-based, per migration 010 COMMENT (conversion would require a compound molecular weight, out of scope for this column). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `standard_units` (V0262)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Unit of standard_value: 'nM' for converted molar potency, '%' for %INHIBITION (no conversion, already dimensionless), per migration 010 COMMENT.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `pchembl_value` (V0263)

- Relation: `public.compound_activities`. Type: double precision. Unit: -log10(molar).
- What it is: -log10(standard_value in Molar), computed only when standard_relation='=' AND standard_units='nM' AND standard_value>0 AND standard_type is a molar-potency type,  same convention as ChEMBL's own pChEMBL, per migration 010 COMMENT.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `record_origin` (V0264)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Origin of the record inside the source, verbatim (BindingDB: the Curation/DataSource value). NULL on the rows written before migration 011.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL on the rows written before migration 011. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_class` (V0265)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Licence class of this record: cc_by_3_0, cc_by_sa_3_0, cc_by_4_0, source_agreement or undetermined. From a closed lookup keyed by (source, origin) written by the founder with counsel (P10); an origin that is not in the lookup is undetermined. a loader of a source with per-record origins must set it.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_record_id` (V0267)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: The source's own id of the measurement, verbatim: ChEMBL activities.activity_id; BindingDB <Reactant_set_id>:<type>, type one of Ki, IC50, Kd, EC50 and equal to standard_type (contract v6, founder decision (f) of 2026-10-27). With source_id it is unique where present, which makes a reload idempotent.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_version` (V0268)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Release of the source file the row was read from (BindingDB: 202610).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `collapsed_count` (V0269)

- Relation: `public.compound_activities`. Type: integer. Unit: count.
- What it is: How many identical source rows were collapsed into this one (BindingDB exact duplicates are collapsed, counted here and in the load report, never silently). The list of the collapsed record ids stays in the Parquet of the bundle, not in the database (P6).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ph` (V0270)

- Relation: `public.compound_activities`. Type: real. Unit: pH units.
- What it is: pH of the assay as reported, 0 to 14. A value outside the range is stored as NULL with the flag ph_out_of_range.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. A value outside the range is stored as NULL with the flag ph_out_of_range. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `temperature_c` (V0271)

- Relation: `public.compound_activities`. Type: real. Unit: degree Celsius.
- What it is: Assay temperature in degrees Celsius, not below -273.15. A value below absolute zero is NULL with temp_out_of_range; one that is possible but implausible is kept as written with suspect_unit.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. A value below absolute zero is NULL with temp_out_of_range; Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `pmid` (V0272)

- Relation: `public.compound_activities`. Type: integer. Unit: none stated.
- What it is: PubMed id of the article reporting the measurement, a positive integer; NULL when absent or not numeric.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL when absent or not numeric. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `patent_number` (V0273)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Patent number as reported, trimmed and upper case; NULL when empty.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL when empty. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `pubchem_aid` (V0274)

- Relation: `public.compound_activities`. Type: bigint. Unit: none stated.
- What it is: PubChem BioAssay id (AID), a positive integer, the prefix and spaces of the source removed; NULL when the rest is not numeric.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL when the rest is not numeric. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `published_on` (V0275)

- Relation: `public.compound_activities`. Type: date. Unit: none stated.
- What it is: Publication date of the article, ISO, converted from M/D/YYYY; NULL when it cannot be read (counted in the load report).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL when it cannot be read (counted in the load report). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `value_flags` (V0276)

- Relation: `public.compound_activities`. Type: array. Unit: none stated.
- What it is: Reasons recorded instead of dropping a row, from a closed list (CHECK): zero_value, implausible_gt_1M, multi_accession_field, ph_out_of_range, temp_out_of_range, suspect_unit, cx_extension_stripped, relative_stereo, unparsed_value, doi_malformed. Shown in v_open_cc_by_sa_activities (P8).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `standard_flag` (V0277)

- Relation: `public.compound_activities`. Type: smallint. Unit: none stated.
- What it is: ChEMBL standard_flag: 1 when the source standardised the value (standard_type, relation, value, units), 0 when it did not; NULL for a source without it.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL for a source without it. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `data_validity_comment` (V0278)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: ChEMBL data_validity_comment, verbatim, closed since migration 028 to the seven values of ChEMBL 37 DATA_VALIDITY_LOOKUP (Author confirmed error, Manually validated, Non standard unit for type, Outside typical range, Potential author error, Potential missing data, Potential transcription error); NULL when the source flagged nothing.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL when the source flagged nothing. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `potential_duplicate` (V0279)

- Relation: `public.compound_activities`. Type: boolean. Unit: none stated.
- What it is: ChEMBL potential_duplicate: the source suspects this value repeats one already published. A mark the source gives, not ours; NULL for a source without it.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL for a source without it. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `origin_compound_id` (V0280)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Id of the compound in the database the record comes from: for a ChEMBL row the molecule_chembl_id of the tested form (required by scripts/load.py); for a BindingDB row of ChEMBL origin, the ChEMBL ID of Ligand. Needed for the ChEMBL attribution.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `origin_release` (V0281)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Release of the database the record comes from, when it is not the row's own source_version (a BindingDB row of ChEMBL origin: the ChEMBL release BindingDB took it from). A ChEMBL row falls back to its source_version.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `text_value` (V0282)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: ChEMBL ACTIVITIES.text_value: a non-numeric result as deposited.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `standard_text_value` (V0283)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: ChEMBL ACTIVITIES.standard_text_value: the standardised non-numeric result (e.g. Active, Not active, Toxic), verbatim.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `activity_comment` (V0284)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: ChEMBL ACTIVITIES.activity_comment (e.g. inactive, Not Determined, inconclusive), verbatim: keeps the negative result.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `upper_value` (V0285)

- Relation: `public.compound_activities`. Type: double precision. Unit: none stated.
- What it is: Upper end of a range, as deposited (ChEMBL ACTIVITIES.upper_value).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `standard_upper_value` (V0286)

- Relation: `public.compound_activities`. Type: double precision. Unit: none stated.
- What it is: Upper end of a range, standardised (ChEMBL ACTIVITIES.standard_upper_value).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `action_type` (V0287)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: ChEMBL ACTIVITIES.action_type, closed to the 35 values of ChEMBL 37 ACTION_TYPE.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `bao_endpoint` (V0288)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: BioAssay Ontology endpoint of the measurement (ChEMBL ACTIVITIES.bao_endpoint, BAO_ and seven digits).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `uo_units` (V0289)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Units Ontology id of standard_units (ChEMBL ACTIVITIES.uo_units, UO_ and seven digits).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `qudt_units` (V0290)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: QUDT URI of standard_units (ChEMBL ACTIVITIES.qudt_units).
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `pchembl_origin` (V0291)

- Relation: `public.compound_activities`. Type: text. Unit: none stated.
- What it is: Where pchembl_value came from: source (copied verbatim from the source, ChEMBL) or calculated (by ATHANOR, with ChEMBL's rule); NULL exactly when pchembl_value is NULL. Rows written before 028 are calculated. pchembl_divergence recalculates the source ones.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: May be NULL. NULL exactly when pchembl_value is NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

## Drug annotations (ChEMBL and sources)

### `source_key` (V0292)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: Source of the annotation (sources.source_key).
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `clinical_phase` (V0293)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: Normalized clinical phase (CHECKed list); NULL when the record has none.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: May be NULL. NULL when the record has none. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `clinical_phase_raw` (V0294)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: The phase as the source writes it.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `development_status_raw` (V0295)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: The development status as the source writes it.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `mechanism_of_action` (V0296)

- Relation: `public.compound_drug_annotations`. Type: array. Unit: none stated.
- What it is: Mechanisms of action declared by the source.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `mechanism_detail` (V0297)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: Free-text detail of the mechanism.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `declared_targets` (V0298)

- Relation: `public.compound_drug_annotations`. Type: array. Unit: none stated.
- What it is: Targets as the source declares them (mapped in target_mapping).
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `disease_area` (V0299)

- Relation: `public.compound_drug_annotations`. Type: array. Unit: none stated.
- What it is: Disease areas declared by the source.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `indication` (V0300)

- Relation: `public.compound_drug_annotations`. Type: array. Unit: none stated.
- What it is: Indications declared by the source.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `drug_class` (V0301)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: Drug class declared by the source.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `activity_spectrum` (V0302)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: Activity spectrum declared by the source (antibacterials).
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_redistributable` (V0303)

- Relation: `public.compound_drug_annotations`. Type: boolean. Unit: none stated.
- What it is: Whether the annotation's source record may be redistributed.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `drug_annotation_version` (V0304)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: Version of the S1.6 stage.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `license_class` (V0305)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: Licence class of the annotation row, with no default: source_agreement (the class of the rows before 024: the licence of their source), cc_by_sa_3_0 (ChEMBL), cc_by_sa_4_0 (DrugCentral), cc_by_4_0 or undetermined (never redistributable, CHECK).
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_record_id` (V0306)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: The source's own id of the annotation, when it has one. With source_id it is unique where present (uq_drug_annotations_source_record), which makes a reload idempotent.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_version` (V0307)

- Relation: `public.compound_drug_annotations`. Type: text. Unit: none stated.
- What it is: Release of the source file the annotation was read from; NULL on the rows written before it.
- Origin: S1.6 annotations of the source records.
- How: S1.6 annotations of the source records
- NULL: May be NULL. NULL on the rows written before it. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `result` (V0308)

- Relation: `public.compound_drug_profile`. Type: text. Unit: none stated.
- What it is: found, absent or not_applicable (the absence is a row, decision (ak)).
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `chembl_id` (V0309)

- Relation: `public.compound_drug_profile`. Type: text. Unit: none stated.
- What it is: The ChEMBL molecule id read, one the compound holds in compound_xrefs_resolved; NULL when not_applicable.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. NULL when not_applicable. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `chembl_xref_db` (V0310)

- Relation: `public.compound_drug_profile`. Type: text. Unit: none stated.
- What it is: Generated, always chembl: the xref_db half of the foreign key of chembl_id to compound_xrefs_resolved.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `max_phase` (V0311)

- Relation: `public.compound_drug_profile`. Type: numeric. Unit: none stated.
- What it is: molecule_dictionary.max_phase: 4 approved, 3, 2, 1, 0.5 early phase 1, -1 phase unknown; NULL: ChEMBL holds no phase (preclinical).
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. NULL: ChEMBL holds no phase (preclinical). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `first_approval` (V0312)

- Relation: `public.compound_drug_profile`. Type: smallint. Unit: none stated.
- What it is: molecule_dictionary.first_approval, the year; NULL: not approved, or ChEMBL holds no year.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. NULL: not approved, or ChEMBL holds no year. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `withdrawn_flag` (V0313)

- Relation: `public.compound_drug_profile`. Type: boolean. Unit: none stated.
- What it is: molecule_dictionary.withdrawn_flag; the detail is in compound_drug_warnings.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `black_box_warning` (V0314)

- Relation: `public.compound_drug_profile`. Type: boolean. Unit: none stated.
- What it is: molecule_dictionary.black_box_warning; the detail is in compound_drug_warnings.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `prodrug` (V0315)

- Relation: `public.compound_drug_profile`. Type: boolean. Unit: none stated.
- What it is: molecule_dictionary.prodrug; NULL where ChEMBL writes -1 (not known).
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. NULL where ChEMBL writes -1 (not known). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `first_in_class` (V0316)

- Relation: `public.compound_drug_profile`. Type: boolean. Unit: none stated.
- What it is: molecule_dictionary.first_in_class; NULL where ChEMBL writes -1 (not known).
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. NULL where ChEMBL writes -1 (not known). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `oral` (V0317)

- Relation: `public.compound_drug_profile`. Type: boolean. Unit: none stated.
- What it is: molecule_dictionary.oral: a product with this route exists.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `parenteral` (V0318)

- Relation: `public.compound_drug_profile`. Type: boolean. Unit: none stated.
- What it is: molecule_dictionary.parenteral: a product with this route exists.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `topical` (V0319)

- Relation: `public.compound_drug_profile`. Type: boolean. Unit: none stated.
- What it is: molecule_dictionary.topical: a product with this route exists.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `availability_type` (V0320)

- Relation: `public.compound_drug_profile`. Type: smallint. Unit: none stated.
- What it is: molecule_dictionary.availability_type: -2 withdrawn, -1 unknown, 0 discontinued, 1 prescription only, 2 over the counter.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_version` (V0321)

- Relation: `public.compound_drug_profile`. Type: text. Unit: none stated.
- What it is: The ChEMBL release read (37).
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_class` (V0322)

- Relation: `public.compound_drug_profile`. Type: text. Unit: none stated.
- What it is: cc_by_sa_3_0, the ChEMBL licence.
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_redistributable` (V0323)

- Relation: `public.compound_drug_profile`. Type: boolean. Unit: none stated.
- What it is: Whether the row may go in the CC BY-SA package (the authorization of the chembl source).
- Origin: ChEMBL molecule_dictionary as read by the release.
- How: ChEMBL molecule_dictionary as read by the release
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `result` (V0324)

- Relation: `public.compound_drug_warnings`. Type: text. Unit: none stated.
- What it is: found, absent (the ChEMBL id has no warning) or not_applicable (no ChEMBL id).
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `warning_type` (V0325)

- Relation: `public.compound_drug_warnings`. Type: text. Unit: none stated.
- What it is: Withdrawn or Black Box Warning, as ChEMBL writes it.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `warning_class` (V0326)

- Relation: `public.compound_drug_warnings`. Type: text. Unit: none stated.
- What it is: drug_warning.warning_class (hepatotoxicity, cardiotoxicity...), as ChEMBL writes it; NULL where ChEMBL has none.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `country` (V0327)

- Relation: `public.compound_drug_warnings`. Type: text. Unit: none stated.
- What it is: drug_warning.warning_country; NULL where ChEMBL has none.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `warning_year` (V0328)

- Relation: `public.compound_drug_warnings`. Type: smallint. Unit: none stated.
- What it is: drug_warning.warning_year; NULL where ChEMBL has none.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `efo_id` (V0329)

- Relation: `public.compound_drug_warnings`. Type: text. Unit: none stated.
- What it is: drug_warning.efo_id, the adverse effect; NULL where ChEMBL has none.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ref_types` (V0330)

- Relation: `public.compound_drug_warnings`. Type: array. Unit: none stated.
- What it is: warning_refs.ref_type of each reference (DailyMed, FDA, WHO, DOI...), the order of ref_ids.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ref_ids` (V0331)

- Relation: `public.compound_drug_warnings`. Type: array. Unit: none stated.
- What it is: warning_refs.ref_id of each reference, the order of ref_types.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_version` (V0332)

- Relation: `public.compound_drug_warnings`. Type: text. Unit: none stated.
- What it is: The ChEMBL release read (37).
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_class` (V0333)

- Relation: `public.compound_drug_warnings`. Type: text. Unit: none stated.
- What it is: cc_by_sa_3_0, the ChEMBL licence.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_redistributable` (V0334)

- Relation: `public.compound_drug_warnings`. Type: boolean. Unit: none stated.
- What it is: Whether the row may go in the CC BY-SA package.
- Origin: ChEMBL drug_warning as read by the release.
- How: ChEMBL drug_warning as read by the release
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `result` (V0335)

- Relation: `public.compound_indications`. Type: text. Unit: none stated.
- What it is: found, absent (the ChEMBL id has no indication) or not_applicable (no ChEMBL id).
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `mesh_id` (V0336)

- Relation: `public.compound_indications`. Type: text. Unit: none stated.
- What it is: drug_indication.mesh_id (indexed); NULL where ChEMBL has only an EFO term.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: May be NULL. NULL where ChEMBL has only an EFO term. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `mesh_heading` (V0337)

- Relation: `public.compound_indications`. Type: text. Unit: none stated.
- What it is: drug_indication.mesh_heading, present exactly when mesh_id is.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `efo_id` (V0338)

- Relation: `public.compound_indications`. Type: text. Unit: none stated.
- What it is: drug_indication.efo_id (indexed); NULL where ChEMBL has only a MeSH id.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: May be NULL. NULL where ChEMBL has only a MeSH id. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `efo_term` (V0339)

- Relation: `public.compound_indications`. Type: text. Unit: none stated.
- What it is: drug_indication.efo_term, present exactly when efo_id is.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `max_phase_for_ind` (V0340)

- Relation: `public.compound_indications`. Type: numeric. Unit: none stated.
- What it is: drug_indication.max_phase_for_ind, the highest phase for this indication (4, 3, 2, 1, 0.5, -1); NULL where ChEMBL has none.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ref_types` (V0341)

- Relation: `public.compound_indications`. Type: array. Unit: none stated.
- What it is: indication_refs.ref_type of each reference (ClinicalTrials, DailyMed, ATC, EMA, FDA...), the order of ref_ids.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ref_ids` (V0342)

- Relation: `public.compound_indications`. Type: array. Unit: none stated.
- What it is: indication_refs.ref_id of each reference, the order of ref_types.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_version` (V0343)

- Relation: `public.compound_indications`. Type: text. Unit: none stated.
- What it is: The ChEMBL release read (37).
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_class` (V0344)

- Relation: `public.compound_indications`. Type: text. Unit: none stated.
- What it is: cc_by_sa_3_0, the ChEMBL licence.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_redistributable` (V0345)

- Relation: `public.compound_indications`. Type: boolean. Unit: none stated.
- What it is: Whether the row may go in the CC BY-SA package.
- Origin: ChEMBL drug_indication as read by the release.
- How: ChEMBL drug_indication as read by the release
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `result` (V0346)

- Relation: `public.compound_mechanisms`. Type: text. Unit: none stated.
- What it is: found, absent (the ChEMBL id has no mechanism) or not_applicable (no ChEMBL id).
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `mechanism_of_action` (V0347)

- Relation: `public.compound_mechanisms`. Type: text. Unit: none stated.
- What it is: drug_mechanism.mechanism_of_action, as ChEMBL writes it.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `action_type` (V0348)

- Relation: `public.compound_mechanisms`. Type: text. Unit: none stated.
- What it is: drug_mechanism.action_type (INHIBITOR, AGONIST, ANTAGONIST...); NULL where ChEMBL has none.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `target_chembl_id` (V0349)

- Relation: `public.compound_mechanisms`. Type: text. Unit: none stated.
- What it is: The ChEMBL id of the target (indexed); NULL where ChEMBL names no target.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: May be NULL. NULL where ChEMBL names no target. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `direct_interaction` (V0350)

- Relation: `public.compound_mechanisms`. Type: boolean. Unit: none stated.
- What it is: drug_mechanism.direct_interaction; NULL where ChEMBL has none.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `molecular_mechanism` (V0351)

- Relation: `public.compound_mechanisms`. Type: boolean. Unit: none stated.
- What it is: drug_mechanism.molecular_mechanism; NULL where ChEMBL has none.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `disease_efficacy` (V0352)

- Relation: `public.compound_mechanisms`. Type: boolean. Unit: none stated.
- What it is: drug_mechanism.disease_efficacy; NULL where ChEMBL has none.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: May be NULL. NULL where ChEMBL has none. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ref_types` (V0353)

- Relation: `public.compound_mechanisms`. Type: array. Unit: none stated.
- What it is: mechanism_refs.ref_type of each reference (PubMed, FDA, DailyMed...), the order of ref_ids.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `ref_ids` (V0354)

- Relation: `public.compound_mechanisms`. Type: array. Unit: none stated.
- What it is: mechanism_refs.ref_id of each reference, the order of ref_types; NULL where ChEMBL records the reference with no id, only at a position whose ref_type is Expert, never an empty or blank string.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_version` (V0355)

- Relation: `public.compound_mechanisms`. Type: text. Unit: none stated.
- What it is: The ChEMBL release read (37).
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_class` (V0356)

- Relation: `public.compound_mechanisms`. Type: text. Unit: none stated.
- What it is: cc_by_sa_3_0, the ChEMBL licence.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_redistributable` (V0357)

- Relation: `public.compound_mechanisms`. Type: boolean. Unit: none stated.
- What it is: Whether the row may go in the CC BY-SA package.
- Origin: ChEMBL drug_mechanism as read by the release.
- How: ChEMBL drug_mechanism as read by the release
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `scheme` (V0358)

- Relation: `public.compound_drug_classes`. Type: text. Unit: none stated.
- What it is: mesh_pharmacological_action, fda_epc, source_declared or atc.
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `class_code` (V0359)

- Relation: `public.compound_drug_classes`. Type: text. Unit: none stated.
- What it is: Code of the class in its scheme (MeSH descriptor id, EPC code, ATC code); NULL only for source_declared (CHECK).
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: May be NULL. NULL only for source_declared (CHECK). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `class_label` (V0360)

- Relation: `public.compound_drug_classes`. Type: text. Unit: none stated.
- What it is: Name of the class as the scheme or the source gives it; never blank.
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `basis` (V0361)

- Relation: `public.compound_drug_classes`. Type: text. Unit: none stated.
- What it is: declared (the source states the class for this compound) or derived (through a cross-reference).
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `derived_from` (V0362)

- Relation: `public.compound_drug_classes`. Type: text. Unit: none stated.
- What it is: For a derived row, the cross-reference used: xref:pubchem_cid, xref:chembl or xref:chebi. NULL for a declared row (CHECK).
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: May be NULL. NULL for a declared row (CHECK). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_record_id` (V0363)

- Relation: `public.compound_drug_classes`. Type: text. Unit: none stated.
- What it is: The source's own id of the assertion, when it has one.
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_version` (V0364)

- Relation: `public.compound_drug_classes`. Type: text. Unit: none stated.
- What it is: Release of the source file the row was read from. Never blank.
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_class` (V0365)

- Relation: `public.compound_drug_classes`. Type: text. Unit: none stated.
- What it is: nlm_mesh_terms, us_public_domain, source_agreement, cc_by_sa_3_0, cc_by_sa_4_0, who_atc_restricted (ATC only) or undetermined.
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_redistributable` (V0366)

- Relation: `public.compound_drug_classes`. Type: boolean. Unit: none stated.
- What it is: A mark, never a filter (decision (hp)); false for ATC and for undetermined (CHECK).
- Origin: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable).
- How: MeSH pharmacological action, FDA EPC, source-declared class, ATC (ATC is not redistributable)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: per row, see license_class.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

## Sources, provenance and licence

### `is_redistributable` (V0023)

- Relation: `public.compounds`. Type: boolean. Unit: none stated.
- What it is: True when at least one compound_sources row of this compound is redistributable (decision F1; since (ib), 2026-10-14, every source is). Written by the loader from compound_sources_v1 and checked against compound_sources after the load.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_tier` (V0032)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Licence tier of the compound in the open distribution (migration 008, decision (ie); label renamed by migration 011): 'cc_by_sa' = AURORA package (CC BY-SA 4.0, v_open_cc_by_sa) when at least one redistributable link is CC BY-SA; 'cc_by_nc' = AURORA-NC package (CC BY-NC 4.0, v_open_cc_by_nc) when every redistributable link is NC; with no redistributable link, the same rule over all links; NULL = no source link.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. NULL = no source link. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_redistributable` (V0040)

- Relation: `public.compound_names`. Type: boolean. Unit: none stated.
- What it is: Whether the name's source record may be redistributed.
- Origin: Names read from the source records (S2.8 stage of the pipeline).
- How: Names read from the source records (S2.8 stage of the pipeline)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_redistributable` (V0048)

- Relation: `public.compound_xrefs_resolved`. Type: boolean. Unit: none stated.
- What it is: Whether the identifier may be redistributed.
- Origin: Identifiers resolved from the InChIKey by public services (S2.10 stage).
- How: Identifiers resolved from the InChIKey by public services (S2.10 stage)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `doi` (V0237)

- Relation: `public.compound_references`. Type: text. Unit: none stated.
- What it is: Bibliographic DOI reporting the compound, source-provided (e.g. from COCONUT's pipe-separated 'dois' column).
- Origin: DOIs declared by the sources.
- How: DOIs declared by the sources
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `source_key` (V0238)

- Relation: `public.compound_references`. Type: text. Unit: none stated.
- What it is: Key of the source this reference came from.
- Origin: DOIs declared by the sources.
- How: DOIs declared by the sources
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `created_at` (V0239)

- Relation: `public.compound_references`. Type: timestamp with time zone. Unit: none stated.
- What it is: Row insertion timestamp.
- Origin: DOIs declared by the sources.
- How: DOIs declared by the sources
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_identifier` (V0240)

- Relation: `public.compound_sources`. Type: text. Unit: none stated.
- What it is: Native identifier from the source for this link, when one exists.
- Origin: Link of a compound to a source record, with the licence tier of the link.
- How: Link of a compound to a source record, with the licence tier of the link
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `source_subset` (V0241)

- Relation: `public.compound_sources`. Type: text. Unit: none stated.
- What it is: Named subset within the source for this link, e.g. NExT, DIV7, AODXI.
- Origin: Link of a compound to a source record, with the licence tier of the link.
- How: Link of a compound to a source record, with the licence tier of the link
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_primary` (V0242)

- Relation: `public.compound_sources`. Type: boolean. Unit: none stated.
- What it is: Whether this source is the tie-break 'primary' source when the compound has multiple sources
- Origin: Link of a compound to a source record, with the licence tier of the link.
- How: Link of a compound to a source record, with the licence tier of the link
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `is_redistributable` (V0243)

- Relation: `public.compound_sources`. Type: boolean. Unit: none stated.
- What it is: Whether this compound may be redistributed under CC BY 4.0 on the strength of this source (spec v1.8.0, F1), as decided in the private pipeline from configs/sources.yaml and shipped in compound_sources_v1.parquet.
- Origin: Link of a compound to a source record, with the licence tier of the link.
- How: Link of a compound to a source record, with the licence tier of the link
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `license_tier` (V0244)

- Relation: `public.compound_sources`. Type: text. Unit: none stated.
- What it is: Licence tier of this link = sources.license_tier of its source, set by the trigger compound_sources_license_tier: 'cc_by_sa' goes to the AURORA package (CC BY-SA 4.0), 'cc_by_nc' to AURORA-NC (CC BY-NC 4.0).
- Origin: Link of a compound to a source record, with the licence tier of the link.
- How: Link of a compound to a source record, with the licence tier of the link
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `is_redistributable` (V0266)

- Relation: `public.compound_activities`. Type: boolean. Unit: none stated.
- What it is: A mark, never a filter (decision (hp)): true only for a class the founder cleared. An undetermined record can never be true (CHECK compound_activities_licence_check). For the older rows, copied from the compound_sources link of the same compound and source.
- Origin: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release.
- How: ChEMBL, BindingDB and Iracema measurements, loaded from the activity Parquet of the release
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: no.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

## Collections and membership

### `collection_tags` (V0009)

- Relation: `public.compounds`. Type: array. Unit: none stated.
- What it is: TEXT[] (collection_tags across every source this compound came from; GIN-indexed. Not to be confused with the singular `collection` column.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `collection` (V0018)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Enumerated via CHECK: 'main' or 'cofactors', organic-vs-cofactor triage rule over canonical_smiles (no carbon / no C-C or C-H bond / <=1 heavy atom)
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `collection_slug` (V1980)

- Relation: `view v_collection_members / v_pkg_sa_collection_members`. Type: text. Unit: none stated.
- What it is: Slug of a collection the compound belongs to (view v_collection_members).
- Origin: Membership export of the ATHANOR pipeline, loaded by scripts/load.py.
- How: Membership is computed from collection rules and exported with the bundles.
- NULL: Never NULL on a membership row; a compound outside a collection has no row. Domain: open (collection registry).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `membership_license` (V1981)

- Relation: `view v_collection_members / v_pkg_sa_collection_members`. Type: text. Unit: none stated.
- What it is: Licence of the membership row of the package view.
- Origin: Membership export of the ATHANOR pipeline, loaded by scripts/load.py.
- How: Carried from the licence tier of the compound's links.
- NULL: Never NULL on a membership row; a compound outside a collection has no row. Domain: open (collection registry).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

## Quality flags

### `checker_score` (V0012)

- Relation: `public.compounds`. Type: smallint. Unit: none stated.
- What it is: Numeric score from the standardization/checker step (SMALLINT).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `qc_status` (V0013)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: 'passed' when at least one source record of this compound passed curation (compound_identity_v1.curation_passed), 'quarantined' when none did. 'rejected' records never receive an identity. Quarantined compounds are kept and marked (see compounds.curation_passed).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `partial_reason` (V0019)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: NULL = complete compound (tier 'full' in compound_identity_v1: SDF, PDBQT and approved 3D).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. NULL = complete compound (tier 'full' in compound_identity_v1: SDF, PDBQT and approved 3D). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `stereo_undefined_in_source` (V0020)

- Relation: `public.compounds`. Type: boolean. Unit: none stated.
- What it is: True when the curated structure leaves at least one tetrahedral centre OR one double bond without defined stereo (v1.8.0; until v1.7 the flag lived only in conformers and counted tetrahedral centres only).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `n_stereo_undefined_tetrahedral` (V0021)

- Relation: `public.compounds`. Type: integer. Unit: count.
- What it is: Tetrahedral centres left undefined in the curated structure (compound_identity_v1).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `n_stereo_undefined_double_bond` (V0022)

- Relation: `public.compounds`. Type: integer. Unit: count.
- What it is: Double bonds left without E/Z in the curated structure (compound_identity_v1).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `curation_passed` (V0024)

- Relation: `public.compounds`. Type: boolean. Unit: none stated.
- What it is: MARK. GENERATED (qc_status = 'passed'): at least one source record of this compound passed curation (compound_identity_v1.curation_passed, checked equal to compound_curation_v1.curation_passed by the loader).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `tier` (V0025)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: GENERATED from partial_reason: 'full' (3D geometry, SDF and PDBQT) or 'partial' (identity and 2D data only).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `readiness_passed` (V0026)

- Relation: `public.compounds`. Type: boolean. Unit: none stated.
- What it is: Docking-readiness verdict of the private pipeline (N14) when the bundle carries it (optional column compound_identity_v1.readiness_passed); NULL when the bundle does not, and always NULL for the partial tier, which has no docking file.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. NULL when the bundle does not, and always NULL for the partial tier, which has no docking file. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `review_required` (V0029)

- Relation: `public.compounds`. Type: boolean. Unit: none stated.
- What it is: MARK: the adjudication left something for a human to look at (an organic parent kept from a salt, a radical with a closed-shell alternative recorded, an unusual valence, an unresolved record). Never a reason to drop the compound. NULL = the release did not carry compound_curation_v1.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. NULL = the release did not carry compound_curation_v1. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `review_reason` (V0030)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Why review_required is true, as written by the pipeline (compound_curation_v1); NULL when no review is required.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. NULL when no review is required. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `adjudication` (V0031)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Outcome of the quarantine adjudication for the compound's quarantined records (compound_curation_v1.adjudication): resolved_same_identity | resolved_corrected_identity | unresolved | mixed. NULL = the compound had no quarantined record (or the release did not carry the Parquet).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. NULL = the compound had no quarantined record (or the release did not carry the Parquet). Domain: Closed list: resolved_same_identity, resolved_corrected_identity, unresolved, mixed.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `converged` (V0085)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Whether the minimization step reported convergence.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `inchikey_roundtrip_ok` (V0088)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Whether recomputing the InChIKey from the 3D structure matches the record's InChIKey.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `stereo_preserved` (V0089)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Gate v1.0.0 stereochemistry-preserved flag, superseded as the acceptance criterion by defined_stereo_preserved, which masks stereo elements the source left undefined before comparing.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `skeleton_ok` (V0094)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Gate v1.1.0 criterion: whether the first block of the InChIKey (connectivity/skeleton) survived 3D generation.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `defined_stereo_preserved` (V0095)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Gate v1.1.0 criterion: whether the stereo elements the source actually defined survived 3D generation; elements left undefined at the source are masked out before comparing.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `valence_preserved` (V0096)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Gate v1.1.0 criterion: whether atom valence stayed chemically valid after generation/minimization.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `energy_finite` (V0097)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Gate v1.1.0 criterion: whether the computed energy is a finite value.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `no_atom_clash` (V0098)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Gate v1.1.0 criterion: absence of overlapping/clashing atoms in the generated geometry.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `gate_passed` (V0099)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Conjunction of skeleton_ok, defined_stereo_preserved, valence_preserved, energy_finite and no_atom_clash. CHECK enforces gate_passed equals that AND, and that all six gate columns are either all NULL together or all filled together (num_nonnulls(...) IN (0,6)).
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. CHECK enforces gate_passed equals that AND, and that all six gate columns are either all NULL together or all filled together (num_nonnulls(...) IN (0,6)). Domain: true or false.
- Example: first data row of the v2.0.0 bioactivity-space TSV: true.
- Files: admet_tsv, descriptors_tsv, descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: yes. In aurora_prod: yes. Status: served.

### `stereo_undefined_in_source` (V0100)

- Relation: `public.conformers`. Type: boolean. Unit: none stated.
- What it is: Conformer stage's flag: tetrahedral centres left undefined at the source only. Kept as shipped in conformer_provenance_v1. The authoritative, wider flag (centres AND double bonds) is compounds.stereo_undefined_in_source since v1.8.0.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `n_stereo_undefined` (V0101)

- Relation: `public.conformers`. Type: smallint. Unit: count.
- What it is: Conformer stage's count of undefined tetrahedral centres. See compounds.n_stereo_undefined_tetrahedral / n_stereo_undefined_double_bond.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `failure_reason` (V0102)

- Relation: `public.conformers`. Type: text. Unit: none stated.
- What it is: Free-text reason recorded when the gate did not pass.
- Origin: Conformer stage of the pipeline, minimizer and gate recorded per conformer.
- How: Conformer stage of the pipeline, minimizer and gate recorded per conformer
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: descriptors_tsv, descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `validity_passed` (V0104)

- Relation: `public.geometry_validity`. Type: boolean. Unit: none stated.
- What it is: The S4.4 verdict: N08 gate AND every geometric check passed.
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `n08_gate_passed` (V0105)

- Relation: `public.geometry_validity`. Type: boolean. Unit: none stated.
- What it is: The N08 chemical gate of the conformer stage (conformers.gate_passed for the full tier).
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: Never NULL. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `bond_lengths_ok` (V0106)

- Relation: `public.geometry_validity`. Type: boolean. Unit: none stated.
- What it is: PoseBusters-style bond-length check (bounds from the distance-geometry matrix); NULL when N08 failed (no geometry to check).
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: May be NULL. NULL when N08 failed (no geometry to check). Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `bond_angles_ok` (V0107)

- Relation: `public.geometry_validity`. Type: boolean. Unit: none stated.
- What it is: Bond-angle check; NULL when N08 failed.
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: May be NULL. NULL when N08 failed. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `internal_clash_ok` (V0108)

- Relation: `public.geometry_validity`. Type: boolean. Unit: none stated.
- What it is: Internal steric clash check; NULL when N08 failed.
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: May be NULL. NULL when N08 failed. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `aromatic_ring_flatness_ok` (V0109)

- Relation: `public.geometry_validity`. Type: boolean. Unit: none stated.
- What it is: Aromatic ring flatness check; NULL when N08 failed.
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: May be NULL. NULL when N08 failed. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `double_bond_flatness_ok` (V0110)

- Relation: `public.geometry_validity`. Type: boolean. Unit: none stated.
- What it is: C=C flatness check; NULL when N08 failed.
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: May be NULL. NULL when N08 failed. Domain: true or false.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `failure_reasons` (V0111)

- Relation: `public.geometry_validity`. Type: array. Unit: none stated.
- What it is: Why the gate failed, as written by the pipeline (one entry per failed check, up to 3 in v1.8.0); NULL exactly when validity_passed. N08 messages are in Portuguese in v1.8.0.
- Origin: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks).
- How: S4.4 3D validity gate (N08 chemical gate plus PoseBusters-style geometric checks)
- NULL: May be NULL. NULL exactly when validity_passed. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `gate_passed` (V1822)

- Relation: `descriptors3d TSV column (from descriptors3d_v1)`. Type: boolean. Unit: none stated.
- What it is: Whether the conformer passed the geometry gate; 3D descriptors are only given for passed conformers.
- Origin: descriptors3d_v1 Parquet of the release.
- How: Carried from the pipeline into the TSV of the bundle.
- NULL: Empty means absent. Domain: true or false.
- Example: first data row of the v2.0.0 bioactivity-space TSV: true.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

### `failure_reason` (V1823)

- Relation: `descriptors3d TSV column (from descriptors3d_v1)`. Type: text. Unit: none stated.
- What it is: Why the gate did not pass, as the pipeline wrote it.
- Origin: descriptors3d_v1 Parquet of the release.
- How: Carried from the pipeline into the TSV of the bundle.
- NULL: Empty means absent. Domain: open.
- Example: none in the files read for this task.
- Files: descriptors3d_tsv. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: yes. In aurora_prod: yes. Status: in the database, not served in this release.

## Version and identifier history

### `curation_version` (V0011)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: Version string of the curation/standardization pipeline that produced this row.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `created_at` (V0016)

- Relation: `public.compounds`. Type: timestamp with time zone. Unit: none stated.
- What it is: Timestamp the row was created; defaults to now.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `superseded_by_seq` (V0027)

- Relation: `public.compounds`. Type: integer. Unit: none stated.
- What it is: alchemia_seq of the compound that carries the corrected identity (S2.3, compound_curation_v1).
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `superseded_by` (V0028)

- Relation: `public.compounds`. Type: text. Unit: none stated.
- What it is: GENERATED ('ALC' || superseded_by_seq): the public id of the superseding compound. Same fact as superseded_by_seq, in the form the catalog shows.
- Origin: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py.
- How: Curated identity of the ATHANOR pipeline (compound_identity_v1), loaded by scripts/load.py
- NULL: May be NULL. The column comment does not say what NULL means (open question OQ6). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `old_alchemia_seq` (V0066)

- Relation: `public.alchemia_id_history`. Type: integer. Unit: none stated.
- What it is: The seq of the id in release 1.9.0 (primary key: one row per old id).
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `old_alchemia_id` (V0067)

- Relation: `public.alchemia_id_history`. Type: text. Unit: none stated.
- What it is: 9.0.
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `new_alchemia_seq` (V0068)

- Relation: `public.alchemia_id_history`. Type: integer. Unit: none stated.
- What it is: The seq the same compound carries from 2.0.0 on (unique among renumbering_ah rows: one old id per new id); for merged_into_parent the seq of the main piece it was merged into; NULL when the id was retired (removed_non_organic). Migration 032.
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: May be NULL. NULL when the id was retired (removed_non_organic). Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

### `new_alchemia_id` (V0069)

- Relation: `public.alchemia_id_history`. Type: text. Unit: none stated.
- What it is: 0.0 on (of the main piece, for a merge); NULL when the id was retired.
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: May be NULL. NULL when the id was retired. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `renumbered_in` (V0070)

- Relation: `public.alchemia_id_history`. Type: text. Unit: none stated.
- What it is: The release version that renumbered (2.0.0); the loader requires it to be the version being loaded.
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `reason` (V0071)

- Relation: `public.alchemia_id_history`. Type: text. Unit: none stated.
- What it is: Closed list: renumbering_ah (the founder's decision (ah) of 2026-10-28; a new id and a new area) or removed_non_organic (decision (as) of 2026-10-28, migration 032: no new id, no new area; the compound is not in the release that renumbered) or merged_into_parent.
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: Never NULL. Domain: Closed list: renumbering_ah (the founder's decision (ah) of 2026-10-28; a new id and a new area) or removed_non_organic (decision (as) of 2026-10-28, migration 032: no new id, no new area; the compound is not in the release that renumbered) or merged_into_parent.
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `old_area` (V0072)

- Relation: `public.alchemia_id_history`. Type: text. Unit: none stated.
- What it is: complete or incomplete: the area of the compound in release 1.9.0.
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: Never NULL. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `new_area` (V0073)

- Relation: `public.alchemia_id_history`. Type: text. Unit: none stated.
- What it is: complete or incomplete: the area of the compound in the release that renumbered; NULL when the id was retired.
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: May be NULL. NULL when the id was retired. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: yes. In the files: no. In aurora_prod: yes. Status: served.

### `parent_inchikey` (V0074)

- Relation: `public.alchemia_id_history`. Type: text. Unit: none stated.
- What it is: For merged_into_parent: the full InChIKey of the main piece the old id was merged into, the anchor scripts/load.py and the verifier V2 check against the compound at the new id; NULL for the other reasons. Migration 032.
- Origin: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032.
- How: Append-only registry of the renumbering of 2.0.0, migrations 031 and 032
- NULL: May be NULL. NULL for the other reasons. Domain: open (no closed list in the schema).
- Example: none in the files read for this task.
- Files: none. AURORA CC BY-SA: yes; AURORA-NC CC BY-NC: yes.
- Served: no. In the files: no. In aurora_prod: yes. Status: in the database, not served in this release.

## Limits of this dictionary

- The mark 'in aurora_prod' comes from the schema, the migrations and the loader. It was not rechecked on the VM today (the deploy is today and the VM is frozen).
- The mark 'served' comes from reading the API role file and the platform code on this machine today. It says what the API is built to return, not what a live request returned today.
- The mark 'in the files' comes from the columns lists of the v2.0.0 variable bundles and the manifest of the other bundles. The bundles are not published yet.
- Technical keys (compound_uuid and the internal ids of rows) and relations that are not about one molecule (sources, BI tables, release statistics) have no entry.
- Examples come from the first data row of the bundle TSV of the public package or from the file samples of the release. Where none exists the entry says so.
- The NC package has the same fields; nothing about its values, ids or counts per collection or source is published here.
- The previous table-by-table reference, generated from a live schema on 2026-11-17, was replaced by this file. The generator of that reference, scripts/generate_data_dictionary.py, now writes to docs/DATA_DICTIONARY_SCHEMA_DUMP.md and no longer touches this file.

## Open questions

- **OQ1, Dimorphite-DL version.** docs/REFERENCES.md shows both 2.0.2 and 2.1.0. The dictionary names the tool without a version for protonation until the founder or the pipeline owner says which one produced the release.
- **OQ2, ADMET percentile keys in the bundle TSV.** The TSV carries the model predictions only. The DrugBank percentile keys are in the database and in the features endpoint, not in the TSV (decision D5 is open).
- **OQ3, Fingerprint MACCS width.** Two figures are recorded and the reason for the gap is not proved here. The database width of the MACCS column is 168, as measured by the cartridge call size(maccs_fp('CCO'::mol)) that scripts/variables_per_molecule.py:472 runs and that scripts/variables_per_molecule.v1.json:11416 records. The bundle export declares 167 bits in 21 bytes (scripts/export_fingerprint_bundle.py:78); 21 bytes hold 168 bits. The usual explanation, that RDKit numbers MACCS keys from 1 and leaves position 0 unused, was not confirmed: RDKit is not installed in this session and no fingerprint Parquet of the bundle is on disk. Stays open. The dictionary gives each figure where it applies.
- **OQ4, Drug-likeness rules with publishable false.** Every rule row of druglikeness_rules except Lipinski and Veber had publishable false when the dashboard aggregate was measured on 2026-11-18, so the flag view returns no row. The state after that is not rechecked here. A false value means: shown nowhere, not an answer about the compound.
- **OQ5, Mordred names without a family text.** Mordred is described by family where the family is certain. Names that fit no family rule carry a generic text; no per-descriptor definition is invented.
- **OQ6, NULL meaning not documented.** Where a column comment does not say what NULL means, the entry says so instead of guessing.
- **OQ7, RDKit version in two places.** Reported, not decided. docs/REFERENCES.md:186 gives RDKit 2026.03.4 for the library; docs/REFERENCES.md:189 says the cartridge in the database image is RDKit 2026.03.2. Which version computed which stored value was not established here. The entries that name a version cite 2026.03.4 because that is the version in REFERENCES; that is a citation, not a finding.
- **OQ8, Per-field display in the Explorer.** 'Served' means the API role can read the column and the platform returns it. Which fields the Explorer pages show was not checked field by field.
- **OQ9, Units of 3D shape descriptors.** RDKit does not label the unit of the principal moments; none is stated here.

## Inputs

| Input | sha256 |
|---|---|
| softwares/aurora-platform/backend/deploy/sql/aurora_api_role.sql | `c953d5305e33` |
| bioactivity-space-admet.tar.zst (v2.0.0 variable bundle, local) | `67100ba7132a` |
| bioactivity-space-descriptors.tar.zst (v2.0.0 variable bundle, local) | `549ffbb92533` |
| bioactivity-space-descriptors3d.tar.zst (v2.0.0 variable bundle, local) | `31b059d5f5c0` |
| dist/data_dictionary.json | `41911fa0268d` |
| scripts/variables_per_molecule.v1.json | `d116625f5909` |
| docs/qc/2026-11-18-numeros-para-stats.json | `67ee17020403` |
