import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator  # Import para minor ticks
import os

import nucleardatapy as nuda

# Dictionary to map sources to LaTeX names
SOURCE_LABELS_LATEX = {
    "48Ca": r"$^{48}\mathrm{Ca}$",
    "208Pb": r"$^{208}\mathrm{Pb}$"
}

# Directory containing the model data tables
MODEL_TABLES_DIR = nuda.param.path_data + '/rnp/'

# Define markers and colors for each model
MODEL_STYLES = {
    "skyrme": {"color": "blue", "marker": "s", "label": "Skyrme"},
    "nlrh": {"color": "red", "marker": "^", "label": "NLRH"},
    "ddrh": {"color": "green", "marker": "D", "label": "DDRH"}
}

def read_model_data(directory, source):
    model_data = {}
    for filename in os.listdir(directory):
        if filename.endswith(".dat") and source in filename:
            model_name = filename.split("rnp")[0].lower()
            filepath = os.path.join(directory, filename)
            data = []
            with open(filepath, 'r') as file:
                for line in file:
                    if line.startswith("#") or not line.strip():
                        continue
                    parts = line.split()
                    param = parts[0]
                    rn, rp, rskin = map(float, parts[1:4])
                    data.append((param, rn, rp, rskin))
            model_data[model_name] = np.array(data, dtype=object)
            if nuda.env.verb:
                print(f"Loaded model data for {model_name}: {model_data[model_name]}")
    return model_data

def nuc_setupRnpTheo_fig(pname, source):
    print(f'Plot name: {pname}')
    print(f'Using source: {source}')

    # subplot_label = "(a)"  # remove this if you don't want any labels
    subplot_label = " "

    labels = []
    rskin_values = []
    error_lower = []
    error_upper = []
    xexp = []

    cals = nuda.nuc.rnp_exp_source(source)
    for i, cal in enumerate(cals):
        neutron_skin_calc = nuda.nuc.setupRnpExp(source=source, cal=cal)
        if neutron_skin_calc.rnp is not None:
            labels.append(neutron_skin_calc.label)
            rskin_values.append(neutron_skin_calc.rnp)
            xexp.append(i)
            err_down = neutron_skin_calc.rnp_sig_lo if neutron_skin_calc.rnp_sig_lo is not None else 0.0
            err_up = neutron_skin_calc.rnp_sig_up if neutron_skin_calc.rnp_sig_up is not None else 0.0
            error_lower.append(err_down)
            error_upper.append(err_up)

    model_data = read_model_data(MODEL_TABLES_DIR, source)
    combined_rskin = []
    combined_errors = []
    combined_markers = []
    combined_colors = []
    xtheo = []

    for model_name, data in model_data.items():
        for j, (_, _, _, rskin) in enumerate(data):
            x_position = xexp[j % len(xexp)] + 0.5  # Cycle through xexp and offset by 0.5
            xtheo.append(x_position)
            combined_rskin.append(rskin)
            combined_errors.append((0.0, 0.0))
            combined_markers.append(MODEL_STYLES[model_name]["marker"])
            combined_colors.append(MODEL_STYLES[model_name]["color"])

    if nuda.env.verb:
        print(f"Experimental positions for {source}: {xexp}")
        print(f"Theoretical positions for {source}: {xtheo}")

    fig, ax = plt.subplots(figsize=(10, 8))
    for i, (x, y, err_down, err_up) in enumerate(zip(xexp, rskin_values, error_lower, error_upper)):
        adjusted_err_down = min(err_down, 0.2)
        adjusted_err_up = min(err_up, 0.2)
        ax.errorbar(x, y, yerr=[[adjusted_err_down], [adjusted_err_up]], fmt='o', markersize=8, capsize=0, color='black', markerfacecolor='none')
        if err_down >= 1000:
            ax.plot([x], [y - adjusted_err_down], marker="v", color="black", markersize=8)
        if err_up >= 1000:
            ax.plot([x], [y + adjusted_err_up], marker="^", color="black", markersize=8)

    nsav = nuda.nuc.setupRnpAverage(source=source)
    if nsav.rnp_cen is not None:
        ax.errorbar(len(labels), nsav.rnp_cen, yerr=nsav.sig_std, label=nsav.label, 
                   color='k', marker='o', markersize=10, linestyle='solid', linewidth=3)           

    for i, (x, y, marker, color) in enumerate(zip(xtheo, combined_rskin, combined_markers, combined_colors)):
        ax.plot(x, y, marker=marker, markersize=8, color=color)

    # Add legend for experimental points
    ax.scatter([], [], color='black', marker='o', facecolors='none', label='Experimental/Analysis')

    # Add legend for theoretical models
    for model_name, style in MODEL_STYLES.items():
        ax.scatter([], [], color=style["color"], marker=style["marker"], label=style["label"])

    ax.set_ylim([0, 0.5])
    ax.set_xticks(xexp)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=15)
    ax.set_ylabel(rf"$R_{{\rm{{skin}}}}$ {SOURCE_LABELS_LATEX[source]} (fm)", fontsize=15)
    ax.text(0.95, 0.95, subplot_label, transform=ax.transAxes, fontsize=15, verticalalignment='top', horizontalalignment='right')

    # Add minor ticks on y-axis
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis='y', which='minor', length=4, color='gray')

    ax.legend(loc="upper right", bbox_to_anchor=(0.5, 1), fontsize=12)

    output_dir = "figs/"
    os.makedirs(output_dir, exist_ok=True)
    fig_name = os.path.join(output_dir, f"plot_nuc_setupRnpTheo_source{source.replace(' ', '_')}.png")    
    plt.tight_layout()
    plt.savefig(fig_name, dpi=200)
    plt.close()

    print(f"Plot saved: {fig_name}")