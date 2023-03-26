import json
from os.path import exists
from random import choice
from typing import List, Union
import numpy as np
import pandas as pd
from pandas import DataFrame
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

    @staticmethod
    def send_train_data(data: List):
        with open('./data/train_user_data.csv', 'w') as f:
            f.write(','.join([key for key in data[0].keys()]) + '\n')
            for line in data:
                f.write(','.join([str(item[1]) for item in line.items()]) + '\n')

    def get_data(self, path_to_file: str) -> Union[DataFrame, None]:
        if not self.validate_path(path_to_file):
            return None
        return pd.read_csv(path_to_file)

    @staticmethod
    def validate_path(path_to_file: str):
        return exists(path_to_file)

    @staticmethod
    def calc_price(data: List) -> DataFrame:
        data = pd.read_json(json.dumps(data))
        data = data.assign(price=(pd.Series(np.random.random(len(data))).values*100000).round())
        data["price"] = data['price'].astype('int')

        return data
