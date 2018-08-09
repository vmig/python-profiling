# -*- coding: utf-8 -*-

# SIMPLE TIMING DECORATOR

# Pros: Easy to understand and implement.
#       Also very simple to compare before and after fixes.
#       Works across many languages.
# Cons: Sometimes a little too simplistic for extremely complex codebases,
#       you might spend more time placing and replacing boilerplate code than you will fixing the problem!

import time
from functools import wraps

from source import cube_function


def metrics(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = fn(*args, **kwargs)
        t1 = time.time()
        print("Total time running '{}': {} seconds".format(fn.__name__, t1 - t0))
        return res
    return wrapper


@metrics
def expensive_function():
    return cube_function()


# Perform profiling
result = expensive_function()
