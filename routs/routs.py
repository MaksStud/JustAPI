from typing import Dict, Optional, List
from common.classes import Singleton
from request_response.response import Response, HTMLResponse
from request_response.status_code import StatusCode
from routs.errors import Errors


class RoutsTreeNode:
    """
    Node of a routing tree.

    :param segment: URL path segment stored in this node.
    :type segment: str
    """

    def __init__(self, segment: str):
        self.segment = segment
        self.children: Dict[str, RoutsTreeNode] = {}
        self.response: Optional[Response] = None


class Routs(Singleton):
    """
    Routing registry implemented as a tree.

    Stores routes as path segments and resolves them to responses.
    """

    def __init__(self):
        """
        Initialize routing tree root node.
        """
        if hasattr(self, "root"):
            return
        self.root = RoutsTreeNode("/")

    def register(self, path: str, response: Response) -> None:
        """
        Register a new route.

        :param path: URL path.
        :type path: str
        :param response: Response object bound to the path.
        :type response: Response
        :raises ValueError: If route already registered.
        """
        segments = self._prepare_path(path)
        node = self.root

        for segment in segments:
            if segment not in node.children:
                node.children[segment] = RoutsTreeNode(segment)
            node = node.children[segment]

        if node.response is not None:
            raise ValueError(Errors.ROUTE_DUPLICATION)

        node.response = response

    async def get_response(self, path: str) -> Response:
        """
        Resolve path to a response.

        :param path: Request path.
        :type path: str
        :return: Matched response or 404 response.
        :rtype: Response
        """
        segments = self._prepare_path(path)
        node = self.root

        if not segments:
            if self.root.response:
                return self.root.response
        else:
            for segment in segments:
                if segment in node.children:
                    node = node.children[segment]
                else:
                    return self._not_found()

        if node.response:
            return node.response

        return self._not_found()

    def _prepare_path(self, path: str) -> List[str]:
        """
        Normalize and split path into segments.

        :param path: Raw request path.
        :type path: str
        :return: List of path segments.
        :rtype: List[str]
        """
        return [segment for segment in path.strip("/").split("/") if segment]

    def _not_found(self) -> Response:
        """
        Create default 404 response.

        :return: HTML 404 response.
        :rtype: Response
        """
        return HTMLResponse(
            "<p><b>404 NOT FOUND</b><p/>",
            status_code=StatusCode.NOT_FOUND
        )
