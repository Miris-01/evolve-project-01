import os
from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean_data
from src.features import build_features
from src.utils import assert_columns
from src.viz import (plot_most_demanding_nationality,
                    plot_top_complaints_emiratis,
                    plot_monthly_trend,
                    plot_summer_trend,
                    plot_leng_complaint,
                    plot_mean_nationalities)



def main():

    file_path = 'data/raw/Hotel_Reviews.csv'

    possible_paths = [
        file_path,
        'Hotel_Reviews.csv',
        'data/Hotel_Reviews.csv',
        '../data/raw/Hotel_Reviews.csv',
        './data/raw/Hotel_Reviews.csv',
    ]

    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}. "
            "Please verify the dataset location or move the CSV to one of the expected paths."
        )
    

    print('Loading dataset...')
    df = load_csv(file_path)
    print('Cleaning data...')
    df_clean = clean_data(df)
    print('Features...')
    df_final = build_features(df_clean)
    
    #assert_columns(df_final)

    print('**************************************DATA VISUALIZE****************************************')
    plot_most_demanding_nationality(df_final)
    plot_top_complaints_emiratis (df_final)
    plot_monthly_trend (df_final)
    plot_summer_trend (df_final)
    plot_leng_complaint (df_final)
    plot_mean_nationalities (df_final)



if __name__ == "__main__":            
    main()
