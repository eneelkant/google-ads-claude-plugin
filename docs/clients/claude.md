# Claude

## Prerequisites

- Claude Desktop and/or Claude Code
- Python 3.12+ and [uv](https://astral.sh/uv)
- Repository cloned and `uv sync` completed

## Claude Desktop (local stdio)

Merge `clients/claude/claude_desktop_config.json` into:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Replace `/ABSOLUTE/PATH/TO/...` placeholders before saving.

## Claude Code / Cowork

Use project `.mcp.json` (see `clients/claude/mcp.json`) or install the bundled plugin from `.claude-plugin/marketplace.json`.

Plugin metadata lives under `google-ads-manager/` (skills + setup command). The MCP server itself is the root package:

```bash
uv run google-ads-mcp
```

## Verify

1. Restart Claude Desktop / reload Claude Code MCP
2. Confirm the `google-ads` server appears
3. Ask: `Show my Google Ads account hierarchy`

## Troubleshooting

- Prefer absolute paths in Desktop configs.
- Keep secrets in env vars — never paste tokens into chat.
- Destructive tools still require `confirm_removal=True`.
