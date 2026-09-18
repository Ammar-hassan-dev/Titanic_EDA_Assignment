import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

class_group = df.groupby('Pclass')[['Survived', 'Age', 'Fare']].mean()

print("Average Survival, Age, and Fare by Passenger Class:\n")
print(class_group)