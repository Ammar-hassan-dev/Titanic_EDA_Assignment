import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# Sirf numerical columns ke sath groupby taake error na aaye
gender_group = df.groupby('Sex')[['Survived', 'Age', 'Fare']].mean()

print("Average Survival, Age, and Fare by Gender:\n")
print(gender_group)