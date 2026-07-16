from src.data_loader import load_data

df = load_data()

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns)
print(df.columns.to_list())