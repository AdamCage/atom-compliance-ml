from pathlib import Path

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def plot_compliance_distribution(report: pd.DataFrame, save_as_png: bool, path: Path):
    compliance_counts = report["Complience Level"].value_counts().reset_index()
    compliance_counts.columns = ["Compliance Level", "Count"]

    plt.figure(figsize=(8, 6))
    sns.barplot(data=compliance_counts, x="Compliance Level", y="Count", palette="viridis")

    plt.title("Распределение комплаенс-меток")
    plt.xlabel("Compliance Level")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

    if save_as_png:
        plt.savefig(path / "compliance_distribution.png")
