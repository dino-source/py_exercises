# Breadth-first search
from collections import deque


graph = {}
graph["1_you"] = ["2_alice", "2_bob", "2_claire", ]
graph["2_bob"] = ["3_anuj", "3_peggy", ]
graph["2_alice"] = ["3_peggy", ]
graph["2_claire"] = ["3_thom", "3_johnny", ]
graph["3_anuj"] = []
graph["3_peggy"] = []
graph["3_thom"] = []
graph["3_johnny"] = []


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

print(graph)
bfs("1_you")
