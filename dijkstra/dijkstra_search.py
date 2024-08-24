from math import inf as infinity
from typing import Union


def find_lowest_cost_node(c: dict[str, int], p: set) -> Union[str, None]:
    costs = c
    processed = p

    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node
