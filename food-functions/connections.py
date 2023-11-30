import pandas as pd

def get_foods_kcal_df() :
    return pd.read_csv('./db/foods-kcal.csv', encoding="UTF-8")