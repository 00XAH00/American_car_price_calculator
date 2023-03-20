import dash_bootstrap_components as dbc
from page_elements.main_page import layout
from dash_extensions.enrich import DashProxy, LogTransform

app = DashProxy(
    transforms=[LogTransform()],
    prevent_initial_callbacks=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = layout
