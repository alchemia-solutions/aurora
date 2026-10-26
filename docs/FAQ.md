# FAQ

**Is the pipeline open source?**
No. The data is released under Creative Commons licences. The ATHANOR pipeline is private, and nothing in
this repository grants a right in it.

**Can I download the database?**
Not yet. No download package is published.

**Can I use the API?**
The API answers in a closed beta, for approved testers. Without a token it answers 401.

**Which licence covers what?**
The AURORA package, the documentation and the figures are CC BY-SA 4.0. The AURORA-NC package is
CC BY-NC 4.0. The code in `examples/` and `scripts/` is Apache-2.0. See [LICENSE](../LICENSE) and
[LICENSE-CODE](../LICENSE-CODE).

**Can I use AURORA commercially?**
The main package is licensed under CC BY-SA 4.0, which allows commercial use under its ShareAlike
condition. No package is published yet, and the AURORA-NC package does not allow commercial use.

**What does "complete" mean?**
A compound with an approved 3D geometry, a docking file and the core feature tables. Some exhaustive
descriptors are missing on some compounds. Compounds without an
approved geometry are kept in a separate, marked area.

**Does "docking-ready" mean it is ready for my target?**
No. It means the files passed the pipeline checks. Protonation and tautomer states are not validated for
every target.

**Are the ADMET values measured?**
No. They are predictions with an applicability domain. Use them for triage.

**How do I cite it?**
See `CITATION.cff` and cite the upstream sources you used, listed in [SOURCES.md](SOURCES.md).

**Where do I report a problem or a security issue?**
Problems: open an issue. Security: [SECURITY.md](../SECURITY.md). Anything else: contact@alchemia.solutions.
