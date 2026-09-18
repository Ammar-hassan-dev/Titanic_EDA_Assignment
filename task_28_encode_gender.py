import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# Sex column ko numbers mein convert kar rahe hain
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

print(df[['Name', 'Sex']].head())