from pathlib import Path
from typing import Any

from pathlib import Path
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

