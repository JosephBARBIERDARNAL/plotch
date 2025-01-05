import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotch

np.random.seed(0)

plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300

df = pd.DataFrame(
    {
        "x": [10, 34, 71, 42, 82],
        "y": [1, 2, 3, 4, 5],
        "labels": ["A", "B", "C", "D", "E"],
    }
)

_, ax1 = plt.subplots(figsize=(5, 5))
ax1.scatter(df["x"], df["y"])

_, ax2 = plt.subplots(figsize=(5, 5))
ax2.bar(df["y"], df["x"])

ax1 / ax2
plt.gcf().savefig("img/example-1.png")

ax1 + ax2
plt.gcf().savefig("img/example-2.png")

(ax1 + ax2) / ax2
plt.gcf().savefig("img/example-3.png")
