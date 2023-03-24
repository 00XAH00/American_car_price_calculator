import dash
from dash_extensions.enrich import DashLogger
from flask import request
from dash import Output, State, Input, html
from app import app
from core.settings import settings


@app.callback(
    [
        Output("modal", "is_open"),
        Output("login-btn-div", "children")
    ],
    Input("open-login-form", "n_clicks"), State("modal", "is_open"),
    log=True
)
def open_form(n1: int, is_open: bool, dash_logger: DashLogger):
    if not request.cookies.to_dict().get("user-token"):
        return [not is_open, dash.no_update]
    dash_logger.info("Вход выполнен успешно!", autoClose=settings.notify_auto_close_time)
    return [dash.no_update, html.Div()]
