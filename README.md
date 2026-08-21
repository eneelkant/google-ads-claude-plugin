## Why Use Claude for Google Ads?

Google Ads management often requires moving between campaigns, ad groups, ads, keywords, budgets, reports, and performance screens.

With this plugin, Claude can act as an **AI Google Ads assistant** that understands your requests in context.

### Ask instead of navigate

Instead of manually building reports:

```text
Show me campaign performance for the last 30 days,
sorted by cost, and identify campaigns with high spend
and weak conversion performance.
```

Instead of manually checking keywords:

```text
Find keywords that are spending money but producing
poor results.
```

Instead of navigating campaign settings:

```text
Show me all paused Search campaigns and explain
which ones had the highest spend before being paused.
```

---

# Key Capabilities

## 📊 Google Ads Performance & Reporting

Use Claude to retrieve and analyze advertising performance.

* Campaign performance
* Ad group performance
* Keyword performance
* Search terms reports
* Account-level summaries
* Spend and budget analysis
* GAQL queries
* Custom Google Ads reporting

Example:

```text
How did my Google Ads account perform over the last 7 days?
```

---

## 🎯 Campaign Management

Manage campaign structures through natural language.

Supported workflows include:

* Search campaigns
* Display campaigns
* Video campaigns
* Demand Gen campaigns
* Performance Max campaigns
* Campaign listing
* Campaign details
* Campaign creation
* Campaign updates
* Campaign status management
* Campaign removal

Example:

```text
Show me all active campaigns and their daily budgets.
```

---

## 🔎 Search Ads & Keywords

Manage Search advertising workflows from Claude.

* List keywords
* Add keywords
* Specify keyword match types
* Remove keywords
* Update keyword bids
* Analyze keyword performance
* Review search terms

Example:

```text
Find my highest-spending keywords and show their performance.
```

---

## ✍️ AI-Assisted Ad Management

Manage supported Google Ads creative formats through MCP tools.

Supported ad workflows include:

* Responsive Search Ads
* Responsive Display Ads
* Video ads
* Demand Gen ads
* Ad listing
* Ad details
* Ad status management

Example:

```text
Create a responsive search ad for my existing Search ad group
using these headlines and descriptions.
```

---

## 🚀 Performance Max

Manage important Performance Max resources through Claude.

Capabilities include:

* Performance Max campaign creation
* Asset groups
* Asset group details
* Asset management
* Audience signals
* Search theme signals
* Asset performance
* Performance Max placement/channel reporting

Example:

```text
Show me my Performance Max asset groups and their performance.
```

---

## 💰 Google Ads Budgets

Monitor and manage campaign budgets.

* List budgets
* Create shared budgets
* Update budgets
* Check budget utilization
* Compare budget allocation with actual spend

Example:

```text
Which campaigns are using most of their allocated budget?
```

---

## 🏢 Google Ads Accounts & MCC

Work with accounts accessible through your Google Ads API credentials.

* List accessible accounts
* Account information
* MCC account hierarchy
* Customer IDs
* Login customer IDs

Example:

```text
Show me the Google Ads accounts available through my MCC.
```

---

# Natural Language Google Ads Automation

The goal is to make Google Ads operations conversational.

You can ask Claude things like:

### Campaigns

```text
List my active campaigns.
```

```text
Which campaigns spent the most yesterday?
```

```text
Show me my paused campaigns.
```

```text
Create a Search campaign.
```

```text
Pause this campaign.
```

### Ads

```text
Show me the ads in this ad group.
```

```text
Create a responsive search ad.
```

```text
Show me my active ads.
```

### Keywords

```text
Find my highest-spending keywords.
```

```text
Add these keywords to the ad group.
```

```text
Update the CPC bid for these keywords.
```

### Performance

```text
How did my account perform this week?
```

```text
Show me campaigns with high spend and poor performance.
```

```text
Give me a search terms report.
```

### Optimization

```text
Which campaigns should I investigate first based on performance?
```

```text
Find underperforming keywords.
```

```text
Which campaigns are approaching their budgets?
```

---

# MCP Toolset

The plugin currently exposes approximately **47 Google Ads tools** across nine functional areas.

## Accounts

| Tool                       | Purpose                                          |
| -------------------------- | ------------------------------------------------ |
| `list_accessible_accounts` | List accounts accessible through the credentials |
| `get_account_info`         | Retrieve account details                         |
| `get_account_hierarchy`    | Retrieve MCC hierarchy                           |

## Campaigns

| Tool                  | Purpose                             |
| --------------------- | ----------------------------------- |
| `list_campaigns`      | List campaigns                      |
| `get_campaign`        | Retrieve campaign details           |
| `create_campaign`     | Create Search or Display campaigns  |
| `update_campaign`     | Update campaign settings            |
| `set_campaign_status` | Change campaign status              |
| `remove_campaign`     | Remove a campaign with confirmation |

## Ad Groups

