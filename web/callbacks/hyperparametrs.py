from ast import literal_eval
from dash import Output, Input
from app import app


@app.callback(Output('hyperparametrs-input', 'style'),
              Input('hyperparametrs-input', 'value'))
def hyperparametrs_validate(value):
    style = {
        'width': '100%',
        'height': 200
    }

    if (value == '') or (value is None):
        style.update({'borderColor': 'black'})
        return style

    try:
        literal_eval(value)
        print(value)
        style.update({'borderColor': 'green'})
    except (SyntaxError, ValueError):
        style.update({'borderColor': 'red'})

    return style
