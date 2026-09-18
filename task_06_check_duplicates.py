import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

duplicates = df.duplicated().sum()
print("Number of duplicate rows:", duplicates)