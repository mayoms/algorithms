# This is my first solution for finding a eulerian tour. The input is a list of edges
# represented as paired tuples e.g. (1,2). It is assumed that the list contains
# a complete tour, so no testing is done to verify criteria.


# A helper fuction that finds the next node, takes 2 parameters, an edge (pair of nodes)
# to evaluate, and the current node position. If the current position is part of the node
# it returns the next position in the graph, otherwise returns the current node.

def next_node(edge, pos):
  if pos in edge:
    return [x for x in edge if x != pos][0]
  else: 
    return pos
    

# A valid path consists of at least one circuit that terminates at the starting
# node. This function takes two parameters, a graph in the form of a list of edges
# and the starting node. It traverses the graph until the starting node is encountered
# and then returns the completed 'leg', as well as the remaining unvisited edges.

def find_leg(graph, start):
    
  path = [start]
  current = start

  while graph:
    edge = graph.pop(0)
    next = next_node(edge, current)
    if next != current:
      path.append(next)
      current = next
    elif next == start and len(path) > 1:
      graph.append(edge)
      break
    else:
      graph.append(edge)
  return path, graph
        
# this is the organizing function - it takes the graph as its input and 
# then using the find_leg function, finds valid circuits within the graph.
# If there is more than one circuit in the path, the subsequent nodes 
# are circular, so we grab the first point where the circuits can be joined
# and shift the leg so it can be inserted at the correct spot in the existing path.

def find_eulerian_tour(graph):

  path = []
  while graph:
    leg, graph = find_leg(graph, graph[-1][-1])
    if not path:
        path = leg
        continue
    hook = tuple(set(leg) & set(path))[0]
    if hook != leg[0]:
      leg_pos = leg.index(hook)
      leg = leg[leg_pos:] + leg[1:leg_pos+1]
    path_pos = path.index(hook)
    path = path[:path_pos] + leg + path[path_pos+1:]
         
  return path

# Test Cases
            
graph = [(1, 2), (2, 3), (3, 1)]
graph2 = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
graph3 = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9), (7, 14),  (10, 13)]
graph4 = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]

print find_eulerian_tour(graph)
print find_eulerian_tour(graph2)
print find_eulerian_tour(graph3)
print find_eulerian_tour(graph4)
