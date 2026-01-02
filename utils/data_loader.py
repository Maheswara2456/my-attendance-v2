import pandas as pd

CSV_PATH = "data/attendance.csv"

def load_data():
    df = pd.read_csv(CSV_PATH, dtype=str).fillna("")
    if "DATE" not in df.columns:
        df.insert(0, "DATE", "")
    return df

def save_data(df):
    df.to_csv(CSV_PATH, index=False)
