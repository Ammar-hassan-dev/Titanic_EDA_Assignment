import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print("Summary statistics of numerical columns:\n")
print(df.describe())