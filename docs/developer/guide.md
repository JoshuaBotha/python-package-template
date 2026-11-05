# Developer guide

For people changing my-package itself. Process rules (branches, PR titles,
the definition of done, releasing) are in
[CONTRIBUTING.md](../../CONTRIBUTING.md); this guide covers the code. Read
the [architecture overview](../architecture/overview.md) first, and the
gotchas in [CLAUDE.md](../../CLAUDE.md).

## Set up

```bash
git clone https://github.com/JoshuaBotha/my-package.git
cd my-package
mise run setup:dev   # Python 3.13 + uv, uv sync, pre-commit hooks
mise run ci          # lint, typecheck, tests, wheel check (CI=true)
```

| Task | What |
|---|---|
| `setup:dev` | Fresh clone to ready (idempotent). |
| `lint` / `lint:fix` | `ruff check` + `ruff format --check`; `:fix` applies both. |
| `typecheck` | `ty check`. |
| `test` | All suites. |
| `test:unit` | One suite; extra args go to pytest (`mise run test:unit -k version`). |
| `build:dist` | Wheel and sdist into `dist/`. |
| `build:check-wheel` | Install the wheel into a clean venv and import it. |
| `ci` | `CI=true`, lint, typecheck, test, wheel check. Done = this passes. |
| `release:prepare` | Release branch, version bump, relock, doc refs, push. |
| `release:publish` | CI only: tag and release the `pyproject.toml` version. |
| `repo:settings` | Apply GitHub repo settings and the `main` ruleset (idempotent). |

Tasks are bash scripts in `.mise/tasks/` (`test/unit` is `test:unit`).
Workflows only call `mise run`; put new logic in a task, not in YAML.

## Code map

```
src/my_package/       the package (py.typed: ships type information)
tests/unit/           one module, in process
docs/                 user, architecture, ADRs, this guide
.mise/tasks/          every task CI and people run
.claude/skills/       /release-patch, /release-minor, /release-major
```

## Docs

| What changed | Update |
|---|---|
| User-visible behaviour | The page in `docs/user/` that covers it, and `README.md` if it changes the quick start. |
| A design decision with real alternatives | A new ADR in `docs/adr/`, next number. |
| Structure, flow or a seam | [Architecture overview](../architecture/overview.md) and this guide. |
| A term | `GLOSSARY.md`. |
| Something learned the hard way | Gotchas in `CLAUDE.md`. |
