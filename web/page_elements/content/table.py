from dash import dash_table
from pandas import DataFrame
from services.data import Data


def generate_table(table: DataFrame = Data().get_example_table()):
    table = dash_table.DataTable(
        id="table",
        data=table.to_dict('records'),
        columns=[{"name": i, "id": i} for i in table.columns],
        style_data={
            'backgroundColor': '#31302f',
            'color': 'white'
        },
        page_size=50
    )

    return table
