import matplotlib.pyplot as plt
import plotch

_, ax1 = plt.subplots()
ax1.set_facecolor("black")
ax1.plot([1, 2, 3], [1, 2, 3])

_, ax2 = plt.subplots()
ax2.scatter([1, 2, 3], [3, 2, 1])

_, ax3 = plt.subplots()
ax3.bar(["Jo", "Mat", "Lo"], [1, 2, 3])


(ax1 + ax2) / ax3

fig = plt.gcf()
fig.set_facecolor("#c8bdbd")

plt.savefig("img/quickstart.png", dpi=300)
