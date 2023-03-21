import dash_bootstrap_components as dbc
from dash import dash_table
from dash_extensions.enrich import html, dcc
from services.data import Data


data = Data()
example_table = data.get_example_table()

content = dbc.Col(
    [
        html.H1("Тренировка модели"),
        html.A(
            dcc.Upload(
                id='upload-image',
                children=html.Div([
                    'Drag and Drop or select Files'
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px',
                    'color': 'white'
                },
                # Allow multiple files to be uploaded
                multiple=False
            ),
            href='#',
            # href='javascript: void(0)',
            className='upload-href'
        ),
        html.P("Загрузите файл в формате csv содержащий следующие столбцы:"),
        dash_table.DataTable(
            data=example_table.to_dict('records'),
            columns=[{"name": i, "id": i} for i in example_table.columns],
            style_data={
                'backgroundColor': '#31302f',
                'color': 'white'
            },
            page_size=50
        ),
        html.Div(id='output-image-upload'),
    ],
    className="user-result"
)
