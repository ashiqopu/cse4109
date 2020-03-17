from collections import deque

parent = {}

def DFS(node, graph, source, destination, d):
    depth = {}
    stack = deque()
    start = source
    visit = set()
    visit.add(start)
    depth[start] = 0
    stack.append(start)
    print stack
    found = False
    while len(stack):
        now = stack.pop()
        stack.append(now)
        cnt = 0
        if depth[now] == d:
            stack.pop()
            print stack
            continue
        for i in range(len(graph[now])):
            cnt += 1
            nxt = graph[now][i-1]
            if nxt not in visit:
                cnt -= 1
                parent[nxt] = now
                visit.add(nxt)
                stack.append(nxt)
                depth[nxt] = depth[now]+1
                print stack
                if nxt == destination:
                    print "Reached Destination"
                    found = True
                    break
                break
        if found == True:
            break
        if len(graph[now])==cnt:
            stack.pop()
            print stack

    return found
            

def print_path(source, destination):
    if destination==source:
        print destination,
    elif destination not in parent:
        print "No Path"
    else:
        print_path(source, parent[destination])
        print "-> ",destination,


node = 6
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E'] } # bi-directional edges

source = raw_input("Enter Source: ")
destination = raw_input("Enter destination: ")
maxDepth = input("Enter Depth: ")

for i in range(maxDepth+1):
    print "Depth: ",i
    reached = DFS(node, graph, source, destination, i)
    print_path(source, destination)
    print ""
    if reached == True:
        print "Max depth visited: ", i
        break
