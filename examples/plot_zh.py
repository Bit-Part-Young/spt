import matplotlib.pyplot as plt
import numpy as np
from plot_params import set_roman_plot_params

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

set_roman_plot_params()

fig, ax = plt.subplots()

ax.plot(x, y, label="正弦函数")
# ax.plot(x, y, label="$y=\sin(x)$")

ax.set_xlabel("x")
ax.set_ylabel("y")
# x y轴标签 字体设置为SimHei
# ax.set_xlabel("x 轴", fontproperties="SimHei")
# ax.set_ylabel("y 轴", fontproperties="SimHei")

# legend 设置simhei字体
ax.legend(prop={"family": "SimHei"})


fig.savefig("sin_zh.png")

print("figure is generated!")
