import uvicorn
import typer
import logging

logger = logging.getLogger(__name__)

server_app = typer.Typer(help="Commands for controlling the server.")


@server_app.command()
def start(port: int = 8000, reload: bool = True):
    logger.info(f"🚀 Launch at the port {port}...")
    uvicorn.run("server.config:app", host="127.0.0.1", port=port, reload=reload)


@server_app.command()
def status():
    logger("🌐 The server is ready to go.")
