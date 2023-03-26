from dash import html, dcc
import dash_bootstrap_components as dbc
from page_elements.content import table


calc_price = html.Div(
    [
        html.H1("Рассчитать стоимость"),
        html.P("Загрузите файл в формате csv содержащий следующие столбцы:", className="example_table_text"),
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
            className='upload-href'
        ),
        html.Div(
            id='output-image-upload',
            children=table.generate_table(with_price=False)
        ),
        html.Div(
            id='div-calc-btn',
            children=dbc.Button(
                id="calc-btn",
                children="Рассчитать",
            )
        ),

    ]
)
