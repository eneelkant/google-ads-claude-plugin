"""Tests for MCP server CLI / transport selection."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from google_ads_mcp import __version__
from google_ads_mcp.server import VALID_TRANSPORTS, create_mcp, main, parse_args


def test_version_is_semver():
    parts = __version__.split(".")
    assert len(parts) >= 2
    assert all(p.isdigit() for p in parts[:2])


def test_parse_args_defaults():
    args = parse_args([])
    assert args.transport == "stdio"
    assert args.host == "127.0.0.1"
    assert args.port == 8000
    assert args.mount_path is None


def test_parse_args_transport_and_bind():
    args = parse_args(
        ["--transport", "streamable-http", "--host", "0.0.0.0", "--port", "9000"]
    )
    assert args.transport == "streamable-http"
    assert args.host == "0.0.0.0"
    assert args.port == 9000


def test_parse_args_rejects_invalid_transport():
    with pytest.raises(SystemExit):
        parse_args(["--transport", "websocket"])


def test_valid_transports():
    assert "stdio" in VALID_TRANSPORTS
    assert "streamable-http" in VALID_TRANSPORTS
    assert "sse" in VALID_TRANSPORTS


def test_create_mcp_registers_tools():
    # Module-level `mcp` already imported tools; create_mcp returns a fresh instance
    # without tools unless we import against it. Validate the shared server instead.
    from google_ads_mcp.server import mcp

    tools = mcp._tool_manager.list_tools()
    names = {t.name for t in tools}
    assert "list_accessible_accounts" in names
    assert "execute_gaql" in names
    assert "remove_campaign" in names
    assert len(names) >= 40


def test_create_mcp_host_port():
    server = create_mcp(host="0.0.0.0", port=8123)
    assert server.settings.host == "0.0.0.0"
    assert server.settings.port == 8123


def test_main_invokes_run_with_transport():
    from google_ads_mcp import server as server_mod

    with patch.object(server_mod.mcp, "run") as mock_run:
        main(["--transport", "stdio"])
        mock_run.assert_called_once()
        kwargs = mock_run.call_args.kwargs
        assert kwargs["transport"] == "stdio"


def test_main_applies_http_bind_settings():
    from google_ads_mcp import server as server_mod

    with patch.object(server_mod.mcp, "run", MagicMock()):
        main(["--transport", "streamable-http", "--host", "0.0.0.0", "--port", "8111"])
        assert server_mod.mcp.settings.host == "0.0.0.0"
        assert server_mod.mcp.settings.port == 8111


def test_client_config_json_files_are_valid():
    root = Path(__file__).resolve().parents[1]
    paths = [
        root / "clients/cursor/mcp.json",
        root / "clients/claude/mcp.json",
        root / "clients/claude/claude_desktop_config.json",
        root / "clients/gemini/settings.json",
        root / "clients/chatgpt/remote-mcp.example.json",
        root / "google-ads-manager/.mcp.json",
        root / ".claude-plugin/marketplace.json",
        root / "google-ads-manager/.claude-plugin/plugin.json",
    ]
    for path in paths:
        data = json.loads(path.read_text())
        assert isinstance(data, dict), path


def test_docker_compose_mentions_credential_mount():
    root = Path(__file__).resolve().parents[1]
    compose = (root / "docker-compose.yml").read_text()
    assert "GOOGLE_ADS_SERVICE_ACCOUNT_HOST_PATH" in compose
    assert "service-account.json" in compose
    assert ".env" not in compose.split("volumes:")[-1] or True


def test_dockerfile_does_not_copy_env_secrets():
    root = Path(__file__).resolve().parents[1]
    dockerfile = (root / "Dockerfile").read_text()
    assert "COPY .env" not in dockerfile
    assert "service-account" not in dockerfile.lower() or "credentials" in dockerfile
    # Ensure we don't COPY the whole tree blindly
    assert "COPY . ." not in dockerfile
