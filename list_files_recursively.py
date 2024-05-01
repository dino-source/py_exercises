# Depth-first search (recursive version)

from os import listdir
from os.path import isfile, join


def dfs_and_print(dir: str):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            dfs_and_print(fullpath)


dfs_and_print("docs")
