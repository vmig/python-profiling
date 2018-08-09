# -*- coding: utf-8 -*-

# Examples of expensive functions

__all__ = ['REPORTS_DIR', 'get_number', 'cube_function', 'random_sort']

import os
import random


REPORTS_DIR = "{}/reports".format(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def get_number():
    for x in range(5000000):
        yield x


def cube_function():
    for x in get_number():
        i = x ^ x ^ x
    return "Some result!"


def random_sort(n):
    return sorted([random.random() for i in range(n)])
