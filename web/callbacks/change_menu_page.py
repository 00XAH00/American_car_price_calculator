import dash

from app import app
from dash.exceptions import PreventUpdate
from page_elements.side_menu.buttons import buttons
from dash_extensions.enrich import Input, Output, ctx
from pages.calc_price import calc_price
from pages.model_trained_data import model_trained_data
from pages.train_page import train_page


@app.callback(
    [
        Output('button-column', 'children'),
        Output('user-content-block', 'children'),
        Output('cr', 'children')
    ],
    Input('model-train-btn', 'n_clicks'),
    Input('model-data-btn', 'n_clicks'), Input('model-math-btn', 'n_clicks')
)
def btn_callback(btn_one, btn_two, btn_three):
    if ctx.triggered_id is None:
        raise PreventUpdate

    match ctx.triggered_id:
        case 'model-train-btn':
            return [buttons(ctx.triggered_id), train_page, 'train']
        case 'model-data-btn':
            return [buttons(ctx.triggered_id), model_trained_data(), dash.no_update]
        case 'model-math-btn':
            return [buttons(ctx.triggered_id), calc_price, 'calc']
