import dash_bootstrap_components as dbc
from dash_extensions.enrich import html, dcc
from page_elements.content import table


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
        html.Div(
            id='output-image-upload',
            children=table.generate_table()
        ),
        html.Div(
            id='div-train-btn',
            children=dbc.Button(
                id="train-btn",
                children="Тренировать",
            )
        )
    ],
    className="user-result"
)
