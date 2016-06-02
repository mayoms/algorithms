# This is the second implementation of the eulerian tour algorithm. In this 
# version we use a hash to represent the graph, rather than a list of paired tuples.
# This version takes on average 25-35% of the steps in my first solution, for example
# the test graph3 has 861 evaluated statements at completion, where as this
# implementation has 230 statements executed at completion. I don't yet have any 
# large test cases to do more thorough testing, though.

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

def find_leg(graph_hash):
  
  path = []
  
  node = graph_hash.keys()[0]
  path.append(node)
  next_node = graph_hash[node].pop()

  while graph_hash[next_node]:
    path.append(next_node)
    graph_hash[next_node].remove(node)
    if graph_hash[next_node]:
      node = next_node
      next_node = graph_hash[next_node].pop()

  graph_hash = dict((k, v) for k, v in graph_hash.iteritems() if v)
  return path, graph_hash

def find_eulerian_tour(graph):

  path = []
  while graph:
    leg, graph  = find_leg(graph)
    if not path:
        path = leg
        continue
    if leg[0] in path:
      hook = leg[0]
    else:
      hook = tuple(set(leg) & set(path))[0]
      leg_pos = leg.index(hook)
      leg = leg[leg_pos:] + leg[1:leg_pos+1]
    path_pos = path.index(hook)
    path = path[:path_pos] + leg + path[path_pos+1:]
         
  return path

# test cases

graph = [(1, 2), (2, 3), (3, 1)]
graph2 = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
graph3 = [(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9), (7, 14),  (10, 13), (1, 13), (1, 6), (6, 11), (3, 13)]
graph4 = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]


graph = make_graph_hash(graph)
graph2 = make_graph_hash(graph2)
graph3 = make_graph_hash(graph3)
graph4 = make_graph_hash(graph4)

print find_eulerian_tour(graph)
print find_eulerian_tour(graph2)
print find_eulerian_tour(graph3)
print find_eulerian_tour(graph4)






