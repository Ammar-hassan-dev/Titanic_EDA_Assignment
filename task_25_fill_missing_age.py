import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# Missing age ko average age se fill kar rahe hain
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("Missing values in Age column after filling:", df['Age'].isnull().sum())