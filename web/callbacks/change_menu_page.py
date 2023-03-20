from app import app
from dash.exceptions import PreventUpdate
from page_elements.side_menu.buttons import buttons
from dash_extensions.enrich import Input, Output, ctx


@app.callback(
    Output(component_id='button-column', component_property='children'), Input('model-train-btn', 'n_clicks'),
    Input('model-data-btn', 'n_clicks'), Input('model-math-btn')
)
def btn_callback(btn_one, btn_two):
    if ctx.triggered_id is None:
        raise PreventUpdate
    else:
        return buttons(ctx.triggered_id)
