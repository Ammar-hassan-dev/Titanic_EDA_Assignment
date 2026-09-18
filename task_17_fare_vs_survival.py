import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

sns.boxplot(data=df, x='Survived', y='Fare')
plt.title("Fare vs Survival")
plt.show()