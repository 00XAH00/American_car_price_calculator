from dash import Output, State, Input
from app import app


@app.callback(Output("modal", "is_open"),
              Input("open-login-form", "n_clicks"),
              State("modal", "is_open"))
def open_form(n_clicks: int, is_open: bool):
    return not is_open
