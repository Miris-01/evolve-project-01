from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import limpiar_datos_hoteles
from src.features import build_features
from src.utils import assert_columns
from src.viz import plot_graph


def main():
    df = load_csv(RAW_PATH)
    df = limpiar_datos_hoteles(df)
    df = build_features(df) #no sé qué pasa
    # assert_columns(df, ['column_1', 'column_2'])

    plot_graph(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":            
    main()
