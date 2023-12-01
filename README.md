[![PyPi](https://img.shields.io/pypi/v/spt?logo=pypi&logoColor=white&label=PyPI)](https://pypi.org/project/spt/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/spt?logo=pypi&logoColor=white&color=blue&label=PyPI%20downloads)](https://pypi.org/project/spt)
[![Requires Python 3.6+](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)](https://python.org/downloads)

# spt

Scientific matplotlib plot rcParams configuration template python package.

- **Repo**: [https://github.com/Bit-Part-Young/spt](https://github.com/Bit-Part-Young/spt)
- **Full documentation**: [README.md](https://github.com/Bit-Part-Young/spt)

---

## Installation

- via pip:

```bash
pip install spt

# update
pip install -U spt

# install spt and examples dependencies
pip install ".[examples]"
```

- via git:

```bash
pip install git+https://gitee.com/yangsl306/spt.git
# or
pip install git+https://github.com/Bit-Part-Young/spt.git
```

- via source code:

```bash
git clone https://gitee.com/yangsl306/spt.git
# or
git clone https://github.com/Bit-Part-Young/spt.git

cd spt

pip install .
# or 
pip install -r requirements.txt

# editable mode
pip install -e .
```

---

## Usage

Full example codes can be found in [examples](https://github.com/Bit-Part-Young/spt/tree/master/examples) folder.

---

### set_plot_params()

<!-- script: [plot.py](./examples/plot.py) -->
script: [plot.py](https://github.com/Bit-Part-Young/spt/blob/master/examples/plot.py)

- plot:

```python
import matplotlib.pyplot as plt
from spt.plot_params import set_plot_params

...

set_plot_params()

fig, ax = plt.subplots()

...

```

---

- Figure:

<!-- ![sin.png](./assets/sin.png) -->
<img src="https://raw.githubusercontent.com/Bit-Part-Young/spt/master/assets/sin.png" alt="sin.png" />

---

### set_roman_plot_params()

<!-- script: [plot_roman.py](./examples/plot_roman.py) -->
script: [plot_roman.py](https://github.com/Bit-Part-Young/spt/blob/master/examples/plot_roman.py)

- requirements:

To use Times New Roman font, you need to do:

```bash
# copy roman-ttf fonts to your matplotlib font path in specific conda env
cp roman-ttf/* <conda_env>/lib/pythonXXX/site-packages/matplotlib/mpl-data/fonts/ttf/

# remove matplotlib cache
rm -rf ~/.cache/matplotlib
```

---

- plot:

```python
import matplotlib.pyplot as plt
from spt.plot_params import set_roman_plot_params

...

set_roman_plot_params()

fig, ax = plt.subplots()

...

```

---

- Figure:

<!-- ![sin_roman.png](./assets/sin_roman.png) -->
<img src="https://raw.githubusercontent.com/Bit-Part-Young/spt/master/assets/sin_roman.png" alt="sin_roman.png" />

---

- 3d plot:

<!-- script: [plot_3d.py](./examples/plot_3d.py) -->
script: [plot_3d.py](https://github.com/Bit-Part-Young/spt/blob/master/examples/plot_3d.py)

```python
import matplotlib.pyplot as plt
from spt.plot_params import set_roman_plot_params

...

set_roman_plot_params(
    axes_labelpad=15,
    legend_handletextpad=0.0,
    legend_fontsize=22,
    savefig_bbox="standard",
)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(10, 8))

...

```

---

- Figure:

<!-- ![scatter_3d.png](./assets/scatter_3d.png) -->
<img src="https://raw.githubusercontent.com/Bit-Part-Young/spt/master/assets/scatter_3d.png" alt="scatter_3d.png" />

---

### Chinese characters plot

<!-- script: [plot_zh.py](./examples/plot_zh.py) -->
script: [plot_zh.py](https://github.com/Bit-Part-Young/spt/blob/master/examples/plot_zh.py)

- requirements:

To use Chinese(SimHei 黑体) font, you need to do:

```bash
# copy SimHei-ttf fonts to matplotlib font path in specific conda env
cp chinese-config/chinese-ttf/* <conda_env>/lib/pythonXXX/site-packages/matplotlib/mpl-data/fonts/ttf/

# backup matplotlibrc file
cd <conda_env>/lib/pythonXXX/site-packages/matplotlib/mpl-data/
cp matplotlibrc matplotlibrc_origin
cd -

# copy modified matplotlibrc file
cp chinese-config/matplotlibrc <conda_env>/lib/pythonXXX/site-packages/matplotlib/mpl-data/

# remove matplotlib cache
rm -rf ~/.cache/matplotlib
```

---

`matplotlibrc` modification:

```bash
# origin 
font.family:  sans-serif
font.sans-serif: DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
axes.unicode_minus: True  # use Unicode for the minus symbol rather than hyphen.  See

# modification
font.family:  sans-serif
font.sans-serif: DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif, SimHei, Times New Roman, Times
axes.unicode_minus: False  # use Unicode for the minus symbol rather than hyphen.  See
```

---

- plot:

```python
import matplotlib.pyplot as plt
from spt.plot_params import set_roman_plot_params

...

set_roman_plot_params()

fig, ax = plt.subplots()

ax.plot(x, y, label="正弦函数")

ax.set(xlabel="x", ylabel="y")

# legend 字体设置为 SimHei
ax.legend(prop={"family": "SimHei"})

...

```

---

- Figure

<!-- ![sin_zh.png](./assets/sin_zh.png) -->
<img src="https://raw.githubusercontent.com/Bit-Part-Young/spt/master/assets/sin_zh.png" alt="sin_zh.png" />

---

## Scientific Figure Examples

- Example 1:

<!-- script: [phase_stability_Nb3Si_plot.py](./examples/phase-stability-Nb3Si-plot/phase_stability_Nb3Si_plot.py) -->
script: [phase_stability_Nb3Si_plot.py](https://github.com/Bit-Part-Young/spt/blob/master/examples/phase-stability-Nb3Si-plot/phase_stability_Nb3Si_plot.py)

Figure:

<!-- ![substitution_energy_Nb3Si.png](./assets/substitution_energy_Nb3Si.png) -->
<img src="https://raw.githubusercontent.com/Bit-Part-Young/spt/master/assets/substitution_energy_Nb3Si.png" alt="substitution_energy_Nb3Si.png" />

---

- Example 2:

<!-- script: [b_fit_cal.py](./examples/fit-cal-b-plot/b_fit_cal.py) -->
script: [b_fit_cal.py](https://github.com/Bit-Part-Young/spt/blob/master/examples/fit-cal-b-plot/b_fit_cal.py)

Figure:

<!-- ![b_fit_cal.png](./assets/b_fit_cal.png) -->
<img src="https://raw.githubusercontent.com/Bit-Part-Young/spt/master/assets/b_fit_cal.png" alt="b_fit_cal.png" />

---

## To do

- [x] 完善 `setup.py` 安装脚本
- [x] 3D 图绘制 z 轴标签显示不全（`"savefig.bbox"` 参数设为 `"tight"` 时，会出现这种情况，需设为 `"standard"`，多余空白需自己后处理掉；**jupyter notebook 中 z 轴标签仍显示不全**）
- [x] 安装 spt package 后，使用 `fig, ax = plt.subplots()` 命令，VSCode 的 Pylance 插件无法自动识别 `ax` 对象的属性和方法（matplotlib 3.8 版本的问题，需将 matplotlib 版本降到 3.8 以下）
