from pathlib import Path

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike


def plot_ground_truth_vs_predictions(target: pd.Series, preds: ArrayLike, save_as_png: bool, path: Path):
    df = pd.DataFrame({'target': target, 'preds': preds})

    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, palette="tab10", markers=True)
    plt.title('Ground Truth vs Predictions')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.xticks(ticks=range(len(df)), labels=range(len(df)))
    plt.legend(['Ground Truth', 'Predictions'])
    plt.grid()

    if save_as_png:
        plt.savefig(path / "ground_truth_vs_predictions.png")

    plt.show()


def plot_coefficients(coefficients: ArrayLike, feature_names: list[str], save_as_png: bool, path: Path):
    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 5))
    sns.barplot(x=feature_names, y=coefficients, palette="viridis")
    plt.title('Coefficients of the Regression Model')
    plt.xlabel('Features')
    plt.ylabel('Coefficient Value')
    plt.grid()

    if save_as_png:
        plt.savefig(path / "coefficients.png")

    plt.show()


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

    if save_as_png:
        plt.savefig(path / "compliance_distribution.png")

    plt.show()
