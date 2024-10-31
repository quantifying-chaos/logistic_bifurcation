import numpy as np
from tabulate import tabulate

import utils


def display_res(func, A_list):
    print(f"bifurcation points: {A_list}")

    feigenbuam_delta_list = [(A_list[i] - A_list[i - 1]) /
                             (A_list[i + 1] - A_list[i])
                             for i in range(1, len(A_list)-1)]

    d_orbit_list = [abs(f_iter(func, 0.5, A_list[i], 2**(i-1))-0.5)
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


def sin_d(x, r):
    return r * np.sin(np.pi * x)


def f_iter(func, x, r, n):
    res = x
    for i in range(0, n):
        res = func(res, r)
    return res


def stable_orbit(func, r, x_init, f_cycle, thres, iter_times=5):
    """
    Check if the f_cycle_orbit of the f map is stable,
    with r and init val

    NOTE: at A_n, the 2^n stable orbit contains x = 0.5

    Returns stable f(x_init) iterated iter_times all fall within thres of x_init
    """
    def g(x):
        for _ in range(f_cycle):
            x = func(x, r)
        return x

    val = x_init
    for _ in range(iter_times):
        val = g(val)

        if abs(val - x_init) > thres:
            return False

    return True


# Do the calculation
A_list = [0.5, 0.7777337]
r_max = 0.9
r = 0.83
x_0 = 0.5
n_cycle = 4
delta = 1e-4
thres = 1e-4
iter_n = 2
feigenbuam_delta = 4.4669
r_interval = 0.001
while True:
    if r > r_max:
        utils.print_alert("r_max reached")
        break
    limit = 15
    if len(A_list) > limit:
        utils.print_alert(f"{limit} bifurcation points found")
        break
    if stable_orbit(sin_d, r, x_0, n_cycle, thres, iter_times=iter_n):
        A_list.append(r)
        n_cycle *= 2
        thres /= 2
        r += r_interval
        r_interval /= feigenbuam_delta
        delta /= feigenbuam_delta
        # iter_n += 1
        thres /= 1.05
        display_res(sin_d, A_list)

    r += delta


display_res(sin_d, A_list)

# NOTE (1/Feigenbaum)^11 ~= 4.35e-8: near te limit of float precision
# Assuming feigenbuam_alpha_list is already defined
print("""
      Comments:
      We have calculated the first 10 bifurcation points.
      The accuracy required thereafter is smaller than
      (1/delta)^10 ~= 2e-7, close to the limit of float-point precision.
      """)

# OUTPUT
# 12 bifurcation points found
# bifurcation points: [0.5, 0.7777337, 0.8463399999999256, 0.8614392634712809, 0.8646912187601725, 0.8653888250295066, 0.865538416614664, 0.8655705110122935, 0.8655773887984283, 0.8655788653955588, 0.8655791821435145, 0.8655792501865809, 0.8655792648089539]
# Calculated Feigenbaum Alpha:
# +-------+---------+
# | Index |  Alpha  |
# +-------+---------+
# |   0   | 2.59262 |
# |   1   | 2.52183 |
# |   2   | 2.50726 |
# |   3   | 2.50468 |
# |   4   | 2.50442 |
# |   5   | 2.50378 |
# |   6   | 2.50494 |
# |   7   | 2.50460 |
# |   8   | 2.50569 |
# |   9   | 2.50617 |
# |  10   | 2.50717 |
# +-------+---------+
# expected: 2.5029
#
# Calculated Feigenbaum Delta:
# +-------+---------+
# | Index |  Delta  |
# +-------+---------+
# |   0   | 4.04822 |
# |   1   | 4.54369 |
# |   2   | 4.64313 |
# |   3   | 4.66159 |
# |   4   | 4.66341 |
# |   5   | 4.66099 |
# |   6   | 4.66638 |
# |   7   | 4.65786 |
# |   8   | 4.66174 |
# |   9   | 4.65511 |
# |  10   | 4.65335 |
# +-------+---------+
