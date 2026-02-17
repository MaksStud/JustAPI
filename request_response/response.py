from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar
import json

from request_response.status_code import StatusCode
from request_response.content_type import ContentType
from request_response.endcodes import TextEncoding


T = TypeVar("T")
encode = TextEncoding.UTF_8


class Response(Generic[T], ABC):
    """
    Base class for all response types.

    :param body: Response body content.
    :type body: T
    :param status_code: HTTP status code.
    :type status_code: int
    :param headers: Additional HTTP headers.
    :type headers: dict
    """

    def __init__(self, body: T, 
                 status_code: int = StatusCode.SUCCESS, 
                 headers: dict = {}):
        self.body = body
        self.status_code = status_code
        self.content_type = self._set_content_type()
        self.headers = [[b'content-type', self.content_type]]

    def _set_content_type(self):
        """
        Define content type for the response.

        :return: Content-Type header value.
        :rtype: bytes
        """
        return ContentType.TEXT_HTML

    async def __call__(self, send):
        """
        Send ASGI response.

        :param send: ASGI send callable.
        :type send: Callable
        """
        await send({
            'type': 'http.response.start',
            'status': self.status_code,
            'headers': self.headers,
        })
        await send({
            'type': 'http.response.body',
            'body': await self.to_bytes(self.body),
        })

    @abstractmethod
    async def to_bytes(self, body: Optional[bytes]) -> bytes:
        """
        Convert response body to bytes.

        Must be implemented in subclasses.

        :param body: Response body.
        :type body: Optional[bytes]
        :return: Encoded body.
        :rtype: bytes
        """
        raise NotImplementedError()

    def __reduce__(self) -> str:
        """
        Debug representation used for serialization.

        :return: Debug string.
        :rtype: str
        """
        return f"Class: {self.__name__} -> {self.body=}, {self.status_code=}, {self.content_type=}, {self.headers}"

    def __str__(self) -> str:
        """
        Human-readable representation.

        :return: Debug string.
        :rtype: str
        """
        return f"Class: {self.__class__.__name__} -> {self.body=}, {self.status_code=}, {self.content_type=}, {self.headers}"


class JsonResponse(Response[dict]):
    """
    JSON response implementation.

    Sends response with ``application/json`` content type.
    """

    async def to_bytes(self, body: Optional[dict]) -> bytes:
        """
        Encode JSON body to bytes.

        :param body: JSON serializable object.
        :type body: Optional[dict]
        :return: UTF-8 encoded JSON.
        :rtype: bytes
        """
        if body is None:
            return b""

        return json.dumps(body, ensure_ascii=False).encode(encode)

    def _set_content_type(self):
        """
        Set JSON content type.

        :return: JSON content type header.
        :rtype: bytes
        """
        return ContentType.APPLICATION_JSON


class HTMLResponse(Response[str]):
    """
    HTML response implementation.

    Sends response with HTML content.
    """

    async def to_bytes(self, body: Optional[str]) -> bytes:
        """
        Encode HTML string to bytes.

        :param body: HTML markup.
        :type body: Optional[str]
        :return: UTF-8 encoded HTML.
        :rtype: bytes
        """
        if body is None:
            return b""

        return body.encode(encode)
