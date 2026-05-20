import pandas as pd


#def clean(df: pd.DataFrame) -> pd.DataFrame:
 #   pass


def delete_duplicates(df):
    df = df.drop_duplicates()

    return df

def clean_dates(df, column_name) :
    if column_name in df.columns:
        df[column_name] = pd.to_datetime(df[column_name])
    
    return df


