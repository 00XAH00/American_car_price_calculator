import dash_bootstrap_components as dbc
from dash import html
from page_elements.form.input import form_input


login_form = html.Div(
    children=[
        dbc.Button(
            id="open-login-form",
            children="Войти"
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Вход")),
                dbc.ModalBody(
                    [
                        form_input(
                            input_id="user-login",
                            placeholder="Логин",
                        ),
                        form_input(
                            input_id="user-password",
                            placeholder="Пароль",
                            input_type="password"
                        )
                    ]
                ),
                dbc.ModalFooter(
                    dbc.Button(
                        "Войти",
                        id="login-btn",
                        className="ms-auto"
                    ),
                ),
            ],
            id="modal",
            is_open=False,
        )
    ],
    id="login-btn-div"
)
