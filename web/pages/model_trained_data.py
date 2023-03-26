from dash import html
from page_elements.content import table
from services.data import Data


def model_trained_data():
    return html.Div(
        [
            html.H1("Данные модели"),
            html.Div(
                children=table.generate_table(Data().get_data('./data/train_user_data.csv'))
            )
        ]
    )
