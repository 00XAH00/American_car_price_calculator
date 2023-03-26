import dash_bootstrap_components as dbc
from dash import html
from page_elements.form.login_modal_form import login_form
from pages.train_page import train_page


content = dbc.Col(
    [
        login_form,
        html.Div(children=train_page, id="user-content-block")
    ],
    className="user-result"
)
