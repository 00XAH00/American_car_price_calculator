import dash
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, State, DashLogger, ctx
from pandas.core.frame import DataFrame
from app import app
from core.settings import settings
from page_elements.content import table
from services.file import UploadFile


@app.callback(
    Output('output-image-upload', 'children'),
    Input('upload-image', 'contents'),
    State('upload-image', 'filename'),
    State('cr', 'children'), log=True)
def update_output(content: str, name: str, cr: str, dash_logger: DashLogger):
    if ctx.triggered_id is None:
        raise PreventUpdate
    elif cr == 'calc':
        with_price = False
    else:
        with_price = True

    if content is not None:
        upload_file = UploadFile()

        if not upload_file.type_validate(name):
            dash_logger.warning("Файл должен быть в формате csv!", autoClose=settings.notify_auto_close_time)
            return dash.no_update

        input_data = upload_file.read_from_content(content)
        if not isinstance(input_data, DataFrame):
            dash_logger.error("Не удалось прочитать содержимое файла", autoClose=settings.notify_auto_close_time)
            return dash.no_update

        if not upload_file.table_structure_validate(input_data, with_price=with_price):
            dash_logger.warning("Структура файла не соответствует примеру", autoClose=settings.notify_auto_close_time)
            return dash.no_update

        return table.generate_table(input_data)

    return dash.no_update
