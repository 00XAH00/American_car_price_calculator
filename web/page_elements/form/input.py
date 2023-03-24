from dash_extensions.enrich import html
import dash_bootstrap_components as dbc


def form_input(input_id: str, placeholder: str, input_type: str = "text") -> html.Div:
    return html.Div(
        [
            html.P(placeholder),
            dbc.Input(
                placeholder=placeholder,
                id=input_id,
                type=input_type
            )
        ],
        className="modal-form-input"
    )
