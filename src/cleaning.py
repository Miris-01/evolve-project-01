import pandas as pd


#def clean(df: pd.DataFrame) -> pd.DataFrame:
 #   pass

def limpiar_datos_hoteles(df) :
    #eliminamos registros duplicados
    df = df.drop_duplicates()
    #sustituimos 'Negative_Review'
    return df


