import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from spt.plot_params import set_plot_params, set_roman_plot_params

fit_b_data = pd.read_csv("fit_b.dat", header=None)
cal_b_data = pd.read_csv("cal_b.dat", header=None)
# change all fit_b_data to 1 dimension
fit_b_data_1d = fit_b_data.values.reshape(-1)
cal_b_data_1d = cal_b_data.values.reshape(-1)


score_rmse = np.round(np.sqrt(mean_squared_error(cal_b_data_1d, fit_b_data_1d)), 2)
score_r2 = np.round(np.sqrt(r2_score(cal_b_data_1d, fit_b_data_1d)), 2)
print(f"RMSE: {score_rmse}.")
print(f"R2: {score_r2}.")


set_roman_plot_params(
    legend_frameon=False,
    legend_handletextpad=0.1,
)

figsize = 6
fig, ax = plt.subplots(figsize=(figsize, figsize))

temperatue_list = [f"{str(num)}00K" for num in range(1, 10, 2)]
marker_list = ["X", "s", "o", "^", "p"]

max_val = 8.5
ax.plot([0.0, max_val], [0.0, max_val], linestyle="--", color="black")
for i in range(fit_b_data.shape[0]):
    ax.plot(
        cal_b_data.iloc[i, :],
        fit_b_data.iloc[i, :],
        marker=marker_list[i],
        linestyle="",
        label=temperatue_list[i],
    )

ax.set(
    xlim=(0.0, max_val),
    ylim=(0.0, max_val),
    xticks=range(0, 9, 1),
    yticks=range(0, 9, 1),
    xlabel=r"Calculated B$\,·\,10^{-5}$ (Pa$\,·\,$s)",
    ylabel=r"Predicted B$\,·\,10^{-5}$ (Pa$\,·\,$s)",
)

# f-string 对于在图中添加需要 LaTeX 格式的 text 效果不是很好，改用 str.replace()
ax.text(3.0, 1.5, r"RMSE=cha$\,·\,10^{-5}$ Pa$\,·\,$s".replace("cha", str(score_rmse)))

ax.legend()

fig.savefig("b_fit_cal.png")

print("\nFigure is generated!")
