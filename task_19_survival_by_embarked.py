import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

sns.countplot(data=df, x='Embarked', hue='Survived')
plt.title("Survival by Embarked Port")
plt.show()