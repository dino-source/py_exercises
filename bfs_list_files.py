# Breadth-first search #

# Output will be as follows:
# odissey.png
# a.png
# space.png


from collections import deque
from os import listdir
from os.path import isfile, join


def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)


printnames("pics")
