import matplotlib.pyplot as plt
import numpy as np
from spt.plot_params import set_roman_plot_params

set_roman_plot_params(
    axes_labelpad=15,
    legend_fontsize=22,
    legend_handletextpad=0.0,
)

np.random.seed(42)
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(15, 8))

ax.scatter(x, y, z, c="b", marker="o", label=r"$a \, · \, b  \, · \, 10^{-5}$")

ax.set(xlabel="X axis", ylabel="Y axis", zlabel="Z axis")
ax.legend()

fig.savefig("scatter_3d.png")

print("\nFigure is generated!")
