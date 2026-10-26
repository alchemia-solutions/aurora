# Contributing

Thank you for the interest. This repository describes ATHANOR and AURORA and holds read-only examples of
the API. The pipeline code and the data are not here, so there is nothing of them to patch.

## Where to go for what

| You want to | Go to |
|---|---|
| Register a study that uses AURORA | [Collaborate, register studies](https://aurora.alchemia.solutions/collaborate/register-studies) |
| Ask that a molecule database be considered by ATHANOR | [Collaborate, add databases](https://aurora.alchemia.solutions/collaborate/add-databases) |
| Read how the API works | [Documents, API](https://aurora.alchemia.solutions/docs/api) and [docs/API.md](docs/API.md) |
| Fix or improve this repository | An issue or a pull request here |
| Report a vulnerability | contact@alchemia.solutions, see [SECURITY.md](SECURITY.md) |

Collaborate forms need an approved account and open to read when the v1.3 release is live.

## What helps

- A correction to the source list: a wrong reference, a dead link, a licence statement the source changed.
  Quote the source page and the date you read it.
- A fix or an addition to the examples, as long as they only read the API.
- A clearer sentence in the documentation, or a correction of a claim that overreaches.
- A question or a use case, as an issue.

## What we cannot take

- Pipeline code, configuration or parameters. They are not in this repository.
- Compound data of any kind.
- Credentials, tokens or personal data. Do not paste them in an issue or a pull request, and remove them
  from any log you attach.

## How

1. Open an issue first for anything larger than a typo.
2. Keep a pull request to one subject.
3. Run `python scripts/gen_numbers.py --check`. Figures live in `data/numbers.json` and nowhere else.
4. Write no em dash or en dash in text. Rewrite the sentence.

## Licence of a contribution

By contributing you agree that documentation is released under CC BY-SA 4.0 and code under Apache-2.0, as
in [LICENSE](LICENSE) and [LICENSE-CODE](LICENSE-CODE).

## Privacy

This repository collects nothing. GitHub processes what you submit there under its own terms. For a private
matter write to contact@alchemia.solutions.
