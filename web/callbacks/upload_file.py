from dash_extensions.enrich import html
from dash_extensions.enrich import Input, Output, State, DashLogger
from app import app


@app.callback(Output('output-image-upload', 'children'), Input('upload-image', 'contents'),
              State('upload-image', 'filename'), State('upload-image', 'last_modified'), log=True)
def update_output(contents, name, dates, dash_logger: DashLogger):
    if contents is not None:
        dash_logger.info("Файл получен:)", autoClose=5000)
        if not type_validate(name):
            dash_logger.warning("Файл должен быть в формате csv!", autoClose=5000)
        return html.Div("test")


def type_validate(file_name: str) -> bool:
    split_name = file_name.split(".")
    file_format = split_name[-1]

    if file_format == "csv":
        return True

    return False
