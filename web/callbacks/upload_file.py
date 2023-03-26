import dash
from dash_extensions.enrich import Input, Output, State, DashLogger
from pandas.core.frame import DataFrame
from app import app
from core.settings import settings
from page_elements.content import table
from services.file import UploadFile


@app.callback(Output('output-image-upload', 'children'), Input('upload-image', 'contents'),
              State('upload-image', 'filename'), State('upload-image', 'last_modified'), log=True)
def update_output(content: str, name: str, date: int, dash_logger: DashLogger):
    if content is not None:
        upload_file = UploadFile()

        if not upload_file.type_validate(name):
            dash_logger.warning("Файл должен быть в формате csv!", autoClose=settings.notify_auto_close_time)
            return dash.no_update

        input_data = upload_file.read_from_content(content)
        if not isinstance(input_data, DataFrame):
            dash_logger.error("Не удалось прочитать содержимое файла", autoClose=settings.notify_auto_close_time)
            return dash.no_update

        if not upload_file.table_structure_validate(input_data):
            dash_logger.warning("Структура файла не соответствует примеру", autoClose=settings.notify_auto_close_time)

        # TODO: Переместить в callback кнопки для тренировки модели
        upload_file.data.send_train_data(input_data)

        return table.generate_table(input_data)

    return dash.no_update
