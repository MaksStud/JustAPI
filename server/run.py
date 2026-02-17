import uvicorn
import logging
import debugpy
import settings

from common.classes import Singleton

logger = logging.getLogger(__name__)


class RunServer(Singleton):
    """
    A singleton class to configure and launch the Uvicorn server.

    This class encapsulates server settings and provides a unified interface 
    to start the application in either standard, reload, or debug mode.

    :ivar app: The ASGI application import string.
    :ivar host: The network interface to bind the server to.
    :ivar port: The TCP port for the server.
    :ivar reload: Boolean flag for hot-reloading on code changes.
    :ivar debug: Boolean flag to enable remote debugging via ``debugpy``.
    :ivar debug_port: The port designated for the debugger connection.
    """

    def __init__(
            self, 
            app: str = "server.config:app", 
            host: str = "127.0.0.1", 
            port: int = 8000, 
            reload: bool = True, 
            debug: bool = False,
            debug_port: int = 5678) -> None:
        """
        Initialize the server configuration.

        :param app: The application path (e.g., 'module:attribute').
        :param host: The host address to run the server on.
        :param port: The port number to listen on.
        :param reload: If True, the server restarts on file modifications.
        :param debug: If True, activates ``debugpy`` for remote debugging.
        :param debug_port: The port used by the debugger.
        """
        self.app = app
        self.host = host 
        self.port = port
        self.reload = reload
        self.debug = debug
        self.debug_port = debug_port

    def run(self) -> None:
        """
        Start the Uvicorn server with the configured parameters.

        This method coordinates the startup sequence. If :attr:`debug` is 
        enabled, it initializes the debugger and forces :attr:`reload` to 
        False to prevent process cycling during a debug session.
        """
        if self.debug:
            self.__start_debug()

        logger.info(f"Server starting on {self.host}:{self.port} (reload={self.reload})")

        uvicorn.run(
            self.app,
            host=self.host,
            port=self.port,
            reload=self.reload,
            log_config=settings.LOGGING_CONFIG
        )

    def __start_debug(self) -> None:
        """
        Initialize the debugpy listener.

        Configures the server for remote debugging. Note that this 
        automatically disables the reload feature to ensure stability 
        while the debugger is attached.

        :raises ImportError: If ``debugpy`` is not installed in the environment.
        """
        self.reload = False
        debugpy.listen((self.host, self.debug_port))
        debugpy.wait_for_client()
