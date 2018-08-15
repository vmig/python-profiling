# -*- coding: utf-8 -*-

# BUILT-IN PROFILER (cProfile)

# To use the cProfile module:
#     python -m cProfile -s cumulative 01_simple_timer.py
# The report is sorted by the cumulative time spent on each function (thanks to the -s cumulative option).

# Pros: No external dependencies and quite fast.
#       Useful for quick high-level checks.
# Cons: Rather limited information that usually requires deeper debugging;
#       reports are a bit unintuitive, especially for complex codebases.

# Viewers:
# 1. PyCharm integrated tool:
#    https://www.jetbrains.com/pycharm/   (Tools -> Open CProfile snapshot)
# 2. `SnakeViz` is a browser based graphical viewer for the output of Python’s cProfile module:
#    https://jiffyclub.github.io/snakeviz/
# 3. `tuna` is a Python profile viewer:
#    https://github.com/nschloe/tuna

import cProfile
from functools import wraps
import os

from source import REPORTS_DIR, cube_function


report = os.path.join(REPORTS_DIR, "cprofile.dat")


def do_cprofile(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            res = fn(*args, **kwargs)
            profile.disable()
            return res
        finally:
            profile.print_stats()
            profile.dump_stats(report)
    return wrapper


@do_cprofile
def expensive_function():
    return cube_function()


# Perform profiling
result = expensive_function()
