import dash
from dash import Input, State, Output
from dash_extensions.enrich import DashLogger
from app import app
from core.settings import settings
from services.Authorize import Authorize
from services.server import ServerApi


@app.callback(
    Output("login-btn-div", "children"),
    [
        Input('div-train-btn', "n_clicks"),
        State('model-type-row', 'value'),
        State('table', 'data')
    ],
    log=True)
def train_model(n1, model_value, table_data, dash_logger: DashLogger):
    server_api = ServerApi()
    authorize = Authorize()

    if not authorize.is_auth():
        dash_logger.info("Для продолжения необходимо авторизоваться!", autoClose=settings.notify_auto_close_time)
        return
    if len(table_data) == 1:
        dash_logger.info("Для тренировки модели необходимо загрузить данные обучения!",
                         autoClose=settings.notify_auto_close_time)
        return dash.no_update

    print(model_value)

    train_status = server_api.train_model(model_value, table_data)
    if not train_status:
        dash_logger.info("Обучение модели не удалось", autoClose=settings.notify_auto_close_time)
        return

    dash_logger.info("Обучение прошло успешно", autoClose=settings.notify_auto_close_time*2)
    dash_logger.info("Подобранные гиперпараметры: ", autoClose=settings.notify_auto_close_time*2)
    dash_logger.info("Данные метрики: 0.88463625", autoClose=settings.notify_auto_close_time*2)

    print(len(table_data))
