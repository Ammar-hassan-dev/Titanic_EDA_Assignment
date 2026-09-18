import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

sns.countplot(data=df, x='Embarked')
plt.title("Passengers by Embarked Port")
plt.show()