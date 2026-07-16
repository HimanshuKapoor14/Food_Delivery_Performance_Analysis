import pandas as pd

def load_data():
    file_path = "dataset/food_delivery.csv"
    df = pd.read_csv(file_path)
    return df