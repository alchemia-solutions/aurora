# FAQ

[Repository home](../README.md) · [Docs index](README.md)

**Is the pipeline open source?**
No. The data is released under Creative Commons licences. The ATHANOR pipeline is private, and nothing in
this repository grants a right in it.

**Can I download the database?**
Not openly. The packages are built and staged in object storage, but release 2.0.0 is not published and no
date is promised. The platform is meant to hand the files to approved accounts: see
[Download and access](../README.md#download-and-access) and [Packages](../README.md#packages).

**Can I use the API?**
The API needs a Bearer token from an approved account, except for the health probes, the sign-in doors and
one route of aggregates ([API.md](API.md)). The platform is a closed beta. The Terms of Use and the Privacy Policy are in version 1.1 since platform 1.5.2 (2026-11-23). Sign-up is open by
request: a new account is pending until an administrator approves it. With an approved account you can create a
read-only API key in Profile. Step by step: [QUICKSTART.md](QUICKSTART.md).

**Which pages of the platform are open?**
Only the Home page and the sign-in page, checked on 2026-11-25. Every other page asks you to sign in with an
approved account. No page is promised to stay open.

**Which licence covers what?**
The documentation is CC BY-SA 4.0, and so are the figures, except the names, wordmarks and symbols inside
them, which are not licensed. The AURORA package is under CC BY-SA 4.0 and the AURORA-NC package
under CC BY-NC 4.0; neither is published yet. The code in `examples/` and `scripts/` is Apache-2.0. See [LICENSE](../LICENSE) and
[LICENSE-CODE](../LICENSE-CODE).

**What terms apply to the data?**
The main package is under CC BY-SA 4.0 and the companion package, AURORA-NC, under CC BY-NC 4.0. Each compound belongs to exactly one package.
The official licence texts govern: read them at the links in [LICENSE](../LICENSE). Each source keeps its
own terms, and the licence status of some sources for the ShareAlike condition is not settled. No package is published yet.

**What does "complete" mean?**
A compound with an approved 3D geometry, a docking file and the core feature tables. Some exhaustive
descriptors are missing on some compounds. Compounds without an approved geometry are kept in a separate, marked area.

**Does "docking-ready" mean it is ready for my target?**
No. It means the files passed the pipeline checks. Protonation and tautomer states are not validated for
every target.

**How many compounds does release 2.0.0 have?**
The complete compounds of the release are split in two packages, AURORA and AURORA-NC, and the two add up to
the complete set. The incomplete compounds are kept apart and are in no package. The figures, with their
dates, are in the [README](../README.md#at-a-glance). Release 2.0.0 is not published.

**Does AURORA have bioactivity data?**
The release database of 2.0.0 holds bioactivity measurements about the compounds AURORA holds, each row with its own
licence, and not every row is redistributable. The platform serves them on the compound page to a signed-in approved account (2026-11-25), not to an API key. AURORA does not replace
ChEMBL as a bioactivity reference.

**Are the ADMET values measured?**
No. They are predictions with an applicability domain. Use them for triage.

**How do I cite it?**
Cite AURORA by name and publisher, the release you used and the date you accessed it. The release is shown
on the platform. There is no DOI. Cite the upstream sources you used too, listed in [SOURCES.md](SOURCES.md).

**How do I register a study or suggest a database for ATHANOR?**
Use [Collaborate](https://aurora.alchemia.solutions/collaborate) on the platform.

**Where do I report a problem or a security issue?**
Problems: open an issue. Security: [SECURITY.md](../SECURITY.md). Anything else: contact@alchemia.solutions.
