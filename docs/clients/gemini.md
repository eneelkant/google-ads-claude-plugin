# Gemini (Gemini CLI)

## Prerequisites

- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- Python 3.12+ and [uv](https://astral.sh/uv)
- Repository cloned and `uv sync` completed

## Configuration

Gemini CLI reads `mcpServers` from `~/.gemini/settings.json` or project `.gemini/settings.json`.

Stdio example (see `clients/gemini/settings.json`):

```json
{
  "mcpServers": {
    "google-ads": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/ABSOLUTE/PATH/TO/google-ads-claude-plugin",
        "google-ads-mcp"
      ],
      "env": {
        "GOOGLE_ADS_DEVELOPER_TOKEN": "$GOOGLE_ADS_DEVELOPER_TOKEN",
        "GOOGLE_ADS_SERVICE_ACCOUNT_PATH": "$GOOGLE_ADS_SERVICE_ACCOUNT_PATH",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "$GOOGLE_ADS_LOGIN_CUSTOMER_ID"
      }
    }
  }
}
```

Or add via CLI:

```bash
gemini mcp add google-ads uv -- run --directory /ABSOLUTE/PATH/TO/google-ads-claude-plugin google-ads-mcp
```

## HTTP transport (optional)

For a running streamable HTTP server:

```json
{
  "mcpServers": {
    "google-ads": {
      "httpUrl": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

## Verify

```bash
gemini mcp list
```

Then ask Gemini to list accessible Google Ads accounts.

## Troubleshooting

- Use absolute paths for `--directory`.
- Gemini expands `$VAR` / `${VAR}` in `env` values from your shell environment.
- This project does not invent Gemini-only APIs; it uses Gemini CLI's documented MCP config.
