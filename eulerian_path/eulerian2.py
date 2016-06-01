from collections import defaultdict

def make_graph_hash(graph):

  edge_dict = defaultdict(list)

  for edge in graph:
    edge_dict[edge[0]].append(edge[1])
    edge_dict[edge[1]].append(edge[0])

  return edge_dict

def get_eulerian_path(graph):

  graph_hash = make_graph_hash(graph)

  keys = list(graph_hash)
  path = []
  
  for key in keys:                  
    if graph_hash[key]:
      path.append(key)
      current = graph_hash[key].pop()
    if not graph_hash[current]:
        break
    while True:
      path.append(current)
      if key in graph_hash[current]:
          graph_hash[current].remove(key)
      if graph_hash[current]:
        next = graph_hash[current].pop()
        key = current
        current = next
      else:
        break

  return path

graph = [(1, 2), (2, 3), (3, 1)]
graph2 = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
graph3 = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9), (7, 14),  (10, 13)]

print get_eulerian_path(graph)
print get_eulerian_path(graph2)
print get_eulerian_path(graph3)






