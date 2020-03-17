from collections import deque
import operator
parent = {}

def Greedy_Best_First(node, graph, cost, source, destination):
    queue = deque()
    start = source
    visit = set()
    visit.add(start)
    queue.append(start)
    found = False
    while len(queue):
        now = queue.popleft()
        lst = {}
        for i in range(len(graph[now])):
            it = graph[now][i]
            #print it
            lst[it] = cost[it]
        #print lst
        sorted_lst = sorted(lst.iteritems(), key=operator.itemgetter(1))
        #print sorted_lst
        for i in range(len(sorted_lst)):
            nxt = sorted_lst[i][0]
            #print nxt
            if nxt not in visit:
                visit.add(nxt)
                queue.append(nxt)
                print queue
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
graph = {'Arad': ['Zerind','Timisoara','Sibiu'],
         'Bucharest': ['Faragas','Pitesti','Giurgiu','Urziceni'],
         'Craiova': ['Pitesti','Rimnicu Vilcea','Dobreta'],
         'Dobreta': ['Craiova','Mehadia'],
         'Eforie': ['Hirsova'],
         'Faragas': ['Sibiu','Bucharest'],
         'Giurgiu': ['Bucharest'],
         'Hirsova': ['Eforie','Urziceni'],
         'Iasi': ['Neamt','Vaslui'],
         'Lugoj': ['Timisoara','Mehadia'],
         'Mehadia': ['Lugoj','Dobreta'],
         'Neamt': ['Iasi'],
         'Oradea': ['Zerind','Sibiu'],
         'Pitesti': ['Craiova','Rimnicu Vilcea','Bucharest'],
         'Rimnicu Vilcea': ['Sibiu','Pitesti','Craiova'],
         'Sibiu': ['Arad','Oradea','Faragas','Rimnicu Vilcea'],
         'Timisoara': ['Arad','Lugoj'],
         'Urziceni': ['Hirsova','Bucharest','Vaslui'],
         'Vaslui': ['Iasi','Urziceni'],
         'Zerind': ['Arad','Oradea'] } # bi-directional edges

cost = {'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Dobreta': 242,
        'Eforie': 161,
        'Faragas': 176,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 10,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374 }

source = raw_input("Enter Source: ")
destination = raw_input("Enter destination: ")

Greedy_Best_First(node, graph, cost, source, destination)
print_shortest_path(source, destination)
