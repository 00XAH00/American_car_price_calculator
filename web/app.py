import dash_bootstrap_components as dbc
import flask
from page_elements.main_page import layout
from dash_extensions.enrich import DashProxy, LogTransform, NoOutputTransform


app_server = flask.Flask(__name__)
app = DashProxy(
    title="CarCalc",
    update_title="CarCalc updating>>>",
    transforms=[LogTransform(), NoOutputTransform()],
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    ],
    server=app_server
)


app.layout = layout
