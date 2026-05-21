import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df_featured = df.copy()

    df_featured['Month'] = df_featured['Review_Date'].dt.month

    df_featured['Negative_Review_Length'] = df_featured['Negative_Review_Clean'].str.len()

    return df_featured