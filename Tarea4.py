# %%
import math
import csv
import random
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator

df = pd.read_csv('ulabox.csv')
del df['order']

# %%
dfp = df[["weekday", "total_items"]]
kmeans = KMeans(n_clusters=3).fit(df[["weekday", "total_items"]])
sns.scatterplot(data=df, x="weekday", y="total_items", hue=kmeans.labels_)
plt.show()
"""
sns.heatmap(df.corr(),annot=True)
items = df[df["total_items"] < 29]
sns.boxplot(data=items,x="weekday",y="total_items")
"""