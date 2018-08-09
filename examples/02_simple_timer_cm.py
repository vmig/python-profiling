# -*- coding: utf-8 -*-

# SIMPLE TIMING DECORATOR WITH A CONTEXT MANAGER

import time

from source import cube_function


class Metrics(object):

    def __init__(self, name=''):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name=''):
        print("{timer} {checkpoint}: {elapsed} seconds".format(
            timer=self.name,
            checkpoint=name,
            elapsed=self.elapsed,
        ).strip())

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('finished')
        pass


def expensive_function():
    return cube_function()


# Perform profiling
with Metrics('MyFunc') as timer:
    expensive_function()
    timer.checkpoint('done with something')
    expensive_function()
    expensive_function()
    timer.checkpoint('done with something else')

# ... or directly
timer = Metrics('MyFunc')
expensive_function()
timer.checkpoint('done with something')
