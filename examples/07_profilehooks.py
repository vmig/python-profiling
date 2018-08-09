# -*- coding: utf-8 -*-

# PROFILEHOOKS
# https://github.com/mgedmin/profilehooks

import os

from profilehooks import profile, coverage, timecall

from source import REPORTS_DIR, cube_function, random_sort


report = os.path.join(REPORTS_DIR, "profilehooks.dat")


@profile
# @profile(immediate=True)
# @profile(filename=report)
def expensive_function_1():
    return cube_function()


@timecall
# @timecall(immediate=True)
def expensive_function_2(n):
    return random_sort(n)


@coverage
def silly_factorial_example(n):
    """Return the factorial of n."""
    if n < 1:
        raise ValueError("n must be >= 1, got {}".format(n))
    if n == 1:
        return 1
    else:
        return silly_factorial_example(n - 1) * n


# Perform profiling
expensive_function_1()
expensive_function_2(1000000)
silly_factorial_example(1)
