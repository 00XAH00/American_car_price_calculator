from typing import Union
import pandas as pd
from pandas import DataFrame
from services.server import ServerApi


class Data(ServerApi):
    def __init__(self):
        super().__init__()

    def get_example_table(self) -> Union[DataFrame, None]:
        if not self.validate_path('./data/car_prices_example.csv'):
            return None
        example_data = pd.read_csv('./data/car_prices_example.csv', parse_dates=True)

        return example_data
