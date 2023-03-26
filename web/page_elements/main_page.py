import dash_bootstrap_components as dbc
from dash import html, dcc
from page_elements.content.content import content
from page_elements.side_menu.menu import menu

layout = html.Div(
    [
        dbc.Row(
            [
                menu,
                content,
            ],
            className="main-row"
        ),
        html.Div("train", id="cr")
    ],
)
