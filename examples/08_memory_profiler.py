# -*- coding: utf-8 -*-

# MEMORY_PROFILER
# https://github.com/pythonprofilers/memory_profiler

# --- Command line usage ---:
#     python -m memory_profiler 08_memory_profiler.py

# --- Time-based memory usage ---
# Before use it, need to install some packages (Ubuntu):
#     $ sudo apt-get install python3-tk

# and then:
#     mprof run <script>    # mprof run 01_simple_timer.py
#     mprof plot
#     mprof clean

# Also, please refer to documentation about
#     mprof run --include-children <script>
#     mprof run --multiprocess <script>


import os

from memory_profiler import profile

from source import REPORTS_DIR


report = os.path.join(REPORTS_DIR, "mprofile_*.dat")


@profile
# @profile(precision=4)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


# Perform profiling
my_func()
