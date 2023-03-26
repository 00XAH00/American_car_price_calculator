from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from page_elements.content import table
from page_elements.content.model_type import model_types_row


train_page = html.Div(
    [
        html.H1("Тренировка модели"),
        html.Div(
            children=[
                html.H2("Укажите тип модели для обучения", className="model-type-header"),
                html.A(
                    href="https://scikit-learn.org/stable/supervised_learning.html#supervised-learning",
                    children=html.Span("help", className="material-symbols-outlined", id="models-help"),
                    target="_blank"
                )
            ],
            className="models-help-row"
        ),
        model_types_row,
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    dcc.Textarea(
                        id="hyperparametrs-input",
                        placeholder="{\n\t'max_features': [1, 5, 10, 15]\n\t'alpha': [.1, .2, .3, .4, .5]\n}",
                        style={'width': '100%', 'height': 200}
                    ),
                    title="Гиперпараметры (не обязательно)"
                )
            ],
            start_collapsed=True
        ),
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
        html.P("Загрузите файл в формате csv содержащий следующие столбцы:", className="example_table_text"),
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
    ]
)
