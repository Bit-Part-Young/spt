import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from spt.plot_params import set_plot_params, set_roman_plot_params

set_roman_plot_params()

fig, ax = plt.subplots()

subs_ene_fn = "subs_ene_Nb3Si.csv"
subs_ene_df = pd.read_csv(subs_ene_fn, sep=" ")

equi_site_list = ["Nb_I", "Nb_II", "Nb_III", "Si_I"]
label_list = ["Nb_{I}", "Nb_{II}", "Nb_{III}", "Si_{I}"]

bar_width = 0.4
bar_gap = 0.2


def phase_stability_plot():
    solute_list = subs_ene_df.loc[
        subs_ene_df["solute_site"] == "Nb_I", "solute"
    ].tolist()
    x_data = np.arange(len(solute_list)) * 2

    for index, equi_site in enumerate(equi_site_list):
        y_data = subs_ene_df.loc[subs_ene_df["solute_site"] == equi_site, "subs_energy"]
        ax.bar(
            x_data + bar_width * (index - 2) + bar_gap,
            y_data,
            width=bar_width,
            label=f"$\mathrm{{{label_list[index]}}}$",
        )

    ax.axhline(0.0, linestyle="--", c="k")
    ax.set_xticks(x_data, solute_list)

    ax.set(
        ylim=(-0.5, 5.0),
        xlabel="Alloying Elements",
        ylabel="$\mathrm{E_{SS}}$ (eV)",
    )

    ax.legend(ncols=2, loc="upper left")

    figname = "substition_energy_Nb3Si.png"
    fig.savefig(figname)

    print("\nFigure is generated.")


if __name__ == "__main__":
    phase_stability_plot()
