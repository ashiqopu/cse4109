from collections import deque

parent = {}

def BFS(node, graph, source, destination):
    queue = deque()
    start = source
    visit = set()
    visit.add(start)
    queue.append(start)
    found = False
    while len(queue):
        now = queue.popleft()
        for i in range(len(graph[now])):
            nxt = graph[now][i-1]
            if nxt not in visit:
                visit.add(nxt)
                queue.append(nxt)
                parent[nxt] = now
                if nxt == destination:
                    print "Reached Destination"
                    found = True
                    break
                
        if found == True:
            break 

def print_shortest_path(source, destination):
    if destination==source:
        print destination,
    elif destination not in parent:
        print "No Path"
    else:
        print_shortest_path(source, parent[destination])
        print "-> ",destination,



node = 6
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E'] } # bi-directional edges

source = raw_input("Enter Source: ")
destination = raw_input("Enter destination: ")

BFS(node, graph, source, destination)
print_shortest_path(source, destination)
