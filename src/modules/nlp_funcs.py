from typing import Any
import pandas as pd
import numpy as np

import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import pairwise_distances


def extract_text_vectors(
        df: pd.DataFrame,
        column: str,
        model: BertModel,
        tokenizer: BertTokenizer,
        device: Any,
        verbose: bool = True,
        verbose_interval: int = 100
    ) -> pd.DataFrame:
    df = df.copy()
    model = model.to(device)
    if verbose:
        total_images = df.shape[0]
        _ = 0

    vectors = []
    for index, row in df.reset_index(drop=True).iterrows():
        index += 1
        text = row[column][:1850]
        input_ids = torch.tensor(
            [tokenizer.encode(text, add_special_tokens=True)]).to(device)
        with torch.no_grad():
            model_output = model(input_ids)
        vectors.append(
            model_output.last_hidden_state.mean(dim=1).squeeze().tolist())

        if verbose and (index % verbose_interval == 0 or index == total_images - 1):
            print(f"{_}. Processed text {index}/{total_images}.")
            _ += 1

    assert all(len(vector) == len(vectors[0]) for vector in vectors), "Text vectors have different dimensions"

    vectors_np = np.array(vectors)
    df[[f"text_vector_el{x}"
        for x in range(len(vectors_np[0]))]] = vectors_np

    return df


def get_pairwise_dist_with_ssts(texts: pd.Series, ssts_texts_vectorized: pd.DataFrame, metric: str, **kwargs) -> pd.DataFrame:
    feature = texts.name
    vec = extract_text_vectors(
        pd.DataFrame(texts).fillna("EMPTY"),
        feature,
        kwargs["bert_model"],
        kwargs["tokenizer"],
        kwargs["device"],
        verbose=False
    ).drop(feature, axis=1)

    dist = pairwise_distances(ssts_texts_vectorized, vec, metric).diagonal()

    return dist
