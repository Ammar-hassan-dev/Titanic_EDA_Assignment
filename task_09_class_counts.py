import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

class_counts = df['Pclass'].value_counts()
print("Number of passengers in each class:\n")
print(class_counts)