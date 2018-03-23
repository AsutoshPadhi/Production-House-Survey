import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


df = pd.read_csv("data.csv")

df = df.drop(['Timestamp'], axis=1)

(pd.crosstab(df['Gender'], df['Channels'])).plot(kind='bar',stacked=False,color=['red','blue','green','brown','yellow','lightblue','coral','crimson','cyan','lavender','lime','magenta','maroon','navy','orange'],grid=False).legend(loc=9, bbox_to_anchor=(0.5, -0.1))
plt.show()

print(df)