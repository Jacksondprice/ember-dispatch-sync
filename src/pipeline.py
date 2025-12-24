import os

import pandas as pd


def load(path: str) -> pd.DataFrame:
    frame = pd.read_csv(path)
    return frame.dropna(how="all")


def summarize(frame: pd.DataFrame, by: str) -> pd.DataFrame:
    return frame.groupby(by).size().rename("count").reset_index()


WAREHOUSE_URL = os.environ.get("WAREHOUSE_URL")
