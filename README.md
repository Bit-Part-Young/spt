# spt

scientific matplotlib plot template python module(`plot_params.py` and `plot_params_roman.py`).


**Note: the module can't render chinese characters!!!**


---
---


## Usage

### use plot_params.py

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

![sin.png](./sin.png)


---


### use plot_params_roman.py

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
from plot_params_roman import set_plot_params


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

set_plot_params()

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

![sin-roman.png](./sin-roman.png)