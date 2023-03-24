from random import choice
from typing import List
from core.settings import settings


class ServerApi:
    def __init__(self):
        self.__url = settings.backend_url

    def train_model(self, model_type: int, data: List, hyperparametrs: dict = None) -> bool:
        print(self.__url)
        return True

    @staticmethod
    def auth(login: str, password: str):
        if choice([0, 1]) == 1:
            return False
        result = ''.join([choice(login) for i in range(10)])
        result += ''.join([choice(password) for i in range(20)])
        result += ''.join([choice(login) for i in range(7)])
        result += ''.join([choice(password) for i in range(3)])
        result += ''.join([choice(login) for i in range(10)])

        return result
