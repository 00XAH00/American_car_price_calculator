import dash_bootstrap_components as dbc
from page_elements.form.login_modal_form import login_form
from pages.train_page import train_page

content = dbc.Col(
    [
        login_form,
        train_page
    ],
    className="user-result"
)
