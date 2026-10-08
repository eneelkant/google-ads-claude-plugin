# Cursor

## Prerequisites

- [Cursor](https://cursor.com/)
- Python 3.12+ and [uv](https://astral.sh/uv)
- Repository cloned and `uv sync` completed
- Google Ads credentials in your environment or a local `.env`

## Configuration

Copy the example into your Cursor MCP config:

- Project: `.cursor/mcp.json`
- Global: `~/.cursor/mcp.json`

Example (stdio):

```json
{
  "mcpServers": {
    "google-ads": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "${workspaceFolder}",
        "google-ads-mcp"
      ],
      "envFile": "${workspaceFolder}/.env"
    }
  }
}
```

See `clients/cursor/mcp.json` for an env-var based variant.

## HTTP transport (optional)

If the server is already running with streamable HTTP:

```json
{
  "mcpServers": {
    "google-ads": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

Start it with:

```bash
uv run google-ads-mcp --transport streamable-http --host 127.0.0.1 --port 8000
```

## Verify

1. Open **Cursor Settings → MCP**
2. Confirm `google-ads` is connected
3. Ask: `List my accessible Google Ads accounts`

## Troubleshooting

- **Server failed to start**: ensure `uv` is on `PATH` and `--directory` points at the repo root.
- **Missing credentials**: set `GOOGLE_ADS_*` env vars or use `envFile` pointing at `.env`.
- **Tools missing**: reload MCP servers after saving `mcp.json`.