| Tool                  | Purpose                   |
| --------------------- | ------------------------- |
| `list_ad_groups`      | List ad groups            |
| `get_ad_group`        | Retrieve ad group details |
| `create_ad_group`     | Create an ad group        |
| `update_ad_group`     | Update an ad group        |
| `set_ad_group_status` | Change ad group status    |

## Ads

| Tool                           | Purpose                        |
| ------------------------------ | ------------------------------ |
| `list_ads`                     | List ads                       |
| `create_responsive_search_ad`  | Create a responsive search ad  |
| `create_responsive_display_ad` | Create a responsive display ad |
| `create_video_ad`              | Create a video ad              |
| `create_demand_gen_ad`         | Create a Demand Gen ad         |
| `set_ad_status`                | Change ad status               |
| `get_ad_details`               | Retrieve ad details            |

## Keywords

| Tool                      | Purpose                      |
| ------------------------- | ---------------------------- |
| `list_keywords`           | List keywords                |
| `add_keywords`            | Add keywords in batches      |
| `remove_keyword`          | Remove a keyword             |
| `update_keyword_bid`      | Update keyword CPC bids      |
| `get_keyword_performance` | Retrieve keyword performance |

## Performance Max

| Tool                              | Purpose                                                |
| --------------------------------- | ------------------------------------------------------ |
| `create_performance_max_campaign` | Create a Performance Max campaign                      |
| `list_asset_groups`               | List Performance Max asset groups                      |
| `get_asset_group_details`         | Retrieve asset group details                           |
| `add_assets_to_group`             | Add assets to an asset group                           |
| `remove_asset_from_group`         | Remove an asset                                        |
| `add_audience_signal`             | Add audience/search theme signals                      |
| `get_asset_performance`           | Retrieve asset performance                             |
| `get_pmax_placement_performance`  | Retrieve Performance Max placement/channel performance |

## Budgets

| Tool                     | Purpose                  |
| ------------------------ | ------------------------ |
| `list_budgets`           | List campaign budgets    |
| `create_budget`          | Create a shared budget   |
| `update_budget`          | Update a budget          |
| `get_budget_utilization` | Check budget utilization |

## Reporting

| Tool                              | Purpose                                   |
| --------------------------------- | ----------------------------------------- |
| `execute_gaql`                    | Execute a Google Ads Query Language query |
| `get_campaign_performance`        | Campaign performance                      |
| `get_ad_group_performance`        | Ad group performance                      |
| `get_search_terms_report`         | Search terms reporting                    |
| `get_keyword_performance_report`  | Keyword reporting                         |
| `get_account_performance_summary` | Account performance summary               |

## Utilities

| Tool                  | Purpose                               |
| --------------------- | ------------------------------------- |
| `list_gaql_resources` | Discover GAQL resources               |
| `get_field_metadata`  | Inspect GAQL field metadata           |
| `convert_micros`      | Convert Google Ads micros to currency |

---

# Built for AI-Assisted PPC Management

The plugin is designed around how people actually communicate with an AI agent.

Rather than requiring every Google Ads API parameter to be known beforehand, Claude can translate a natural-language request into the appropriate MCP tool call.

For example:

```text
"Show me campaigns that spent more than $500
in the last 14 days."
```

Claude can determine the appropriate reporting workflow and return the relevant Google Ads data.

For more advanced workflows, Claude can use GAQL directly:

```text
Run a Google Ads query showing campaign,
cost, clicks, impressions, and conversions
for the last 30 days.
```

---

# Safety & Confirmation

Google Ads changes can have real financial consequences.

The plugin therefore distinguishes between read operations and potentially destructive or costly actions.

### Read operations

Reporting and inspection workflows can retrieve information such as:

* Campaign data
* Ad group data
* Ads
* Keywords
* Performance
* Search terms
* Budgets
* Account information

### Write operations

Operations that change advertising resources should be treated carefully.

Before significant changes, Claude should communicate:

* The campaign or resource
* Its current state
* The requested change
* The expected impact

For potentially costly actions such as increasing budgets or launching campaigns, explicit confirmation should be obtained before execution.

Removal operations use an additional server-side confirmation parameter:

```text
confirm_removal=True
```

---

# Security

Google Ads API credentials remain under your control.

The plugin does **not** provide tools for:

* Changing Google account access
* Managing Google Ads users
* Changing login credentials
* Managing payment methods
* Managing billing accounts
* Granting account permissions

However, Google Ads API credentials can provide significant access to advertising data and campaign resources.

Protect your credentials carefully.

### Never commit credentials

Do not commit:

```text
.env
```

or Google Cloud service-account JSON credentials to Git.

Use environment variables or a secure local credential-management workflow.

---

# Requirements

You need:

* Python 3.12+
* `uv`
* A Google Ads API developer token
* A Google Cloud service account
* Google Ads customer access
* An MCC/login customer ID when required by your account structure
* Claude with MCP/plugin support

---

# Installation

Clone the repository:

```bash
git clone https://github.com/eneelkant/google-ads-claude-plugin.git
cd google-ads-claude-plugin
```

Install dependencies:

```bash
uv sync
```

The Claude plugin is located in:

```text
google-ads-manager/
```

