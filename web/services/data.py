import pandas as pd


class Data:
    def __init__(self): ...

    # TODO: Изменить на получение данных с сервера
    @staticmethod
    def get_example_table():
        example_data = pd.read_csv('./data/car_prices_example.csv', parse_dates=True)

        return example_data
