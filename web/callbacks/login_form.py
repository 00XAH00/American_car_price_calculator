from dash import html
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

    user_token = authorize.auth(user_login, user_password)

    if not user_token:

        print(dash_logger)
        dash_logger.warning("Не верный логин или пароль")
        return login_form

    return None
