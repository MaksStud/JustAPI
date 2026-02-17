from typing import Dict
from common.classes import Singleton
from request_response.response import Response, HTMLResponse
from request_response.status_code import StatusCode


class Routs(Singleton):
    def __init__(self) -> None:
        if not hasattr(self, "routs"):
            self.routs: Dict[str, Response] = {}

    def set(self, rout: str, response: Response) -> None:
        self.routs[rout] = response

    async def get_resonse(self, rout: str) -> Response:
        return self.routs.get(rout, HTMLResponse("<p><b>error<b/><p/>", status_code=StatusCode.NOT_FOUND))

    def __reduce__(self) -> str:
        return f"Routs(self.routs={self.routs})"

    def __str__(self) -> str:
        return f"Routs(self.routs={self.routs})"
