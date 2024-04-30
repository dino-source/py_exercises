from os import listdir
from os.path import isfile, join
from collections import deque


def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                for _ in range(1, int(file[0])):
                    print("\t", end='')
                print(f"|__{file}")
            else:
                search_queue.append(fullpath)
                

printnames("docs")
