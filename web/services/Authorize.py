from flask import request
from services.server import ServerApi


class Authorize(ServerApi):
    def __init__(self):
        super().__init__()

    def is_auth(self) -> bool:
        token = request.cookies.to_dict().get("user-token")
        return self.validate_token(token)

    @staticmethod
    def validate_token(token: str) -> bool:
        return True
