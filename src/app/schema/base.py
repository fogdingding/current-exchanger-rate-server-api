from pydantic import BaseModel


class ApiException(Exception):
    def __init__(self,
                 code: int,
                 msg: str,
                 detail: dict = {}):
        self.code = code
        self.msg = msg
        self.detail = detail


class ApiErrorResponse(BaseModel):
    code: int = -1
    message: str = ""
