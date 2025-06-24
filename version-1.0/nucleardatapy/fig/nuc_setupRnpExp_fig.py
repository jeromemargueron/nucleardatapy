import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

import nucleardatapy as nuda

SOURCE_LABELS_LATEX = {
    "48Ca": r"$^{48}\mathrm{Ca}$",
    "208Pb": r"$^{208}\mathrm{Pb}$"
}

def nuc_setupRnpExp_fig(pname=None, source=None):
    print(f"Using source: {source}")
    
    # subplot_label = "(a)"
    subplot_label = " "

    if source is None:
        print("Erro: nenhum source fornecido.")
        return

    labels = []
    rskin_values = []
    error_lower = []
    error_upper = []
    markers = []

    cals = nuda.nuc.rnp_exp_source(source)

    for cal in cals:
        neutron_skin_calc = nuda.nuc.setupRnpExp(source=source, cal=cal)

        if neutron_skin_calc.rnp is not None:
            labels.append(neutron_skin_calc.label)
            rskin_values.append(neutron_skin_calc.rnp)

            err_down = neutron_skin_calc.rnp_sig_lo if neutron_skin_calc.rnp_sig_lo is not None else 0.0
            err_up = neutron_skin_calc.rnp_sig_up if neutron_skin_calc.rnp_sig_up is not None else 0.0
            error_lower.append(err_down)
            error_upper.append(err_up)

            marker = getattr(neutron_skin_calc, "marker", 'o')
            markers.append(marker)

    if not rskin_values:
        print(f"Nenhum dado disponível para {source}.")
        return

    fig, ax = plt.subplots(figsize=(10, 8))
    x_positions = range(len(labels) + 1)

    for i, (x, y, err_down, err_up, marker) in enumerate(zip(x_positions, rskin_values, error_lower, error_upper, markers)):
        adjusted_err_down = min(err_down, 0.2)
        adjusted_err_up = min(err_up, 0.2)

        ax.errorbar(x, y, yerr=[[adjusted_err_down], [adjusted_err_up]], fmt=marker, markersize=8, capsize=0, label=labels[i])

        if err_down >= 1000:
            ax.plot([x], [y - adjusted_err_down], marker="v", color="grey", markersize=8)
        if err_up >= 1000:
            ax.plot([x], [y + adjusted_err_up], marker="^", color="grey", markersize=8)

    nsav = nuda.nuc.setupRnpAverage(source=source)
    if nsav.rnp_cen is not None:
        ax.errorbar(len(labels), nsav.rnp_cen, yerr=nsav.sig_std, label=nsav.label,
                    color='red', marker='o', markersize=10, linestyle='solid', linewidth=3)
        labels.append(nsav.label)

    ax.set_ylim([0, 0.5])
    ax.set_xticks(x_positions)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.set_ylabel(rf"$R_{{\rm{{skin}}}}$ {SOURCE_LABELS_LATEX[source]} (fm)", fontsize=15)
    ax.text(0.95, 0.95, subplot_label, transform=ax.transAxes, fontsize=15,
            verticalalignment='top', horizontalalignment='right')
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis='y', which='minor', length=4, color='gray')

    if pname is None:
        output_dir = os.path.abspath("figs/")
        os.makedirs(output_dir, exist_ok=True)
        pname = os.path.join(output_dir, f"plot_nuc_setupRnp_Exp_{source.replace(' ', '_')}.png")

    plt.tight_layout()
    plt.savefig(pname, dpi=200)
    plt.close()
    print(f"Plot saved: {pname}")