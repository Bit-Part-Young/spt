# spt
scientific matplotlib plot template python module.

## Usage
plot test script:
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
```

## Figure:

![](./sin.png)
