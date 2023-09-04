# spt

scientific matplotlib plot template python module(`plot_params.py`).




---
---

## Usage

### use set_plot_params function

[plot.py](./plot.py)

- plot test script:

```python
import numpy as np
import matplotlib.pyplot as plt
from plot_params import set_plot_params


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

set_plot_params()

fig, ax = plt.subplots()

ax.plot(x, y, label='$y=\sin(x)$')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

fig.savefig('sin.png')

print("figure is generated!")
```

---

- Figure:

![sin.png](./assets/example-figures/sin.png)



---
---

### use set_roman_plot_params function

[plot_roman.py](./plot_roman.py)

- requirements:

To use times new roman font, you need to do:

```bash
# cp roman-ttf fonts to your matplotlib font path in your conda env
cp roman-ttf/* <<conda_env>>/lib/pythonXXX/site-packages/matplotlib/mpl-data/fonts/ttf/

# remove matplotlib cache
rm -rf ~/.cache/matplotlib
```

---

- plot test script:

```python
import matplotlib.pyplot as plt
import numpy as np
from plot_params import set_roman_plot_params


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

set_roman_plot_params()

fig, ax = plt.subplots()

ax.plot(x, y, label="$y=\sin(x)$")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

fig.savefig("sin-roman.png")

print("figure is generated!")
```

---

- Figure:

![sin-roman.png](./assets/example-figures/sin-roman.png)

---

- 3d plot test script:

[plot_3d.py](./plot_3d.py)


```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
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

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.legend()

fig.savefig("scatter-3d.png")

print("Figure is generated!")

```

---

- Figure:

![scatter-3d.png](./assets/example-figures/scatter-3d.png)



---
---

### Chinese font plot

[plot_zh.py](./plot_zh.py)


- requirements:

To use chinese(SimHei 黑体) font, you need to do:

```bash
# cp SimHei-ttf fonts to your matplotlib font path in your conda env
cp chinese-config/chinese-ttf/* <<conda_env>>/lib/pythonXXX/site-packages/matplotlib/mpl-data/fonts/ttf/

# you need to backup matplotlibrc file first
cp chinese-config/matplotlibrc <<conda_env>>/lib/pythonXXX/site-packages/matplotlib/mpl-data/

# remove matplotlib cache
rm -rf ~/.cache/matplotlib
```

`matplotlibrc` modification:
```bash
# origin 
#font.family:  sans-serif

#font.sans-serif: DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif

#axes.unicode_minus: True  # use Unicode for the minus symbol rather than hyphen.  See

---

# modification
font.family:  sans-serif

font.sans-serif: DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif, SimHei, Times New Roman, Times

axes.unicode_minus: False  # use Unicode for the minus symbol rather than hyphen.  See
```


- plot test script:

```python
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
ax.legend(prop={'family': 'SimHei'})


fig.savefig("sin-zh.png")

print("figure is generated!")
```

---

- Figure

![sin-zh.png](./assets/example-figures/sin-zh.png)



---
---

## Examples

- Figure 1:

![subs-ene-Nb3Si-bar.png](./assets/subs-ene-Nb3Si-bar.png)

---

- Figure 2:

![b_fit_cal.png](./assets/b_fit_cal.png)
