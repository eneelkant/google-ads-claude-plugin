# Google Ads MCP Server

Universal **Model Context Protocol (MCP)** server for Google Ads — one implementation, many AI clients.

Works with:

- **Cursor**
- **Claude** (Desktop, Code, Cowork plugin)
- **Gemini CLI**
- **ChatGPT / OpenAI** (remote MCP or Secure MCP Tunnel)
- Any other **MCP-compatible** client

~47 tools cover accounts, campaigns, ad groups, ads, keywords, Performance Max, budgets, reporting, and utilities.

## Architecture

```text
Google Ads API
      │
      ▼
Google Ads MCP Server   ←── single source of truth
      │
      ├── Cursor
      ├── Claude
      ├── Gemini
      ├── ChatGPT
      └── Other MCP clients
```

Client-specific folders under `clients/` only explain how to launch or connect. They do **not** reimplement the Google Ads API.

See [docs/architecture.md](docs/architecture.md).

## Requirements

- Python **3.12+**
- [uv](https://docs.astral.sh/uv/) **or** Docker
- Google Ads API developer token
- GCP service account JSON key with Google Ads API access

## Installation

The repository is **public** — clone without GitHub authentication.

### Option 1 — uv

```bash
git clone https://github.com/eneelkant/google-ads-claude-plugin.git
cd google-ads-claude-plugin
uv sync
```

Run (stdio, default):

```bash
uv run google-ads-mcp
```

### Option 2 — Docker

```bash
git clone https://github.com/eneelkant/google-ads-claude-plugin.git
cd google-ads-claude-plugin

export GOOGLE_ADS_DEVELOPER_TOKEN=your-developer-token
export GOOGLE_ADS_LOGIN_CUSTOMER_ID=your-mcc-customer-id
export GOOGLE_ADS_SERVICE_ACCOUNT_HOST_PATH=/absolute/path/to/service-account.json

docker compose up --build
```

Or build/run manually:

```bash
docker build -t google-ads-mcp .
docker run --rm -p 8000:8000 \
  -e GOOGLE_ADS_DEVELOPER_TOKEN \
  -e GOOGLE_ADS_LOGIN_CUSTOMER_ID \
  -e GOOGLE_ADS_SERVICE_ACCOUNT_PATH=/credentials/service-account.json \
  -v /absolute/path/to/service-account.json:/credentials/service-account.json:ro \
  google-ads-mcp
```

Docker defaults to **streamable-http** on port `8000`. Credentials are mounted at runtime — never copied into the image.

## Google Ads credentials

Copy the example env file:

```bash
cp .env.example .env
```

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | yes | API developer token |
| `GOOGLE_ADS_SERVICE_ACCOUNT_PATH` | yes | Path to service account JSON |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | MCC | Login customer / MCC ID |
| `GOOGLE_ADS_CUSTOMER_ID` | no | Default customer ID |
| `GOOGLE_ADS_IMPERSONATED_EMAIL` | no | Workspace user for domain-wide delegation |

Never commit `.env`, service account JSON, tokens, or keys.

## MCP transports

| Transport | Command | Use when |
|-----------|---------|----------|
| **stdio** (default) | `uv run google-ads-mcp` | Cursor, Claude, Gemini CLI launch the process |
| **streamable-http** | `uv run google-ads-mcp --transport streamable-http` | Remote clients (ChatGPT) or URL-based MCP |
| **sse** | `uv run google-ads-mcp --transport sse` | Legacy SSE clients |

HTTP bind options:

```bash
uv run google-ads-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

Env overrides: `MCP_TRANSPORT`, `MCP_HOST`, `MCP_PORT` (or `PORT`).

## Client setup

| Client | Mode | Guide |
|--------|------|-------|
| Cursor | Local stdio (optional HTTP) | [docs/clients/cursor.md](docs/clients/cursor.md) |
| Claude | Local stdio + plugin | [docs/clients/claude.md](docs/clients/claude.md) |
| Gemini CLI | Local stdio (optional HTTP) | [docs/clients/gemini.md](docs/clients/gemini.md) |
| ChatGPT | **Remote** MCP / Secure Tunnel | [docs/clients/chatgpt.md](docs/clients/chatgpt.md) |

Example configs live under `clients/`.

### LOCAL MCP vs REMOTE MCP

- **LOCAL (stdio)**: the client starts `google-ads-mcp` as a child process.
- **REMOTE (HTTP)**: you run the server (or Docker) and the client connects to `https://host/mcp`. ChatGPT requires remote MCP or a Secure MCP Tunnel — it does not spawn local stdio servers.

## Capabilities

- Accounts & MCC hierarchy
- Search / Display / Video / Demand Gen / Performance Max campaigns
- Ad groups, RSAs, RDAs, video & Demand Gen ads
- Keywords, bids, search terms
- Budgets & utilization
- GAQL reporting and performance summaries

Full list: [docs/tools.md](docs/tools.md).

## Security

- Credentials via environment / mounted secrets only
- Destructive removals require `confirm_removal=True`
- Server cannot change billing, user access, or Google account permissions
- See [SECURITY.md](SECURITY.md)

## Development

```bash
uv sync --all-groups
uv run pytest -q
uv run google-ads-mcp --help
```

Package name: `google-ads-mcp`  
Import package: `google_ads_mcp`  
Entry point: `google-ads-mcp`

## Testing

```bash
uv run pytest
```

Tests mock the Google Ads API — no real credentials required.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Google Ads client is not available` | Check `GOOGLE_ADS_*` env vars and service account path |
| Client cannot start server | Use absolute paths; ensure `uv` is on `PATH` |
| ChatGPT cannot connect to stdio | Deploy streamable-http (or Secure MCP Tunnel) instead |
| Docker credential errors | Set `GOOGLE_ADS_SERVICE_ACCOUNT_HOST_PATH` to a real JSON file |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache-2.0 — see [LICENSE](LICENSE).
