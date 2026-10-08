# Universal Google Ads MCP server
# Credentials are injected at runtime via environment variables — never baked into the image.

FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv \
    && useradd --create-home --uid 10001 --shell /usr/sbin/nologin mcp \
    && mkdir -p /credentials \
    && chown -R mcp:mcp /app /credentials

# Copy only packaging metadata and source (no .env, no keys — see .dockerignore)
COPY --chown=mcp:mcp pyproject.toml README.md ./
COPY --chown=mcp:mcp src ./src

RUN uv pip install --system --no-cache .

USER mcp

ENV MCP_TRANSPORT=streamable-http \
    MCP_HOST=0.0.0.0 \
    MCP_PORT=8000 \
    PYTHONUNBUFFERED=1

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import os,sys,urllib.request; t=os.environ.get('MCP_TRANSPORT','streamable-http');\
sys.exit(0) if t=='stdio' else urllib.request.urlopen('http://127.0.0.1:%s/mcp'%os.environ.get('MCP_PORT','8000'), timeout=3)" || exit 1

ENTRYPOINT ["google-ads-mcp"]
CMD ["--transport", "streamable-http", "--host", "0.0.0.0", "--port", "8000"]
