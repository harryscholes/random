import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress, mannwhitneyu
sns.set(style='ticks')

df = pd.read_csv("peak_flow.csv")

date_fields = ["hour", "day", "month", "year"]
dates = pd.to_datetime(df[date_fields])
df.index = dates
df = df.drop(date_fields, axis=1)

pre = ["pre1", "pre2", "pre3"]
post = ["post1", "post2", "post3"]

fig, ax = plt.subplots(1, figsize=(8,3))
ax.plot(df[post].mean(axis=1), label="post-medication")
#plt.show()
#xlabel_ax = ax
#locs, labs = plt.xticks()
#[i.get_text() for i in ax]
print([i.get_text() for i in ax.get_xticklabels()])
#[i.get_text() for i in ax.get_xticklabels()]
