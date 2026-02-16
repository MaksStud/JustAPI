import uvicorn
import logging

logger = logging.getLogger(__name__)


class RunServer:
    """Start the server with the specified parameters."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance of the server.
        :return: The new instance of the server.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
            self, 
            app: str = "server.config:app", 
            host: str = "127.0.0.1", 
            port: int = 8000, 
            reload: bool = True) -> None:
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

    def run(self) -> None:
        """
        Run the server.
        """
        uvicorn.run(
            self.app, 
            host=self.host, 
            port=self.port,
            reload=self.reload,
        )
