#!/usr/bin/env python

import os
import fnmatch
import magic

def check_py(fname):
    return magic.from_file(fname, mime=True) == 'text/x-python'

def Walk(root='.', recurse=True, pattern='*'):
    """
        Generator for walking a directory tree.
        Starts at specified root folder, returning files
        that match our pattern. Optionally will also
        recurse through sub-folders.
    """
    for path, subdirs, files in os.walk(root):
        dirname = os.path.basename(path)
        if dirname in ('env', '.git', 'build') \
                or dirname.endswith('.egg-info'):
            del subdirs[:]
            continue
        for name in files:
            fname = os.path.join(path, name)
            if fnmatch.fnmatch(name, pattern) or check_py(fname):
                yield fname
        if not recurse:
            break

for fname in Walk('.', True, '*.py'):
    print fname
