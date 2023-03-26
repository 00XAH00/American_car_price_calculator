import dash
from dash import Input, State, Output, ctx
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import DashLogger
from app import app
from core.settings import settings
from page_elements.content import table
from services.Authorize import Authorize
from services.server import ServerApi


@app.callback(
    Output("login-btn-div", "children"),
    Output('output-image-upload', 'children'),
    Input('calc-btn', "n_clicks"),
    State('table', 'data'),
    log=True,
)
def calc_model(n1, table_data, dash_logger: DashLogger):
    if ctx.triggered[0]["value"] is None:
        raise PreventUpdate
    authorize = Authorize()
    server = ServerApi()

    if not authorize.is_auth():
        dash_logger.info("Для продолжения необходимо авторизоваться!", autoClose=settings.notify_auto_close_time)
        return [dash.no_update, dash.no_update]
    if len(table_data) == 1:
        dash_logger.info("Для расчета цен необходимо загрузить данные!",
                         autoClose=settings.notify_auto_close_time)
        return [None, dash.no_update]

    dash_logger.info("Цена посчитана!:)")
    return [dash.no_update, table.generate_table(server.calc_price(table_data))]
