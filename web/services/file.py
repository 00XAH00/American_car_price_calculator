import base64
import io
from typing import Union

import numpy as np
import pandas as pd
from pandas import DataFrame
from services.data import Data


class UploadFile:
    def __init__(self):
        self.data = Data()

    @staticmethod
    def type_validate(file_name: str) -> bool:
        split_name = file_name.split(".")
        file_format = split_name[-1]

        if file_format == "csv":
            return True

        return False

    def table_structure_validate(self, input_data: DataFrame):
        example_data = self.data.get_example_table()
        example_data_columns = example_data.columns
        input_data_columns = input_data.columns

        return np.array_equal(example_data_columns, input_data_columns)

    @staticmethod
    def read_from_content(content: str) -> Union[DataFrame, None]:
        _, content_string = content.split(',')

        # noinspection PyBroadException
        try:
            decoded = base64.b64decode(content_string)

            # noinspection PyTypeChecker
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

            return df

        except:
            return None
