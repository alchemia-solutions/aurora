# data

`numbers.json` holds every figure printed in the root README: counts of release 2.0.0, the date each was
read and the id of the reading it was copied from. The release is in preparation and not published.

`site-links.json` is the one list of links to the AURORA platform. Every document points to an address in
it, and `scripts/check_links.py` fails when a document links to a platform address that is not listed. A link
there is a reference and not a statement that the page is open; the platform is a closed beta. Check the
addresses in one pass when the state of the platform changes.

## How to use

Edit a value in `numbers.json` (each figure is an object with `value`, `asof` and `id`), then run `python scripts/gen_numbers.py` from the repository root. It
rewrites the generated blocks of the README. `python scripts/gen_numbers.py --check` fails when a block
differs from this file.

## What is not here

No compound data, no download package and no database dump. This file measures nothing by itself: its values
are copies of dated readings of the Alchemia registry.
