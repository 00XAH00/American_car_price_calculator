import dash_bootstrap_components as dbc


model_types_row = dbc.RadioItems(
    id="radios",
    className="btn-group",
    inputClassName="btn-check",
    labelClassName="btn btn-outline-primary",
    labelCheckedClassName="active",
    options=[
        {"label": "Линейная регрессия без регуляризаторов", "value": 1},
        {"label": "Линейная регрессия с регуляризацией (Ridge)", "value": 2},
        {"label": "Линейная регрессия с регуляризацией (Lasso)", "value": 3},
        {"label": "Деревья принятия решений", "value": 4},
        {"label": "Ансамблевые модели", "value": 5},
        {"label": "K ближайших соседей", "value": 6},
        {"label": "Логистическая регрессия", "value": 7},
        {"label": "Деревья принятия решений и ансамбли", "value": 8},
    ],
    value=1,
)
