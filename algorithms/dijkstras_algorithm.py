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

