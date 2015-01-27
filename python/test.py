#!/usr/bin/env python

"""
Run doctests on all local modules.
"""

import argparse
import doctest
import glob
import os
import time

parser = argparse.ArgumentParser(description='Project Euler test script')
parser.add_argument('-q', '--quiet', dest='quiet', action='store_true',
                    help='Suppress progress and timing output')
args = parser.parse_args()

# Project Euler program names begin with a capital letter
for python_file in glob.glob(os.path.dirname(__file__) + '/[A-Z]*.py'):
    name = os.path.basename(python_file)[:-3]
    module = __import__(name, globals(), locals(), [name])

    starttime = time.time()
    doctest.testmod(module)
    if not args.quiet:
      duration = time.time() - starttime
      print('{}: {:1.3f} seconds'.format(name, duration))