---

# Google Ads API Configuration

Create your local environment file:

```bash
cp google-ads-manager/.env.example google-ads-manager/.env
```

Configure the required Google Ads credentials.

Typical variables include:

```text
GOOGLE_ADS_DEVELOPER_TOKEN=
GOOGLE_ADS_SERVICE_ACCOUNT_PATH=
GOOGLE_ADS_LOGIN_CUSTOMER_ID=
GOOGLE_ADS_CUSTOMER_ID=
GOOGLE_ADS_IMPERSONATED_EMAIL=
```

Keep `.env` local and never commit it to GitHub.

---

# Running the MCP Server

From the plugin directory:

```bash
cd google-ads-manager
uv sync
uv run google-ads-mcp
```

The server uses the MCP stdio transport so that Claude can communicate with it locally.

---

# Claude Plugin Configuration

The repository includes a Claude plugin manifest:

```text
google-ads-manager/.claude-plugin/plugin.json
```

and an MCP configuration:

```text
google-ads-manager/.mcp.json
```

The MCP configuration uses:

```text
${CLAUDE_PLUGIN_ROOT}
```

so the plugin can locate its own server installation.

---

# Google Ads Setup Command

The plugin includes a setup command:

```text
/google-ads-setup
```

Use it as a guided workflow for configuring:

1. Google Ads developer credentials
2. Google Cloud service-account credentials
3. Google Ads customer ID
4. MCC/login customer ID where applicable
5. Local credential storage
6. API connectivity verification

Never paste private credentials into GitHub, public issues, or public chat.

---

# Repository Structure

```text
google-ads-claude-plugin/
│
├── .claude-plugin/
│   └── marketplace.json
│
├── google-ads-manager/
│   ├── .claude-plugin/
│   │   └── plugin.json
│   │
│   ├── commands/
│   │   └── google-ads-setup.md
│   │
│   ├── skills/
│   │   └── google-ads-manager/
│   │       └── SKILL.md
│   │
│   ├── src/
│   │   └── google_ads_mcp/
│   │       ├── server.py
│   │       ├── client.py
│   │       ├── config.py
│   │       ├── helpers.py
│   │       └── tools/
│   │
│   └── .mcp.json
│
├── tests/
├── README.md
├── LICENSE
└── pyproject.toml
```

---

# Development

Install the development environment:

```bash
uv sync
```

Run tests:

```bash
uv run pytest
```

Run the server locally:

```bash
uv run google-ads-mcp
```

---

# Google Ads AI Agent Use Cases

This plugin is particularly useful for:

### PPC Managers

Quickly inspect campaign performance and make controlled changes without manually navigating every Google Ads interface.

### Marketing Agencies

Manage multiple Google Ads accounts through MCC access and use Claude for reporting and operational workflows.

### Growth Teams

Combine Google Ads data with broader marketing analysis and ask Claude for campaign insights.

### Performance Marketers

Investigate spend, keywords, search terms, ads, budgets, and Performance Max performance conversationally.

### Automation Specialists

Use MCP tools as building blocks for AI-assisted Google Ads workflows and automation.

---

# Example Workflow

A typical workflow might look like:

```text
You:
"Show me campaigns that spent more than $1,000
in the last 30 days."

Claude:
[Retrieves campaign performance]

You:
"Which of these have the weakest conversion performance?"

Claude:
[Analyzes the returned data]

You:
"Show me the keywords responsible for the spend."

Claude:
[Retrieves keyword/search-term data]

You:
"Pause the worst-performing campaign."

Claude:
[Summarizes the proposed change and requests confirmation]

You:
"Confirm."

Claude:
[Executes the approved change]
```

This makes Claude useful not only as a reporting interface, but as an **AI agent for Google Ads operations**.

---

# Google Ads + Claude + MCP

This project combines three components:

**Claude**

The conversational AI interface and reasoning layer.

**MCP**

The Model Context Protocol layer that exposes structured Google Ads capabilities to Claude.

**Google Ads API**

The underlying advertising platform used to read and modify Google Ads resources.

Together, they create a conversational Google Ads management workflow.

---

# Project Status

This project is under active development.

The current plugin provides approximately **47 tools** covering Google Ads accounts, campaigns, ad groups, ads, keywords, Performance Max, budgets, reporting, and utilities.

Capabilities and Google Ads API compatibility may evolve as the project develops.

---

# Contributing

Contributions, bug reports, feature requests, and improvements are welcome.

Before submitting changes:

```bash
uv run pytest
```

Please follow the project's contribution guidelines in:

```text
CONTRIBUTING.md
```

---

# License

Apache License 2.0.

See [`LICENSE`](LICENSE) for the complete license text.

---

# Keywords

Claude Google Ads plugin · Google Ads AI agent · Claude AI Google Ads · Claude Cowork Google Ads · Google Ads automation · Google Ads MCP · Google Ads MCP server · Google Ads campaign management · Google Ads reporting · PPC AI agent · Google Ads optimization · Search Ads automation · Display Ads automation · Performance Max automation
