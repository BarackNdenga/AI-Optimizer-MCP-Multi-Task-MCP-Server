"""CLI entrypoint for ai-optimizer-mcp."""
import argparse
import asyncio
import logging
from pathlib import Path

from .server import main
from .config import load_dotenv  # Ensure loaded

logging.basicConfig(level=logging.INFO)

def parse_args():
    parser = argparse.ArgumentParser(description="AI Optimizer MCP Server")
    parser.add_argument("run", nargs="?", default="server", choices=["server"], help="Run server")
    parser.add_argument("--dev", action="store_true", help="Dev mode (logs)")
    parser.add_argument("--install-mcp", action="store_true", help="Print VSCode mcp.json")
    return parser.parse_args()

async def async_main():
    args = parse_args()
    if args.dev:
        logging.getLogger().setLevel(logging.DEBUG)
    if args.install_mcp:
        print('''{
  "servers": {
    "ai-optimizer": {
      "command": "python",
      "args": ["-m", "ai_optimizer_mcp.server"]
    }
  }
}''')
        return
    await main()

if __name__ == "__main__":
    asyncio.run(async_main())

