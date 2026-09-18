import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

categorical_columns = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
unique_counts = df[categorical_columns].nunique()

print("Number of unique values in categorical columns:\n")
print(unique_counts)