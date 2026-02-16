from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar
import json

from rouds.status_code import StatusCode
from rouds.content_type import ContentType
from rouds.endcodes import TextEncoding


T = TypeVar("T")
endcode = TextEncoding.UTF_8


class Response(Generic[T], ABC):
    """Base class for Response sup classes."""
    def __init__(self, body: T, 
                 status_code: int = StatusCode.SUCCESS, 
                 headers: dict = {}):
        self.body = body
        self.status_code = status_code
        self.content_type = ContentType.TEXT_HTML
        self.headers = [[b'content-type', self.content_type]]

    async def __call__(self, send):
        """Sends a response to the sender of the request."""
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
        """Return response to bytes. Need to Implemented in junior classes."""
        raise NotImplementedError()


class JsonResponse(Response[dict]):
    """Sends a response in JSON format."""
    def __init__(self, body: T, status_code: int = StatusCode.SUCCESS, headers: dict = {}):
        super().__init__(body, status_code, headers)
        self.content_type = ContentType.APPLICATION_JSON

    async def to_bytes(self, body: Optional[dict]) -> bytes:
        """
        Endcode JSON to bytes.

        :param body: JSON code.

        :return: Bytes format.
        """
        if body is None:
            return b""

        return json.dumps(body, ensure_ascii=False).encode(endcode)


class HTMLResponse(Response[str]):
    """Sends a response in HTML code format."""
    def __init__(self, body: T, status_code: int = StatusCode.SUCCESS, headers: dict = {}):
        super().__init__(body, status_code, headers)
        self.content_type = ContentType.TEXT_HTML

    async def to_bytes(self, body: Optional[str]) -> bytes:
        """
        Endcode HTML to bytes.

        :param body: HTML code.

        :return: Bytes format.
        """
        if body is None:
            return b""

        return body.encode(endcode)
