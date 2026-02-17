import uvicorn
import logging
import debugpy
import settings
import importlib

from common.classes import Singleton

logger = logging.getLogger(__name__)


class RunServer(Singleton):
    """Start the server with the specified parameters."""
    def __init__(
            self, 
            app: str = "server.config:app", 
            host: str = "127.0.0.1", 
            port: int = 8000, 
            reload: bool = True, 
            debug: bool = False,
            debug_port: int = 5678) -> None:
        """
        Data for class initialization.

        :param app: The application to run.
        :param host: The host to run the server on.
        :param port: The port to run the server on.
        :param reload: Whether to reload the server on code changes.
        """
        self.app = app
        self.host = host 
        self.port = port
        self.reload = reload
        self.debug = debug
        self.debug_port = debug_port

    def run(self) -> None:
        """
        Run the server handling both Debug and Reload logic properly.
        """
        self.read_app()

        if self.debug:
            self.__start_debug()

        logger.info(f"Server starting on {self.host}:{self.port} (reload={self.reload})")

        uvicorn.run(
            self.app,
            host=self.host,
            port=self.port,
            reload=self.reload,
            log_level="debug" if self.debug else "info",
        )

    def __start_debug(self):
        self.reload = False
        debugpy.listen((self.host, self.debug_port))
        logger.debug(f"🚀 Waiting for debugger on port {self.debug_port}...")
        debugpy.wait_for_client()
        logger.debug("✅ Debugger attached!")

    def read_app(self):
        self.read_rouds()

    def read_rouds(self):
        apps = settings.apps

        for app in apps:
            importlib.import_module(f"{app}.routs")
