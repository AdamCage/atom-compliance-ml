from pathlib import Path
from typing import Any, Dict
import joblib

import yaml


def load_yaml(path: Path) -> Dict[str, Any]:
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


def pickle_to_obj(path: Path) -> Any:
    """_summary_

    Args:
        path (Path): _description_

    Returns:
        Any: _description_
    """

    with open(path, "rb") as file:
        return joblib.load(file)


def create_model_name(model_obj: Any) -> str:
    return f'{model_obj.__repr__().replace(r"()", "").lower()}.pickle'
