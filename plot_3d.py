import matplotlib.pyplot as plt
import numpy as np
from plot_params import set_roman_plot_params


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

# plt.subplots_adjust(left=0.1, right=1.0, bottom=0.1, top=0.9)

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
# TODO: z轴的label无法正常显示 待解决
ax.set_zlabel("Z axis")
ax.legend()

fig.savefig("scatter-3d.png")

print("Figure is generated!")
