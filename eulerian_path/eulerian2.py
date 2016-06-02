# This is the second implementation of the eulerian tour algorithm. In this 
# version.

from collections import defaultdict


# We first reorganize the list of nodes into a hash of nodes, which point
# to a list of adjoining nodes. This is accomplished witht he make_graph_hash function.

def make_graph_hash(graph):

  edge_dict = defaultdict(list)

  for edge in graph:
    edge_dict[edge[0]].append(edge[1])
    edge_dict[edge[1]].append(edge[0])

  return edge_dict

# this function starts with the first node in the graph hash and follows the
# path until there are no steps left. Since visiting an edge can be bidirectional
# we need to remove the reference to the edge in the adjacent edge list.

def get_eulerian_path(graph):

  graph_hash = make_graph_hash(graph)
  path = [] 
  for node in graph_hash:
    if graph_hash[node]:
      path.append(node)
      next_node = graph_hash[node].pop()
      while graph_hash[next_node]:
        path.append(next_node)
        graph_hash[next_node].remove(node)
        if graph_hash[next_node]:
          node = next_node
          next_node = graph_hash[next_node].pop()
      else:
        break
  return path

# test cases

graph = [(1, 2), (2, 3), (3, 1)]
graph2 = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
graph3 = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9), (7, 14),  (10, 13)]

print get_eulerian_path(graph)
print get_eulerian_path(graph2)
print get_eulerian_path(graph3)






