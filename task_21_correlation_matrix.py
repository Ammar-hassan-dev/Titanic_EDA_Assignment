import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# Sirf numerical columns ko select karna zaroori hai
numeric_df = df.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numeric_df.corr()
print("Correlation Matrix:\n")
print(correlation_matrix)