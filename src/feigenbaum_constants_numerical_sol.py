import numpy as np
from tabulate import tabulate

import utils


def logistic(x, r):
    return r * x * (1 - x)


def logistic_iter(x, r, n):
    res = x
    for i in range(0, n):
        res = logistic(res, r)
    return res


def stable_orbit(r, x_init, f_cycle, thres, iter_times=10):
    """
    Check if the f_cycle_orbit of the logistic map is stable,
    with r and init val

    NOTE: at A_n, the 2^n stable orbit contains x = 0.5

    Returns stable f(x_init) iterated iter_times all fall within thres of x_init
    """
    def f(x):
        for _ in range(f_cycle):
            x = logistic(x, r)
        return x

    val = x_init
    for _ in range(iter_times):
        val = f(val)

        if abs(val - x_init) > thres:
            return False

    return True


# Do the calculation
# This is the constants A_n
A_list = [2, float(np.sqrt(5) + 1)]
# start calculation with A_2 ~= 3.498553
r_max = 3.58
r = float(np.sqrt(5) + 1) + 0.1
x_0 = 0.5
n_cycle = 4
delta = 1e-5
thres = 1e-5
iter_n = 10
feigenbuam_delta = 4.4669
r_interval = 0.04
while len(A_list) < 11 and r < r_max:
    if stable_orbit(r, x_0, n_cycle, thres, iter_times=iter_n):
        A_list.append(r)
        n_cycle *= 2
        thres /= 2
        r += r_interval
        r_interval /= feigenbuam_delta
        delta /= feigenbuam_delta
        iter_n += 1
        thres /= 1.05

    r += delta


print(f"Calculated A_n: {A_list}")

feigenbuam_delta_list = [(A_list[i] - A_list[i - 1]) /
                         (A_list[i + 1] - A_list[i])
                         for i in range(1, len(A_list)-1)]

d_orbit_list = [abs(logistic_iter(0.5, A_list[i], 2**(i-1))-0.5)
                for i in range(1, len(A_list))]

feigenbuam_alpha_list = [d_orbit_list[i-1]/d_orbit_list[i]
                         for i in range(1, len(d_orbit_list))]


# Display the results

table = [[i, f"{feigenbuam_alpha_list[i]:.5f}"]
         for i in range(len(feigenbuam_alpha_list))]

# Print with headers and table format
print("Calculated Feigenbaum Alpha:")
print(tabulate(table, headers=["Index", "Alpha"], tablefmt="pretty"))
utils.print_emph("expected: 2.5029")

table = [[i, f"{feigenbuam_delta_list[i]:.5f}"]
         for i in range(len(feigenbuam_delta_list))]
print()
print("Calculated Feigenbaum Delta:")
print(tabulate(table, headers=["Index", "Delta"], tablefmt="pretty"))
utils.print_emph("expected: 4.6692")

# NOTE (1/Feigenbaum)^11 ~= 4.35e-8: near te limit of float precision
# Assuming feigenbuam_alpha_list is already defined
print("""
      Comments:
      We have calculated the first 10 bifurcation points.
      The accuracy required thereafter is smaller than
      (1/delta)^10 ~= 2e-7, close to the limit of float-point precision.
      """)
