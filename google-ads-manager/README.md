# Claude plugin: google-ads-manager

Claude-specific plugin metadata for the **universal Google Ads MCP server**.

This directory contains:

- Plugin manifest (`.claude-plugin/plugin.json`)
- Setup command (`commands/google-ads-setup.md`)
- Skill guidance (`skills/google-ads-manager/SKILL.md`)
- MCP launch hint (`.mcp.json`) pointing at the **root** package

The Google Ads implementation lives in the repository root (`src/google_ads_mcp/`). Do not duplicate Python sources here.

## Install the MCP server

From the repository root:

```bash
uv sync
uv run google-ads-mcp
```

## Docs

- Universal README: [../README.md](../README.md)
- Claude client guide: [../docs/clients/claude.md](../docs/clients/claude.md)
