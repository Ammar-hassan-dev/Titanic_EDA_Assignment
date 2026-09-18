import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# 1 isliye plus kiya kyunke passenger khud bhi family ka hissa hai
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

print(df[['SibSp', 'Parch', 'FamilySize']].head())