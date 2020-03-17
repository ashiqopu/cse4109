import Queue
parent = {}

def Uniform_Cost_Search(node, graph, source, destination):
    pq = Queue.PriorityQueue()
    pq.put(source,0)
    cost_so_far = {}
    parent[source] = None
    cost_so_far[source] = 0

    while not pq.empty():
        now = pq.get()
        lst = []
        for i in range(len(graph[now])):
            tmp = graph[now][i]
            it = tmp.keys()[0]
            #print it
            lst.append( (it,cost_so_far[now] + tmp.values()[0]))
        print lst
        for i in range(len(lst)):
            nxt = lst[i][0]
            new_cost = lst[i][1]
            #print nxt
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost
                #print pq
                pq.put(nxt,priority)
                parent[nxt] = now
                

def print_shortest_path(source, destination):
    if destination==source:
        print destination,
    elif destination not in parent:
        print "No Path"
    else:
        print_shortest_path(source, parent[destination])
        print "-> ",destination,


## my_dict.keys()[0]

node = 6
graph = {'Arad': [{'Zerind':75},{'Timisoara':118},{'Sibiu':140}],
         'Bucharest': [{'Faragas':211},{'Pitesti':101},{'Giurgiu':90},{'Urziceni':85}],
         'Craiova': [{'Pitesti':138},{'Rimnicu Vilcea':146},{'Dobreta':120}],
         'Dobreta': [{'Craiova':120},{'Mehadia':75}],
         'Eforie': [{'Hirsova':86}],
         'Faragas': [{'Sibiu':99},{'Bucharest':211}],
         'Giurgiu': [{'Bucharest':90}],
         'Hirsova': [{'Eforie':86},{'Urziceni':98}],
         'Iasi': [{'Neamt':87},{'Vaslui':92}],
         'Lugoj': [{'Timisoara':111},{'Mehadia':70}],
         'Mehadia': [{'Lugoj':70},{'Dobreta':75}],
         'Neamt': [{'Iasi':87}],
         'Oradea': [{'Zerind':71},{'Sibiu':151}],
         'Pitesti': [{'Craiova':138},{'Rimnicu Vilcea':97},{'Bucharest':101}],
         'Rimnicu Vilcea': [{'Sibiu':80},{'Pitesti':97},{'Craiova':146}],
         'Sibiu': [{'Arad':140},{'Oradea':151},{'Faragas':99},{'Rimnicu Vilcea':80}],
         'Timisoara': [{'Arad':118},{'Lugoj':111}],
         'Urziceni': [{'Hirsova':98},{'Bucharest':85},{'Vaslui':142}],
         'Vaslui': [{'Iasi':92},{'Urziceni':142}],
         'Zerind': [{'Arad':75},{'Oradea':71}] } # bi-directional edges


source = raw_input("Enter Source: ")
destination = raw_input("Enter destination: ")

Uniform_Cost_Search(node, graph, source, destination)
print_shortest_path(source, destination)
