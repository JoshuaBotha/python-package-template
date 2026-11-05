# my-package

One-line description of my-package.

<!-- template:start -->
## Using this template

1. On GitHub, **Use this template** → create your repo, then clone it.
2. `mise run setup:init <your-name> --description "What it does"`: renames
   `my-package` / `my_package` everywhere (package dir, imports, docs, URLs from
   your `origin` remote), relocks, removes this section and itself.
3. `mise run setup:dev`, then `mise run ci`. Commit.
4. Set `keywords` in `pyproject.toml` (they become GitHub topics), push, then
   `mise run repo:settings` (squash-only merges, `main` ruleset, security
   features). Rulesets and some security features need a public repo or a paid
   plan for private ones; the task warns and carries on.
5. Version starts at `0.0.0` (never released). `/release-minor` (or
   `mise run release:prepare minor`) makes `0.1.0`.

What you get: mise tasks for everything, uv, ruff (lint + format, also as
pre-commit hooks), ty, pytest, CI on Linux/macOS/Windows, Dependabot,
Conventional Commit PRs, GitHub Releases on merge, and Claude Code release
skills. See [CONTRIBUTING.md](CONTRIBUTING.md).
<!-- template:end -->

## Install

```bash
uv add "my-package @ git+https://github.com/JoshuaBotha/my-package.git@v0.0.0"
```

## Quick start

```python
import my_package

print(my_package.__version__)
```

## Docs

[docs/](docs/README.md): user guides, architecture, decisions, developer guide.

## License

MIT
