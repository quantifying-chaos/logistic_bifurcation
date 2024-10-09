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
