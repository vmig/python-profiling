# -*- coding: utf-8 -*-

# LINE PROFILER
# https://github.com/rkern/line_profiler

# Pros: Has intuitive and finely detailed reports.
#       Can follow functions in third party libraries.
# Cons: Because of the overhead it can be an order of magnitude slower than real execution time,
#       so don't use it for benchmarking. It is also an external requirement.

from functools import wraps
import os


from source import REPORTS_DIR, get_number, cube_function


report = os.path.join(REPORTS_DIR, "line_profile.lprof")

try:
    from line_profiler import LineProfiler

    def do_profile(follow=[]):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                profiler = LineProfiler()
                profiler.add_function(fn)
                try:
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return fn(*args, **kwargs)
                finally:
                    profiler.print_stats(output_unit=1)
                    profiler.dump_stats(report)
            return wrapper
        return decorator

except ImportError:
    def do_profile(follow=[]):
        """Helpful if you accidentally leave in production!"""
        def decorator(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return decorator


@do_profile(follow=[get_number, cube_function])
def expensive_function():
    return cube_function()


# Perform profiling
result = expensive_function()
