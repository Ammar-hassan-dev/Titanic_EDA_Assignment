import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

# kde=True line bhi draw karega graph ke upar
sns.histplot(data=df, x='Age', kde=True, bins=30)
plt.title("Age Distribution of Passengers")
plt.show()