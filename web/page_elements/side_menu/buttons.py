from typing import List
import dash_bootstrap_components as dbc


def buttons(active_button: str) -> List[dbc.Button]:
    buttons_list = []
    buttons_dict = [
        {
            "name": "Тренировка модели",
            "id": "model-train-btn"
        },
        {
            "name": "Данные модели",
            "id": "model-data-btn"
        },
        {
            "name": "Расчет стоимости АТ",
            "id": "model-math-btn"
        }
    ]
    for button in buttons_dict:
        active = "secondary"
        if button["id"] == active_button:
            active = "primary"

        buttons_list.append(
            dbc.Button(
                button["name"],
                color=active,
                className="menu-button",
                id=button["id"]
            )
        )

    return buttons_list
