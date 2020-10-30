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
dfp = df[["weekday", "total_items"]]
# %%
sdd=[]
ks = range(1,14)
for k in range(1,14):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    sdd.append(km.inertia_)
kneedle = KneeLocator(ks, sdd,S=1.0,curve="convex",direction="decreasing")
kneedle.plot_knee()
plt.show()
k= round(kneedle.knee)

# %%
#for i in range(k):
    #print("\nCLUSTER ",i)
cluster0 = df[kmeans.labels_ == 0]
cluster0.describe()

# %%
cluster1 = df[kmeans.labels_ == 1]
cluster1.describe()
# %%
cluster2 = df[kmeans.labels_ == 2]
cluster2.describe()
# %%
cluster3 = df[kmeans.labels_ == 3]
cluster3.describe()
# %%
dfpi = df[["weekday", "Pets%"]]
kmeans = KMeans(n_clusters=k).fit(dfpi)
sns.scatterplot(data=df, x="weekday", y="Pets%", hue=kmeans.labels_)
plt.show()
"""
sns.heatmap(df.corr(),annot=True)
items = df[df["total_items"] < 29]
sns.boxplot(data=items,x="weekday",y="total_items")
"""
# %%
