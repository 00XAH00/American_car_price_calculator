from dash_extensions.enrich import html
from dash_extensions.enrich import Input, Output, State, DashLogger
from app import app


@app.callback(Output('output-image-upload', 'children'), Input('upload-image', 'contents'),
              State('upload-image', 'filename'), State('upload-image', 'last_modified'), log=True)
def update_output(list_of_contents, list_of_names, list_of_dates, dash_logger: DashLogger):
    if list_of_contents is not None:
        print(list_of_contents)
        print(list_of_names)
        print(list_of_dates)
        dash_logger.info("test :)", autoClose=5000)
        # children = [
        #     parse_contents(list_of_contents, list_of_names, list_of_dates)
        # ]
        # print(children)
        return html.Div("test")
