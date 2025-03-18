import os
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import AutoMinorLocator  # Import para minor ticks

#plt.rcParams.update({'font.size': 16})

# nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
# sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda



if __name__ == "__main__":
    plot_neutron_skin_for_each_source_and_param()
