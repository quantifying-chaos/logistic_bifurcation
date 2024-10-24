import numpy as np


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NOC = '\033[0m'


def print_alert(string):
    print(bcolors.FAIL + bcolors.BOLD + string + bcolors.NOC)


def logistic(x, r):
    return r*x*(1-x)


def iterate_r(x_0, r, prep_times, plot_times):
    """
    Iterate the logistic function with initial value x_0 for r = r
    x_1 = logistic(x_0,r), etc

    x_0 to x_{prep_times-1} are ignored.
    x_{prep_times} to x_{prep_times+plot_times-1} are recorded in res
    and returned
    """
    val = x_0
    for _ in range(prep_times):
        val = logistic(val, r)

    res = []
    # ignore x_500, recording values from x_501
    for _ in range(plot_times):
        val = logistic(val, r)
        res.append(val)

    return res


def iterate_r_fn_1d(x_0, r, fn, prep_times, plot_times):
    """
    Iterate the fn function with initial value x_0 for r = r
    x_1 = logistic(x_0,r), etc

    The fn shall have signature fn(x, r) -> x

    x_0 to x_{prep_times-1} are ignored.
    x_{prep_times} to x_{prep_times+plot_times-1} are recorded in res
    and returned
    """
    val = x_0
    for _ in range(prep_times):
        val = fn(val, r)

    res = []
    # ignore x_500, recording values from x_501
    for _ in range(plot_times):
        val = fn(val, r)
        res.append(val)

    return res


def graph_bifurcation(fn, x_0=0, r_start=0, r_end=4,
                      n_of_r=1000, prep_times=100, plot_times=500, dimmmed=0,
                      x_low=None, x_high=None, saved_file_name=None, dpi=1000,
                      title=None):
    """
    Graph the bifurcation diagram of the fn function
    with initial value x_0 for r from r_start to r_end with step r_step

    The fn shall have signature fn(x, r) -> x
    """
    import matplotlib.pyplot as plt

    r_values = []
    x_values = []

    for r in np.linspace(r_start, r_end, n_of_r):
        # print(f"r = {r}")
        # ignore the prep_times x_values
        if x_0 == 0:
            # random value from 0 to 1
            x_0 = np.random.uniform(0, 1)
        x_values.extend(iterate_r_fn_1d(x_0, r, fn, prep_times, plot_times))
        r_values.extend([r]*plot_times)

    if dimmmed == 0:
        plt.scatter(r_values, x_values, s=0.5, c='tab:blue',
                    edgecolors='none', facecolors='tab:blue', marker='o')
    elif dimmmed == 1:
        plt.scatter(r_values, x_values, c='tab:blue', s=0.05,
                    alpha=0.4, edgecolors='none', facecolors='tab:blue',
                    marker='o')
    elif dimmmed == 2:
        plt.scatter(r_values, x_values, c='tab:blue', s=0.04,
                    alpha=0.2, edgecolors='none', facecolors='tab:blue',
                    marker='o')
    else:
        plt.scatter(r_values, x_values, c='tab:blue', s=0.05,
                    alpha=0.2, edgecolors='none', facecolors='tab:blue',
                    marker='o')

    plt.xlabel('r')
    plt.ylabel('x')
    if title:
        plt.title(title)

    if x_low is not None and x_high is not None:
        plt.ylim(x_low, x_high)

    # plt.title('Bifurcation diagram')
    if saved_file_name:
        plt.savefig(saved_file_name, dpi=dpi)
    plt.show()
