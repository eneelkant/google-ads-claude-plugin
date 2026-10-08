#!/usr/bin/env bash
# Launch the Google Ads MCP server over stdio (default).
set -euo pipefail
cd "$(dirname "$0")/.."
exec uv run google-ads-mcp --transport stdio
