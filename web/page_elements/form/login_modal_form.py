import dash_bootstrap_components as dbc
from page_elements.form.input import form_input


login_form = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Вход")),
        dbc.ModalBody(
            [
                form_input(
                    input_id="user-login",
                    placeholder="Логин"
                ),
                form_input(
                    input_id="user-password",
                    placeholder="Пароль"
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
