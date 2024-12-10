
import os
# import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator  # Import para minor ticks

#plt.rcParams.update({'font.size': 16})

# nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
# sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

# Dictionary to map sources to LaTeX names
SOURCE_LABELS_LATEX = {
    "48Ca": r"$^{48}\mathrm{Ca}$",
    "208Pb": r"$^{208}\mathrm{Pb}$"
}

def plot_neutron_skin_for_each_source():
    """
    Generates neutron skin (R_skin) plots for each nucleus using data from the `SetupNeutronSkinExp` class.
    """
    # Retrieve available sources (e.g., '48Ca', '208Pb')
    sources, _ = nuda.nskin_exp()

# Labels for the subplots
    subplot_labels = ["(a)", "(b)"]  # Adjust this list based on the number of sources

    # Iterate over each source to create individual plots
    for idx, source in enumerate(sources):
        # Lists to store data for the plot
        labels = []  # Labels for references (e.g., 'Brissaud 1972')
        rskin_values = []  # R_skin values
        error_lower = []  # Lower errors
        error_upper = []  # Upper errors
        markers = []  # Marker types to customize the points

        # Retrieve available calculations for the source
        cals = nuda.nuc.nskin_exp_source(source)
        
        for cal in cals:
            # Instantiate the object for the specific calculation
            neutron_skin_calc = nuda.nuc.SetupNeutronSkinExp(source=source, cal=cal)
            
            # Store data only if R_skin is available
            if neutron_skin_calc.nskin is not None:
                labels.append(neutron_skin_calc.label)  # Use `self.label` as label
                rskin_values.append(neutron_skin_calc.nskin)
                
                # Replace `None` error values with 0.0
                err_down = neutron_skin_calc.nskin_sig_do if neutron_skin_calc.nskin_sig_do is not None else 0.0
                err_up = neutron_skin_calc.nskin_sig_up if neutron_skin_calc.nskin_sig_up is not None else 0.0
                error_lower.append(err_down)
                error_upper.append(err_up)
                
                # Ensure the marker is valid
                marker = neutron_skin_calc.marker if neutron_skin_calc.marker else 'o'
                markers.append(marker)

        # Check if there is data to plot
        if not rskin_values:
            print(f"No data available for {source}.")
            continue

        # Plot configuration
        fig, ax = plt.subplots(figsize=(10, 8))
        x_positions = range(len(labels))  # X-axis positions

        # Add each point to the plot with vertical error bars
        for i, (x, y, err_down, err_up, marker) in enumerate(zip(x_positions, rskin_values, error_lower, error_upper, markers)):
            # Handle large errors (>= 1000) by limiting the bar to 0.1
            adjusted_err_down = min(err_down, 0.2)
            adjusted_err_up = min(err_up, 0.2)

            # Add adjusted error bars
            ax.errorbar(x, y, yerr=[[adjusted_err_down], [adjusted_err_up]], fmt=marker, markersize=8, capsize=0, label=labels[i])
            
            # Add arrow as cap for err_down >= 1000
            if err_down >= 1000:
                ax.plot([x], [y - adjusted_err_down], marker="v", color="grey", markersize=8)

            # Add arrow as cap for err_up >= 1000
            if err_up >= 1000:
                ax.plot([x], [y + adjusted_err_up], marker="^", color="grey", markersize=8)

        nsav = nuda.nuc.setupNeutronSkinAverage(source=source)
        if nsav.nskin_cen is not None:
            ax.errorbar(len(labels), nsav.nskin_cen, yerr=nsav.sig_std, label=nsav.label, 
                       color='red', marker='o', linestyle='solid', linewidth=3)        
 
        # Fixed y-axis configuration
        ax.set_ylim([0, 0.5])  # Fixed scale from 0 to 0.5 on the y-axis

        # X-axis configuration
        ax.set_xticks(x_positions)
        ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=15)

        # Y-axis configuration and layout
        # Increase font size for y-axis numbers
        ax.tick_params(axis='y', labelsize=15)  # Adjust the font size as desired
        ax.set_ylabel(rf"$R_{{\rm{{skin}}}}$ {SOURCE_LABELS_LATEX[source]} (fm)", fontsize=15)
        # ax.set_xlabel(f"References for {SOURCE_LABELS_LATEX[source]}", fontsize=14)
        # ax.grid(True, linestyle="--", alpha=0.5)

        # Adjust the legend (only if there are valid labels)
        # ax.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=10)

        # Add subplot label (e.g., "(a)", "(b)") in the top right corner
        ax.text(0.95, 0.95, subplot_labels[idx], transform=ax.transAxes, fontsize=15,
                verticalalignment='top', horizontalalignment='right')

        # Add minor ticks on y-axis
        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.tick_params(axis='y', which='minor', length=4, color='gray')  # Style for minor ticks

        # Final adjustments and save the plot
        output_dir = "figs/"
        os.makedirs(output_dir, exist_ok=True)
        fig_name = f"{output_dir}plot_nuc_setup_nskin_exp-{source}.png"
        plt.tight_layout()
        plt.savefig(fig_name)
        plt.close()
        
        print(f"Plot saved: {fig_name}")

if __name__ == "__main__":
    plot_neutron_skin_for_each_source()
