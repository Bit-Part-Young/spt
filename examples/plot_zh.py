import matplotlib.pyplot as plt
import numpy as np
from spt.plot_params import set_roman_plot_params

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

set_roman_plot_params()

fig, ax = plt.subplots()

ax.plot(x, y, label="正弦函数")

# x y 轴标签 字体设置为 SimHei
ax.set_xlabel("x")
ax.set_ylabel("y")

# legend 字体设置 SimHei
ax.legend(prop={"family": "SimHei"})

fig.savefig("sin_zh.png")

print("figure is generated!")
