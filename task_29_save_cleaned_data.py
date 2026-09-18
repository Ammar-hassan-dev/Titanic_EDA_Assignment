import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# Missing values fill aur naya column add kar ke save kar rahe hain
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

df.to_csv("Titanic_Cleaned_Dataset.csv", index=False)
print("Cleaned dataset saved successfully!")