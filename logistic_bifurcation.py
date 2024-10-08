import numpy as np
import matplotlib.pyplot as plt


#################
# Global variables
#################

# Lower bound of r
x_low = 2.5
# Upper bound of r
x_high = 4.0

# init x
x_0 = 0.5

prep_times = 500  # Number of iterations to ignore
plot_times = 1500  # Number of iterations to plot
n_of_r = 2000  # Number of r values to try


def logistic(x, r):
    return r*x*(1-x)


def iterate_r(x_0, r, prep_times, plot_times):
    val = np.random.uniform(0, 1)
    for _ in range(prep_times):
        val = logistic(val, r)

    res = []
    # ignore x_500, recording values from x_501
    for _ in range(plot_times):
        val = logistic(val, r)
        res.append(val)

    return res

# Start of plotting


marker_style = dict(linestyle=':', color='b',
                    markersize=0.001, fillstyle='full')

fig, ax = plt.subplots()
plt.grid(color='gray', linestyle=':', linewidth=0.5)
for r in np.linspace(x_low, x_high, n_of_r):
    if r < 3.5:  # before 3.5 the system is rather stable
        x = iterate_r(x_0, r, prep_times, 100)
    else:
        x = iterate_r(x_0, r, prep_times, plot_times)

    # plt.plot([r]*len(x), x, ',b')
    r_dummy = np.linspace(r, r, len(x))
    ax.scatter(r_dummy, x, c='tab:blue', s=0.1,
               alpha=0.90, edgecolors='none', facecolors='tab:blue',
               marker='o')


plt.xlabel('r', fontsize=15)
plt.ylabel('x', fontsize=15)

plt.xlim(x_low, x_high)
# plt.show()
# plt.axis('off')
# plt.gca().set_position([0, 0, 1, 1])
plt.savefig("small_logistic_map.png", dpi=200)
