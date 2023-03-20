import dash_bootstrap_components as dbc
from dash import html

from page_elements.side_menu.buttons import buttons

menu = dbc.Col(
    [
        html.H2("Расчет стоимости Американских АТ"),
        dbc.Col(
            buttons("model-train-btn"),
            id="button-column"
        )
    ],
    width=3,
    className="user-controls"
)
