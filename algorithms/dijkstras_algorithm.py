graph = {}

graph['you'] = ["alice", "bob","clarie"]

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# print(*graph['start'].keys())

# включим в граф остальные узлы и из соседей

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# print(graph)

# the costs table - таблица весов ребер графа
infinity = float("inf") #бесконечность в - infinity in python
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#код создания хэш-таблицы родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    pass

# Find the lowest-cost node that you haven't processed yet.
#Найти узел с наименьшей стоимостью среди необработанных
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
# Если узлы обработаны - цикл завершен
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        #перебор всех соседей
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        # Если к соседу можно добраться быстрее через текущий узел
        if costs[n] > new_cost:
            # ... update the cost for this node.
            # обновить стоимость этого узла
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            # этот узел становится родителем для соседа
            parents[n] = node
    # Mark the node as processed.
    # Узел помечается как обработанный
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)