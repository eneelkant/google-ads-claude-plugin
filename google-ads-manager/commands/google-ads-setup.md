# Google Ads Setup

Use this command to configure Google Ads API credentials for the universal Google Ads MCP server.

The setup should guide the user through:

1. Cloning the public repository and running `uv sync` at the repo root
2. Google Ads Developer Token
3. Google Cloud service account credentials
4. Google Ads Customer ID
5. Login Customer ID, if using an MCC account
6. Securely storing credentials in a local `.env` (never commit it)
7. Connecting Claude (or another MCP client) via the examples in `clients/` and `docs/clients/`

Never request users to paste credentials into a public GitHub repository.

After configuration, verify that the Google Ads API connection works before attempting campaign management operations.
