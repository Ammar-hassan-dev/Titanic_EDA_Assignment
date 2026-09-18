import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

sns.histplot(data=df, x='Fare', bins=40)
plt.title("Fare Distribution")
plt.show()