#
# ########### Random Contraction Algorithm ############################
# # While more than 2 vertices
# # pick a remaining edge (u,v) uniformly at random
# # merge (or contract) u and v into a single vertex
# # remove self loops
from random import choice #Use random.choice() to Randomly select an item from a list
from copy import deepcopy

def contract(graph):
    u = choice(list(graph.keys()))
    v = choice(graph[u])
    new_key = u+"-"+v # e.g. '18-34-149-156-7-76-121-166-22-131-122-27'
    graph[new_key] = graph[u] + graph[v] # combine the graph of both vertices by just appending edges against e.g. 39-27
    del graph[u]
    del graph[v]
    for key in graph.keys():
        copy = graph[key][:]
        if new_key == key:
            for item in copy:
                if item == u or item == v: # removing self loops
                    graph[key].remove(item)
        else:
            for item in copy:
                if item == u or item == v:
                    graph[key].remove(item)
                    graph[key].append(new_key) # replace edges of v with vertices of both v-u


def min_cut(graph):
    n = len(graph)
    minimum = n*(n-1)//2
    for i in range(n):
        copy =  deepcopy(graph)
        while len(copy) > 2:
            contract(copy) # contrcted graph vertices look like ['97', '100', '91', '20', '69', '198', '196', '57-191']]
            # print('cop vals',list(copy.values())[0])
            minimum = min(minimum , len(list(copy.values())[0]))
    return minimum


graph = {}
with open('kargerMinCut.txt') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(str,line.split('\t')[:-1])) ## Read all the data. Multiple ways of doing that. Check adjList to adjMatrix
        graph[str(elements[0])] = elements[1:] # represent graph as dictionary
f.close()
print(min_cut(graph))