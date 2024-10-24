import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from utils import iterate_r


#################
# Global variables
#################

# Lower bound of r
r_low = 2.5
# Upper bound of r
r_high = 4.0
n_of_r = 3500  # Number of r values to try

# init x
x_0 = 0.5

prep_times = 0  # Number of iterations to ignore
plot_times = 1000  # Number of iterations to plot


# Start of plotting

marker_style = dict(linestyle=':', color='b',
                    markersize=0.001, fillstyle='full')

fig, ax = plt.subplots()
plt.grid(color='gray', linestyle=':', linewidth=0.5)

r_vals = np.linspace(r_low, r_high, n_of_r)

for r in r_vals:
    # variable line size as for r <3.5 there are very few paths
    l_size = 0.05
    if r < 3.5:  # before 3.5 the system is rather stable
        x = iterate_r(x_0, r, prep_times, 100)
        l_size = 0.1
    else:
        x = iterate_r(x_0, r, prep_times, plot_times)
        l_size = 0.05

    # plt.plot([r]*len(x), x, ',b')
    r_dummy = np.linspace(r, r, len(x))
    ax.scatter(r_dummy, x, c='tab:blue', s=l_size,
               alpha=0.3, edgecolors='none', facecolors='tab:blue',
               marker='o')

ax.plot(r_vals, 1 - 1/r_vals, color='r',
        linestyle='--', linewidth=0.8, alpha=0.5)

# Custom legend
legend_elements = [
    Line2D([0], [0], color='r', linestyle='--', linewidth=0.8, label='1-1/r'),
    Line2D([0], [0], marker='o', color='w', label='x values',
           markerfacecolor='b', markersize=3),
]


ax.legend(handles=legend_elements, loc='upper left', fontsize=10)


plt.xlabel('r', fontsize=15)
plt.ylabel('x', fontsize=15)

plt.xlim(r_low, r_high)
plt.show()
# plt.axis('off')
# plt.gca().set_position([0, 0, 1, 1])

# dpi = 2000 -> 28 MB image
# dpi = 1000 -> 7 MB image
# plt.savefig("bifurcation.png", dpi=2000)
