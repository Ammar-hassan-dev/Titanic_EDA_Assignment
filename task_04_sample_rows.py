import pandas as pd

# Dataset load kar rahe hain
df = pd.read_csv("Titanic-Dataset.csv")

# Random 10 rows print kar rahe hain
print("Showing 10 random rows from the dataset:\n")
print(df.sample(10))