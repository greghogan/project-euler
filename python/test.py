#!/usr/bin/env python

"""
Run doctests on all local modules.
"""

import doctest
import glob
import os

# Project Euler program names begin with a capital letter
for python_file in glob.glob(os.path.dirname(__file__) + '/[A-Z]*.py'):
    name = os.path.basename(python_file)[:-3]
    module = __import__(name, globals(), locals(), [name])
    doctest.testmod(module)
