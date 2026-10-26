# data

`numbers.json` holds every figure printed in the root README: counts of the registry, the date they were
read and where they came from.

`site-links.json` is the one list of links to the AURORA platform. Every document points to an address in
it, and `scripts/check_links.py` fails when a document links to a platform address that is not listed. When
the v1.3 release goes live, check these addresses in one pass.

## How to use

Edit a value in `numbers.json`, then run `python scripts/gen_numbers.py` from the repository root. It
rewrites the generated blocks of the README. `python scripts/gen_numbers.py --check` fails when a block
differs from this file.

## What is not here

No compound data, no download package and no database dump. This file measures nothing by itself: its values
are copies of dated readings of the Alchemia registry.
