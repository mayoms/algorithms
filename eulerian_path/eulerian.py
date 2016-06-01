def next_node(edge, pos):
  if pos in edge:
    return [x for x in edge if x != pos][0]
  else: 
    return pos
    
def find_leg(graph, start):
    
  path = [start]
  current = start

  while graph:
    edge = graph.pop(0)
    next = next_node(edge, current)
    if next != current:
      path.append(next)
      current = next
    elif next == start and len(path) > 0:
      graph.append(edge)
      break
    else:
      graph.append(edge)
  return path, graph
        

def find_eulerian_tour(graph):

  path = []
  while graph:
    leg, remainder = find_leg(graph, graph[-1][-1])
    if not path:
        path = leg
        continue
    hook = set(leg) & set(path)        
    pos = path.index(tuple(hook)[0])
    path = path[:pos+1] + leg[1:] + path[pos+1:]
         
  return path
            
graph = [(1, 2), (2, 3), (3, 1)]
graph2 = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
graph3 = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9), (7, 14),  (10, 13)]








print find_eulerian_tour(graph)
print find_eulerian_tour(graph2)
print find_eulerian_tour(graph3)
