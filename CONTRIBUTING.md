# Contributing

## Setup

```bash
git clone https://github.com/eneelkant/google-ads-claude-plugin.git
cd google-ads-claude-plugin
uv sync --all-groups
```

## Tests

```bash
uv run pytest -q
```

Do not add tests that require real Google Ads credentials.

## Structure

- Put Google Ads / MCP logic in `src/google_ads_mcp/`
- Put client launch examples in `clients/` and `docs/clients/`
- Keep `google-ads-manager/` limited to Claude plugin metadata

## Pull requests

1. Branch from `main`
2. Keep tool names stable
3. Preserve destructive-operation safety (`confirm_removal`)
4. Never commit secrets
