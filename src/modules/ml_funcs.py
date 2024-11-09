def atom_score(mse: float) -> float:
    return max(0, 1.5 - mse) / 1.5
