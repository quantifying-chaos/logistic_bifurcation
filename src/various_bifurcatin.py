import numpy as np
from utils import graph_bifurcation


def sin_dummy(x, r):
    return r * np.sin(np.pi * x)


# graph_bifurcation(sin_dummy, r_start=0, r_end=4,
#                   n_of_r=3000, prep_times=300, plot_times=2500, dimmmed=2,
#                   saved_file_name='sin_bifurcation.png')

def double_log(x, r):
    return r * np.log(0.5*x+0.5) * np.log(1 - 0.5 * x)
#
#
# graph_bifurcation(double_log, r_start=5, r_end=15,
#                   n_of_r=2000, prep_times=300, plot_times=2500, dimmmed=2,
#                   x_low=0, x_high=1.1,
#                   saved_file_name='double_log_bifurcation.png')


def e_sin(x, r):
    return r * np.exp(x)*np.sin(np.pi * x)


graph_bifurcation(e_sin, r_start=0.2, r_end=1.5,
                  n_of_r=2000, prep_times=400, plot_times=2800, dimmmed=2, title="r e^x sin(pi x)",
                  x_low=-1.2, x_high=1.2,
                  saved_file_name='e_sin.png')


def deg_three(x, r):
    return r*x*(x-1)*(x-2)


# graph_bifurcation(deg_three, r_start=0.2, r_end=3,
#                   n_of_r=2000, prep_times=400, plot_times=2800, dimmmed=2, title="r x(x-1)(x-2)",
#                   saved_file_name='deg_three.png')
