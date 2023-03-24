import dash_bootstrap_components as dbc
from page_elements.main_page import layout
from dash_extensions.enrich import DashProxy, LogTransform, NoOutputTransform

app = DashProxy(
    transforms=[LogTransform(), NoOutputTransform()],
    prevent_initial_callbacks=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    ]
)


app.layout = layout
