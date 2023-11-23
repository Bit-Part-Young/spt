import matplotlib.pyplot as plt
import numpy as np
from spt.plot_params import set_roman_plot_params

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

set_roman_plot_params()

fig, ax = plt.subplots()

ax.plot(x, y, label="$y=\sin(x)$")

ax.set(xlabel="x", ylabel="y")
ax.legend()

fig.savefig("sin_roman.png")

print("\nFigure is generated!")
