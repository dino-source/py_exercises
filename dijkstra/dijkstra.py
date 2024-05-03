from dijkstra_search import find_lowest_cost_node
from globals import costs, graph, parents, processed


node = find_lowest_cost_node(costs, processed)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs, processed)












