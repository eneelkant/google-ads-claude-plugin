"""FastMCP server definition with lifespan management and transport selection."""

from __future__ import annotations

import argparse
import logging
import os
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from mcp.server.fastmcp import Context, FastMCP

from .client import GoogleAdsClientWrapper
from .config import GoogleAdsSettings

# Configure logging to stderr only (critical for stdio transport)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

VALID_TRANSPORTS = ("stdio", "sse", "streamable-http")


@dataclass
class AppContext:
    """Shared application context available to all tools via lifespan."""

    client: GoogleAdsClientWrapper | None


def get_client(ctx: Context) -> GoogleAdsClientWrapper:
    """Extract the GoogleAdsClientWrapper from MCP tool context.

    Raises:
        RuntimeError: If the Google Ads client failed to initialize at startup.
    """
    client = ctx.request_context.lifespan_context.client
    if client is None:
        raise RuntimeError(
            "Google Ads client is not available. "
            "Check server logs for initialization errors (credentials, service account path, etc.)."
        )
    return client


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Initialize the Google Ads client on server startup.

    If credentials are invalid, the server still starts so stateless tools
    (e.g. convert_micros, list_gaql_resources) remain available.
    """
    logger.info("Starting Google Ads MCP server...")
    client_wrapper: GoogleAdsClientWrapper | None = None
    try:
        settings = GoogleAdsSettings()
        client_wrapper = GoogleAdsClientWrapper(settings)
        logger.info("Google Ads client initialized successfully")
    except Exception as e:
        # Do not log raw credential values — Settings/exception paths may include paths only.
        logger.error("Failed to initialize Google Ads client: %s", e)
        logger.warning(
            "Server will start without API access. Only stateless tools will work."
        )
    try:
        yield AppContext(client=client_wrapper)
    finally:
        logger.info("Google Ads MCP server shutting down")


def create_mcp(*, host: str = "127.0.0.1", port: int = 8000) -> FastMCP:
    """Create the FastMCP server instance.

    Host/port apply only to SSE and streamable-http transports.
    """
    return FastMCP(
        "Google Ads MCP",
        instructions=(
            "Comprehensive Google Ads management with ~47 tools for campaigns, "
            "ads, keywords, Performance Max, reporting, and more."
        ),
        lifespan=app_lifespan,
        host=host,
        port=port,
    )


# Default module-level server used by tool modules (`from ..server import mcp`).
mcp = create_mcp(
    host=os.environ.get("MCP_HOST", "127.0.0.1"),
    port=int(os.environ.get("MCP_PORT", os.environ.get("PORT", "8000"))),
)

# Import all tool modules to register their decorators
import google_ads_mcp.tools  # noqa: E402, F401


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments for transport selection."""
    parser = argparse.ArgumentParser(
        prog="google-ads-mcp",
        description="Universal Google Ads MCP server (stdio, SSE, or streamable HTTP).",
    )
    parser.add_argument(
        "--transport",
        choices=VALID_TRANSPORTS,
        default=os.environ.get("MCP_TRANSPORT", "stdio"),
        help="MCP transport (default: stdio, or MCP_TRANSPORT env).",
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("MCP_HOST", "127.0.0.1"),
        help="Bind host for SSE/streamable-http (default: 127.0.0.1, or MCP_HOST).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("MCP_PORT", os.environ.get("PORT", "8000"))),
        help="Bind port for SSE/streamable-http (default: 8000, or MCP_PORT/PORT).",
    )
    parser.add_argument(
        "--mount-path",
        default=None,
        help="Optional mount path for SSE transport.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Entry point for the MCP server."""
    args = parse_args(argv)

    # Apply host/port to the shared server for HTTP transports.
    mcp.settings.host = args.host
    mcp.settings.port = args.port

    logger.info(
        "Launching Google Ads MCP (transport=%s host=%s port=%s)",
        args.transport,
        args.host,
        args.port,
    )
    mcp.run(transport=args.transport, mount_path=args.mount_path)


if __name__ == "__main__":
    main()
