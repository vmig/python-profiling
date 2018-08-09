# -*- coding: utf-8 -*-

# TIMEIT MODULE

# `timeit` gives an average time measure.
# To run it, execute the following command in your terminal:
#     python -m timeit -n 4 -r 5 -s "import timing_functions" "timing_functions.random_sort(2000000)"
# where `timing_functions` is the name of your script.
#
# At the end of the output, you should see something like:
#    4 loops, best of 5: 2.08 sec per loop
# indicating that of 4 times running the test (-n 4), and averaging 5 repetitions on each test (-r 5),
# the best test result was of 2.08 seconds.
#
# If you don’t specify the number of tests or repetitions, it defaults to 10 loops and 5 repetitions.

import timeit

s = """\
try:
    int.__nonzero__
except AttributeError:
    pass
"""

print(timeit.timeit(stmt=s, number=100000))

print(timeit.timeit("random_sort(20)", setup="from source import random_sort"))
