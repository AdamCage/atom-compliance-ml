import pandas as pd
from numpy.typing import ArrayLike


def get_kickouts_indexes(ds: pd.DataFrame) -> ArrayLike:
    indexes = (ds["full_uc_text"].isna() | ds["full_ssts_text"].isna())

    return (indexes.index[indexes])


def atom_score(mse: float) -> float:
    return max(0, 1.5 - mse) / 1.5
