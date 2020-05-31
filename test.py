'''Testing complex expressions

Usage:
    TBD
'''

from pprint import pprint as pp
import os
import glob

file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)