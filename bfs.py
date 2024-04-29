# Breadth-first search
from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire", ]
graph["bob"] = ["anuj", "peggy", ]
graph["alice"] = ["peggy", ]
graph["claire"] = ["thom", "johnny", ]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []


def is_mango_seller(name: str) -> bool:
    return name[-1] == 'm'


def bfs(name: str) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_mango_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


bfs("you")
