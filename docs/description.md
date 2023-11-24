# spt

Scientific matplotlib plot rcParams configuration template python package.

- Repo: [https://gitee.com/yangsl306/spt](https://gitee.com/yangsl306/spt)
- Full documentation: [README.md](https://gitee.com/yangsl306/spt/README.md)

---

## Installation

- via pip:

```bash
pip install spt
```

- via git:

```bash
pip install git+https://gitee.com/yangsl306/spt.git
```

- via source code:

```bash
git clone https://gitee.com/yangsl306/spt.git
cd spt

pip install .
# or 
pip install -r requirements.txt

# editable mode
pip install -e .
```

---

## Usage

### set_plot_params()

- code:

```python
import matplotlib.pyplot as plt
from spt.plot_params import set_plot_params

...

set_plot_params()

fig, ax = plt.subplots()

...

```

---

### set_roman_plot_params()

- requirements:

To use Times New Roman font, you need to do:

```bash
# copy roman-ttf fonts to your matplotlib font path in specific conda env
cp roman-ttf/* <conda_env>/lib/pythonXXX/site-packages/matplotlib/mpl-data/fonts/ttf/

# remove matplotlib cache
rm -rf ~/.cache/matplotlib
```

---

- code:

```python
import matplotlib.pyplot as plt
from spt.plot_params import set_roman_plot_params

...

set_roman_plot_params()

fig, ax = plt.subplots()

...

```

---

### Chinese characters plot

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

- code:

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
