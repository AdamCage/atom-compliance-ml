from pathlib import Path
from typing import Any
import joblib
from datetime import datetime

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    """_summary_

    Args:
        path (Path): _description_

    Returns:
        dict[str, Any]: _description_
    """

    with open(path, "r") as file:
        return yaml.safe_load(file)

def obj_to_pickle(obj: Any, path: Path) -> None:
    """Сохраняет объект в файл с помощью joblib.

    Args:
        obj (Any): Объект, который нужно сохранить.
        path (Path): Путь к файлу, в который будет сохранен объект.
    """
    with open(path, "wb") as file:
        joblib.dump(obj, file)


def create_model_name(model_obj: Any) -> str:
    return f'{model_obj.__repr__().replace(r"()", "").lower()}_{datetime.today().strftime("%Y-%m-%d")}.pickle'
