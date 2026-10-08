# Security

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please open a [GitHub Issue](https://github.com/eneelkant/google-ads-claude-plugin/issues) with the label `security`, or contact the maintainer privately if the issue involves active credential exposure.

## Scope

This MCP server provides read/write access to Google Ads accounts through the official Google Ads API.

Key points:

- The server **cannot** modify account access, user permissions, credentials, or billing
- Write tools can create/modify campaigns, ad groups, ads, keywords, and budgets
- Removal tools require `confirm_removal=True` as a server-side safety guard
- `execute_gaql` can read sensitive resources like `customer_user_access` (read-only)

## Credentials

- Load credentials from environment variables or a local `.env` file
- Never commit `.env`, service account JSON, developer tokens, or API keys
- Docker images must receive credentials at runtime (env + bind mounts)
- Do not log credential values; logs may include file paths only

## Client exposure

- Prefer local **stdio** for desktop clients (Cursor, Claude, Gemini CLI)
- For remote clients (ChatGPT), terminate TLS at a reverse proxy and restrict network access
- Require human approval for write/destructive tools in remote MCP connectors when available

## Ignored secret patterns

The repository `.gitignore` excludes:

- `.env` / `.env.local`
- `service-account*.json`
- `google-ads.yaml`
- `*.pem` / `*.key`
