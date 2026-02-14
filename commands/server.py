import logging
import typer
from server.run import RunServer

logger = logging.getLogger(__name__)

server_app = typer.Typer(help="Commands for controlling the server.")


@server_app.command()
def start():
    """Start the server."""
    RunServer().run()
