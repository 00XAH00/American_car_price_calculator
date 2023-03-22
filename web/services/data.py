import pandas as pd
from pandas import DataFrame
from os import system


class Data:
    def __init__(self): ...

    # TODO: Изменить на получение данных с сервера
    @staticmethod
    def get_example_table():
        example_data = pd.read_csv('./data/car_prices_example.csv', parse_dates=True)

        return example_data

    @staticmethod
    def send_train_data(data: DataFrame):
        system("rm ./data/train_user_data.csv")
        data.to_csv('./data/train_user_data.csv')
