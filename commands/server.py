import logging
import typer
from typing import Annotated
from server.run import RunServer

logger = logging.getLogger(__name__)

server_app = typer.Typer(help="Commands for controlling the server.")


@server_app.command()
def start(
    debug: Annotated[bool, typer.Option(help="Увімкнути режим налагодження")] = False,
):
    """
    Start the server with configurable options.
    """
    server = RunServer(
        debug=debug, 
    )
    server.run()
