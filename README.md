# CI/CD ASM

A minimal FastAPI service with a full CI pipeline.

## CI Pipeline

| Job | Runs on | Triggered by |
|-----|---------|--------------|
| Lint | ubuntu-latest | push / PR |
| Test | ubuntu + macos × py3.10/3.11/3.12 | after lint passes |

## Caching

Dependencies are cached by `uv` keyed on the hash of `pyproject.toml`. The install step prints a summary to the GitHub Actions job summary showing time and cache status.

### Benchmark — `uv sync --group dev`

| Run type | Install time |
|----------|-------------|
| Without cache | ? seconds |
| With cache | ? seconds |

> Fill in after observing the first two runs in the Actions tab. The "Install dependencies" step summary shows the elapsed time and `cache-hit: true/false` for each matrix job.

## Artifacts

Each matrix job uploads:
- `coverage-<os>-py<version>` — `coverage.xml` (Cobertura format)
- `junit-<os>-py<version>` — `junit.xml` (JUnit XML test results)

Coverage is also reported to [Codecov](https://codecov.io) with per-matrix flags.

## Running locally

```bash
uv sync --group dev
uv run pytest --cov --cov-report=term-missing
uv run ruff check src tests
uv run black --check src tests
```
