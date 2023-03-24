import dash
import flask
from dash_extensions.enrich import Output, State, Input
from dash_extensions.enrich import DashLogger
from app import app
from page_elements.form.login_modal_form import login_form
from services.Authorize import Authorize


@app.callback(
    Output("login-btn-div", "children"),
    Input("login-btn", "n_clicks"),
    [
        State("user-login", "value"),
        State("user-password", "value"),

    ],
    log=True
)
def open_form(n1: int, user_login: str, user_password: str, dash_logger: DashLogger):
    authorize = Authorize()
    # print(flask.request.cookies.to_dict())

    user_token = authorize.auth(user_login, user_password)

    if not user_token:
        dash_logger.warning("Не верный логин или пароль")
        return login_form

    dash.callback_context.response.set_cookie("token", user_token)

    return None
