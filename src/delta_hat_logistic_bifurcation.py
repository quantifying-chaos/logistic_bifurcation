#########################
# This script tries to compute the delat_hat
# As described in page 38, Chaos in Dynamical System, E. Ott, 2002
#
# Brief Outline
# Logistic function is defined as x_{n+1} = rx_n(1-x_n).
# We are interested in the case 0<x_0<1, 1<r<4,
# where it exhibits interesting behaviour (including chaos)
# (For more, check repo's readme)
#
# before r_0 = 3, there is one stable orbit.
# At r_0 = 3, this stable orbit becomes unstable,
# and two new stable orbits were formed.
# At r_1 ~= 3.4, the two stable orbits become unstable,
# and four stable orbits form,
# This is called bifurcation.
#
# It has been proved that (r_m-r_{m-1})/(r_{m+1}-r_m) ~= 4.67
# The following script trys to validate this statement

# NOTE:
# We assume the python double precision are accurate upto 16 sigfigs

import numpy as np
import math
from logistic import iterate_r

import matplotlib.pyplot as plt


# Lower bound of r
r_low = 2.8
# Upper bound of r
r_high = 4
n_of_r = 1000  # Number of r values to try

r_vals = np.linspace(r_low, r_high, n_of_r)

# init x
x_0 = 0.5

prep_times = 500  # Number of iterations to ignore
plot_times = 2000  # Number of iterations to plot


def box_distri_count(vec):
    """
    Input a vector v = [0,0,0,1,1,4,0,0,0,2,0]
    out put how many continuous, non-zero region there is.
    eg, v has 2 continuous, non-zero region
    [1,0,1,0,1] has three
    """
    res = 0
    prev_is_zero = 1
    for i in vec:
        if i == 0:
            prev_is_zero = 1
            continue
        # i != 0
        if prev_is_zero:
            res += 1
        prev_is_zero = 0

    return res


def number_of_scattered_center(data, upper_bound, lower_bound, precision):
    """
    Will disregard data that falls out of the bound
    """

    n_boxes = (upper_bound - lower_bound)/precision
    box_width = (upper_bound - lower_bound) / n_boxes
    boxes = [0] * int(n_boxes)

    for i in data:
        if i >= upper_bound or i < lower_bound:
            continue
        boxes[math.floor((i-lower_bound)/box_width)] += 1

    return box_distri_count(boxes)


print(
    number_of_scattered_center(iterate_r(x_0, 3.565, 500, 500), 1, 0, 0.0001)
)
