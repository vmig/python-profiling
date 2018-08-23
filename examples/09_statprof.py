# -*- coding: utf-8 -*-

# SIMPLE STATISTICAL PROFILER for Python
# https://github.com/bos/statprof.py
# pip install git+https://github.com/bos/statprof.py.git@master#egg=statprof


import statprof


def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


# Perform profiling
statprof.start()
try:
    my_func()
finally:
    statprof.stop()
    statprof.display()

# .. or with context manager
with statprof.profile():
    my_func()
