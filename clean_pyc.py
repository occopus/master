#!/usr/bin/env python

import os
import fnmatch
from argparse import ArgumentParser

args = ArgumentParser(description='List *.pyc files to be cleaned')
args.add_argument('--all', action='store_true', default=False,
                  help='List all *.pyc files (including site-packages, etc.)')
args.add_argument('--delete', action='store_true', default=False,
                  help='Delete files; don\'t just list them')
args = args.parse_args()

def Walk(root='.', recurse=True, pattern='*'):
    """
        Generator for walking a directory tree.
        Starts at specified root folder, returning files
        that match our pattern. Optionally will also
        recurse through sub-folders.
    """
    for path, subdirs, files in os.walk(root):
        dirname = os.path.basename(path)
        if (not args.all and
                (dirname in ('env', '.git', 'build')
                 or dirname.endswith('.egg-info'))) :
            del subdirs[:]
            continue
        for name in files:
            fname = os.path.join(path, name)
            if fnmatch.fnmatch(name, pattern):
                yield fname
        if not recurse:
            break

for fname in Walk('.', True, '*.pyc'):
    if args.delete:
        print "Deleting '{0}'".format(fname)
        os.remove(fname)
    else:
        print fname
