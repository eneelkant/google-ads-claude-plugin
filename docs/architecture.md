# Architecture

```text
Google Ads API
      |
      v
Google Ads MCP Server  (src/google_ads_mcp/)
      |
      +---- Cursor          (local stdio / optional HTTP)
      |
      +---- Claude          (local stdio + plugin metadata)
      |
      +---- Gemini CLI      (local stdio / optional HTTP)
      |
      +---- ChatGPT/OpenAI  (remote Streamable HTTP or Secure MCP Tunnel)
      |
      +---- Other MCP clients
```

## Single implementation

All Google Ads tools live in one Python package: `google_ads_mcp`.

Client folders under `clients/` and docs under `docs/clients/` only describe how each product launches or connects to that server. They do not reimplement the Ads API.

## Transports

| Transport | Command | Typical clients |
|-----------|---------|-----------------|
| stdio | `google-ads-mcp` | Cursor, Claude Desktop/Code, Gemini CLI |
| streamable-http | `google-ads-mcp --transport streamable-http` | ChatGPT remote MCP, Cursor/Gemini via URL |
| sse | `google-ads-mcp --transport sse` | Legacy SSE clients |

## Claude plugin layout

`google-ads-manager/` keeps Claude plugin metadata (skills, setup command, plugin manifest). The executable MCP server is the root package installed via `uv sync`.
