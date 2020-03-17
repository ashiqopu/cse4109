from collections import deque

parent = {}

def BFS(node, graph, source, destination):
    sq = deque()
    dq = deque()
    svisit = set()
    dvisit = set()
    svisit.add(source)
    dvisit.add(destination)
    sq.append(source)
    dq.append(destination)
    found = False
    print sq
    print dq
    while sq or dq or (not found):
        snow = sq.popleft()
        for i in range(len(graph[snow])):
            snxt = graph[snow][i]
            if snxt not in svisit:
                svisit.add(snxt)
                sq.append(snxt)
                print sq
                parent[snxt] = snow
                if snxt == destination or snxt in dvisit:
                    print "Reached Destination"
                    found = True
                    break
                
        if found == True:
            break
        
        dnow = dq.popleft()
        for i in range(len(graph[dnow])):
            dnxt = graph[dnow][i]
            if dnxt not in dvisit:
                dvisit.add(dnxt)
                dq.append(dnxt)
                print dq
                parent[dnow] = dnxt
                if dnxt == source or dnxt in svisit:
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
         'C': ['A'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['E'] } # bi-directional edges

source = raw_input("Enter Source: ")
destination = raw_input("Enter destination: ")

BFS(node, graph, source, destination)
#print_shortest_path(source, destination)
