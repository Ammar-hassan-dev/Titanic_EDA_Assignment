import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# Cabin aur Ticket columns drop kar rahe hain
df = df.drop(columns=['Cabin', 'Ticket'])

print("Columns left in dataset:\n")
print(df.columns)
