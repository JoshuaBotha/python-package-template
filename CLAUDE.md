# my-package

One-line description of my-package.

- Docs: `README.md` (quick start) and `docs/` (index `docs/README.md`): user guides in `docs/user/`, `docs/architecture/overview.md`, `docs/developer/guide.md`, decisions in `docs/adr/`, terms in `GLOSSARY.md`.
- Before any change: follow `CONTRIBUTING.md` (branch names, PR titles, tests, done = `mise run ci` green), including its "For coding agents" section.

## Environment

- `mise.toml`: Python 3.13, uv. `.venv` from `uv sync` (installs the package editable plus the dev group).
- `uv sync` installs the package itself (editable), so tests import the source tree.

## mise

mise is the single entry point for tooling, tasks and env vars, so a task runs the same locally and in CI.

- **Tasks are bash scripts** in `.mise/tasks/`, not inline TOML. Start each with `#!/usr/bin/env bash`, a `#MISE description="..."` line and `set -euo pipefail`; `chmod +x`.
- **Organise with folders**: `.mise/tasks/test/unit` is `mise run test:unit`; `test/_default` is plain `mise run test`.
- **Workflows call tasks** (`mise run ci`), they don't inline logic. CI installs tools with `jdx/mise-action`. If a workflow step is more than a one-liner, make it a task.
- **Env vars** go in `mise.toml` `[env]` (or `#MISE env=` on one task) when they apply to the project.
- Fresh clone: `mise run setup:dev` (also installs the pre-commit hooks). Everything CI runs, with `CI=true`: `mise run ci`.
- Tasks: `setup:dev`, `lint`, `lint:fix`, `typecheck`, `test`, `test:unit`, `build:dist`, `build:check-wheel`, `release:prepare <patch|minor|major>` (release branch + bump + relock + version refs in `README.md`/`docs/user/` + push; skills `/release-patch|minor|major` first check the docs cover every feat/fix since the last tag, then add the PR), `release:publish` (CI-only: tags + releases the pyproject version on merge to `main` or manual dispatch; `0.0.0` = unreleased, skipped), `repo:settings` (GitHub features, merge rules, `main` ruleset; idempotent), `ci`.

## Gotchas (don't relearn these)

- Pre-commit hooks run `uv run --frozen ruff`, the version in `uv.lock`; bump ruff with `uv lock --upgrade-package ruff`, not in `.pre-commit-config.yaml`.
- Local paths handed to tools or compared in tests: use `Path.as_posix()` so Windows CI matches.
