#!/usr/bin/env bash
# Launch the Google Ads MCP server over Streamable HTTP.
set -euo pipefail
cd "$(dirname "$0")/.."
HOST="${MCP_HOST:-0.0.0.0}"
PORT="${MCP_PORT:-8000}"
exec uv run google-ads-mcp --transport streamable-http --host "$HOST" --port "$PORT"
