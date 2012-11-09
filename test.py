#!/usr/bin/env python

"""
Run doctests on all local modules.
"""


import doctest
import glob

for filename in glob.glob('*.py'):
    name = filename[:-3]
    module = __import__(name, globals(), locals(), [name])
    doctest.testmod(module)
