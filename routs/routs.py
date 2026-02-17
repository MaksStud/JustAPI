from typing import Dict
from common.classes import Singleton
from request_response.response import Response, HTMLResponse
from request_response.status_code import StatusCode


class Routs(Singleton):
    """
    A singleton class responsible for managing and storing application routes.

    This class maintains a registry of route strings mapped to their 
    respective response objects, ensuring that only one instance of the 
    registry exists throughout the application lifecycle.

    :ivar routs: A dictionary mapping route paths (strings) to Response objects.
    """
    def __init__(self) -> None:
        """
        Initialize the Routs instance.

        Checks if the 'routs' attribute already exists to prevent overwriting 
        data during multiple singleton access attempts.
        """
        if not hasattr(self, "routs"):
            self.routs: Dict[str, Response] = {}

    def register(self, rout: str, response: Response) -> None:
        """
        Register a new route or update an existing one.

        :param rout: The URL path or identifier for the route.
        :param response: The Response object to be associated with this route.
        """
        self.routs[rout] = response

    async def get_resonse(self, rout: str) -> Response:
        """
        Retrieve a response for a specific route asynchronously.

        If the route is not found in the registry, returns a default 
        404 Not Found HTML response.

        :param rout: The URL path to look up.
        :return: The associated Response object or an HTMLResponse (404).
        :rtype: Response
        """
        return self.routs.get(rout, HTMLResponse("<p><b>ERROR<b/><p/>", status_code=StatusCode.NOT_FOUND))

    def __reduce__(self) -> str:
        """
        Define the pickling behavior for the Routs instance.

        :return: A string representation for object reconstruction.
        :rtype: str
        """
        return f"{self.__class__.__name__}(self.routs={self.routs})"

    def __str__(self) -> str:
        """
        Return a string representation of the Routs instance.

        :return: A string containing the current routes dictionary.
        :rtype: str
        """
        return f"{self.__class__.__name__}(self.routs={self.routs})"
