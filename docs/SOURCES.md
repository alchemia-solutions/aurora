# Sources

[Repository home](../README.md) · [Docs index](README.md)

**State on 2026-11-20.** The list below is the one the platform's summary shows for release 2.0.0. Release 2.0.0
is not published. BindingDB is not on it because it is not a source of compounds: its measurements enter only
as bioactivity rows about compounds AURORA already holds, each row with its own licence.

AURORA draws on public collections. It does not redistribute the raw dumps: for those, go to the original
projects. Attribution names Alchemia LTDA for the curation and aggregation, and it does not replace the
original sources. If you publish work built on a subset, cite the upstream projects too.

Where a source states terms, they are the source's words as read on 2026-10-14 (ChEBI: 2026-10-15), not a
promise of ours. Read the terms at the source before you build on its data. "Package of the source" is the set
the source belongs to: a compound goes to AURORA when at least one of its sources is in the AURORA set, and to
AURORA-NC otherwise.

## Sources that contribute to the registry

| Source | What it contributes | Package of the source | Terms as recorded | Reference |
|---|---|---|---|---|
| **COCONUT 2.0** (COlleCtion of Open NatUral producTs), including its ZINC NP fraction | Natural products | AURORA | The download page releases the data under CC0; the licences of its individual collections were not re-read | [10.1093/nar/gkae1063](https://doi.org/10.1093/nar/gkae1063) · [10.1186/s13321-020-00478-9](https://doi.org/10.1186/s13321-020-00478-9) · ZINC NP: [10.1021/acs.jcim.5b00559](https://doi.org/10.1021/acs.jcim.5b00559) |
| **NCI / DTP** Open Chemical Repository | Compounds with public-domain structures | AURORA | The program calls "Open" the compounds whose structures are in the public domain | No paper. Developmental Therapeutics Program, RRID:SCR_003057, [dtp.cancer.gov](https://dtp.cancer.gov/) |
| **ChEBI** | Compounds and identifiers | AURORA | CC BY 4.0, subject to the terms of use of EMBL-EBI | [10.1093/nar/gkaf1271](https://doi.org/10.1093/nar/gkaf1271) |
| **ChEMBL** 37 | Compounds and bioactivity rows | AURORA | CC BY-SA 3.0; each row carries the ChEMBL identifier and the release number | [10.1093/nar/gkad1004](https://doi.org/10.1093/nar/gkad1004) |
| **BrNPDB** (successor of NuBBEDB) | Brazilian natural products | AURORA | No data licence stated on the site | [10.1021/np3006875](https://doi.org/10.1021/np3006875) · [10.1038/s41598-017-07451-x](https://doi.org/10.1038/s41598-017-07451-x) |
| **BraCoLi** v1 | Brazilian compounds | AURORA | No data licence stated on the site | [10.1007/s11030-022-10386-9](https://doi.org/10.1007/s11030-022-10386-9) |
| **IRACEMA** | Brazilian bioactive compounds | AURORA | No data licence stated on the site; the 2026 article is CC BY 4.0, which covers the article | [10.1021/acsomega.5c11939](https://doi.org/10.1021/acsomega.5c11939) · database: [iracema.ccen.ufpb.br](https://iracema.ccen.ufpb.br/) |
| **TCMBank** | Ingredients of herbal medicines | AURORA-NC | No data licence stated; the site calls itself non-commercial | [10.1039/d3sc02139d](https://doi.org/10.1039/d3sc02139d) · [10.1038/s41392-023-01339-1](https://doi.org/10.1038/s41392-023-01339-1) |
| **Drug Repurposing Hub** (Broad Institute) | Compounds of a drug library | AURORA-NC | The file states it is provided for non-commercial use only | [10.1038/nm.4306](https://doi.org/10.1038/nm.4306) |
| **AntibioticDB** (GARDP) | Antibacterial compounds | AURORA-NC | Terms for personal, non-medical, non-commercial or educational use | [10.1021/acsinfecdis.5c00955](https://doi.org/10.1021/acsinfecdis.5c00955) · [10.1093/jac/dky208](https://doi.org/10.1093/jac/dky208) |

The licence status of each source for the ShareAlike condition of the main package is under review. This
page makes no statement about redistributing data from the sources marked "No data licence stated".

The AURORA-NC package groups the compounds whose source licence does not allow commercial use. No package
is published.

## How to cite a source

Cite the references in the tables above. Where a source asks for a sentence, it is this one:

- **BrNPDB:** Valli et al., Journal of Natural Products, 2013 (https://doi.org/10.1021/np3006875) and Pilon et al., Scientific Reports, 2017 (https://doi.org/10.1038/s41598-017-07451-x).
- **IRACEMA:** Lourenco, T. A.; Costa, R. P. O.; Melo, L. F. M.; Ferreira, U. A.; Alves, E. H. P.; Oliveira-Filho, L. P.; Scotti, L.; Scotti, M. T.; Trossini, G. H. G. IRACEMA: A Database Management System for Bioactive Compounds Obtained and Characterized by Brazilian Researchers. ACS Omega 2026, 11 (15), 22807-22815. https://doi.org/10.1021/acsomega.5c11939
- **NCI / DTP:** "Developmental Therapeutics Program (RRID:SCR_003057)", https://dtp.cancer.gov/
- **Drug Repurposing Hub:** Corsello SM, et al. Nature Medicine. 2017 Apr 7;23(4):405-408. doi: 10.1038/nm.4306.
- **AntibioticDB:** the terms ask that you "appropriately and expressly acknowledge all Content and its source" (clause 4C). Cite Galarion et al., ACS Infectious Diseases, 2026 (https://doi.org/10.1021/acsinfecdis.5c00955) and Farrell et al., Journal of Antimicrobial Chemotherapy, 2018 (https://doi.org/10.1093/jac/dky208).
- **TCMBank:** the site makes no citation request that was found; cite Lv et al., Chemical Science, 2023 (https://doi.org/10.1039/d3sc02139d) and Lv et al., Signal Transduction and Targeted Therapy, 2023 (https://doi.org/10.1038/s41392-023-01339-1).
- **ChEMBL:** the identifier and release number of each row are in the file; cite Zdrazil et al., Nucleic Acids Research, 2024 (https://doi.org/10.1093/nar/gkad1004).

## Not included

The ZINC natural-product subset arrives through COCONUT. ZINC20, MolPort and Enamine are not included, and
no identifier of a commercial catalogue is kept.
