# -*- coding: utf-8 -*-

# SIMPLE STATISTICAL PROFILER for Python
# https://github.com/bdarnell/plop

# To profile an entire Python script, run:
#    python -m plop.collector myscript.py
# This will write the profile to `./profiles/[timestamp]`. Add `-f flamegraph` for flamegraph output.

# To use the viewer for the default .plop output format, run:
#    python -m plop.viewer --datadir=demo/profiles
# and go to http://localhost:8888. For .flame format, see https://github.com/brendangregg/FlameGraph


def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


# Perform profiling
my_func()
