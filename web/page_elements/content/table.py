from dash import dash_table, html
from pandas import DataFrame
from services.data import Data


def generate_table(table_input: DataFrame = Data().get_example_table(), page_size: int = 50, with_price: bool = True):
    if isinstance(table_input, DataFrame):
        if not with_price:
            table_input.drop(['price'], axis=1, inplace=True)

        table = dash_table.DataTable(
            id="table",
            data=table_input.to_dict('records'),
            columns=[{"name": i, "id": i} for i in table_input.columns],
            style_data={
                'backgroundColor': '#31302f',
                'color': 'white'
            },
            page_size=page_size
        )
        return table

    return html.H4("Данные модели отсутствуют", className="data-not-exists")
