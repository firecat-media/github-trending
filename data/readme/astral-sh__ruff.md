# Ruff

[ ](https://github.com/astral-sh/ruff)
[ ](https://pypi.python.org/pypi/ruff)
[ ](https://github.com/astral-sh/ruff/blob/main/LICENSE)
[ ](https://pypi.python.org/pypi/ruff)
[ ](https://github.com/astral-sh/ruff/actions)
[ ](https://discord.com/invite/astral-sh)

[**Docs**](https://docs.astral.sh/ruff/) | [**Playground**](https://play.ruff.rs/)

An extremely fast Python linter and code formatter, written in Rust.

   Linting the CPython codebase from scratch. 

- ⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
- 🐍 Installable via `pip`
- 🛠️ `pyproject.toml` support
- 🤝 Python 3.15 compatibility
- ⚖️ Drop-in parity with [Flake8](https://docs.astral.sh/ruff/faq/#how-does-ruffs-linter-compare-to-flake8), [isort](https://docs.astral.sh/ruff/faq/#how-does-ruffs-import-sorting-compare-to-isort), and [Black](https://docs.astral.sh/ruff/faq/#how-does-ruffs-formatter-compare-to-black)
- 📦 Built-in caching, to avoid re-analyzing unchanged files
- 🔧 Fix support, for automatic error correction (e.g., automatically remove unused imports)
- 📏 Over [900 built-in rules](https://docs.astral.sh/ruff/rules/), with native re-implementations
    of popular Flake8 plugins, like flake8-bugbear
- ⌨️ First-party [editor integrations](https://docs.astral.sh/ruff/editors) for [VS Code](https://github.com/astral-sh/ruff-vscode) and [more](https://docs.astral.sh/ruff/editors/setup)
- 🌎 Monorepo-friendly, with [hierarchical and cascading configuration](https://docs.astral.sh/ruff/configuration/#config-file-discovery)

Ruff aims to be orders of magnitude faster than alternative tools while integrating more
functionality behind a single, common interface.

Ruff can be used to replace [Flake8](https://pypi.org/project/flake8/) (plus dozens of plugins),
[Black](https://github.com/psf/black), [isort](https://pypi.org/project/isort/),
[pydocstyle](https://pypi.org/project/pydocstyle/), [pyupgrade](https://pypi.org/project/pyupgrade/),
[autoflake](https://pypi.org/project/autoflake/), and more, all while executing tens or hundreds of
times faster than any individual tool.

Ruff is actively developed and used in major open-source projects like:

- [Apache Airflow](https://github.com/apache/airflow)
- [Apache Superset](https://github.com/apache/superset)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Hugging Face](https://github.com/huggingface/transformers)
- [Pandas](https://github.com/pandas-dev/pandas)
- [SciPy](https://github.com/scipy/scipy)

Ruff is backed by [Astral](https://astral.sh), the creators of
[uv](https://github.com/astral-sh/uv) and [ty](https://github.com/astral-sh/ty).

Read the [launch
post](https://astral.sh/blog/announcing-astral-the-company-behind-ruff), or the
original [project
announcement](https://notes.crmarsh.com/python-tooling-could-be-much-much-faster).

## Testimonials

[**Sebastián Ramírez**](https://twitter.com/tiangolo/status/1591912354882764802), creator
of [FastAPI](https://github.com/tiangolo/fastapi
