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
        if dirname in ('env', '.git') \
                or dirname.endswith('.egg-info'):
            print '# Skipping directory {0}'.format(path)
            del subdirs[:]
            continue
        for name in files:
            fname = os.path.join(path, name)
            if fnmatch.fnmatch(name, pattern) or check_py(fname):
                with open(fname) as fspec:
                    print '# Processing {0}'.format(fname), 
                    yield fspec
            else:
                print '# Skipping {0}'.format(fname)
        if not recurse:
            break

def str_pc(mini, maxi):
    return '{0:.1f}'.format(float(mini)/maxi*100) \
        if (mini and maxi) \
        else '--'

def LOC(root='', recurse=True):
    """
        Counts lines of code in two ways:
            maximal size (source LOC) with blank lines and comments
            minimal size (logical LOC) stripping same

        Sums all Python files in the specified folder.
        By default recurses through subfolders.
    """
    count_mini, count_maxi = 0, 0
    for fspec in Walk(root, recurse, '*.py'):
        s_count_mini, s_count_maxi = 0, 0
        skip = False
        for line in fspec.readlines():
            s_count_maxi += 1
            
            line = line.strip()
            if line:
                if line.startswith('#'):
                    continue
                if line.startswith('"""'):
                    skip = not skip
                    continue
                if not skip:
                    s_count_mini += 1

        print '({0}/{1}, {2}%)'.format(s_count_mini, s_count_maxi,
                                         str_pc(s_count_mini, s_count_maxi))
        count_mini += s_count_mini
        count_maxi += s_count_maxi

    print '{0}/{1}, {2}%'.format(count_mini, count_maxi,
                                     str_pc(count_mini, count_maxi))

LOC('.')
