#
# ########### Random Contraction Algorithm ############################
# # While more than 2 vertices
# # pick a remaining edge (u,v) uniformly at random
# # merge (or contract) u and v into a single vertex
# # remove self loops
#
# # def kargerMinCut(adjmatrix, remainingVertices, rand):
# #     # while remainingVertices > 2:
# #         adjmatrix
# import re
# import random
# import itertools
#
#
# # Load the file into a graph represented by a dict of lists
# def load_graph():
#     g = {}
#
#     f = open('kargerMinCut.txt')
#     lines = f.readlines()
#     f.close()
#
#     lines = map(lambda s: re.sub('\s+', ' ', str(s.strip('\r\n'))).strip(), lines)
#     lines = map(lambda s: s.split(' '), lines)
#
#     for line in lines:
#         g[int(line[0])] = map(lambda s: int(s), line[1:])
#
#     return g
#
#
# # Contract an edge between 2 vertices
# def contract_edge(edge):
#     global g
#     # v1l = []
#     # merge v2 into v1 and remove v2 from graph
#     v1l = [g[edge[0]]]
#     # print('im global graph', g)
#     # print('im edge in contracting edge', edge[0])
#     # print('im v1l in contracting edge', v1l)
#
#     v1l.extend(g[edge[1]])
#     del g[edge[1]]
#
#     # replace all occurnces of v2 value with v1
#     for k, l in g.items():
#         g[k] = [edge[0] if x == edge[1] else x for x in g[k]]
#
#     # Remove all edges of v1 to itself(loops)
#     g[edge[0]] = [x for x in g[edge[0]] if x != edge[0]]
#
#
# # Gets a random edge available in the current graph
# def get_random_edge():
#     v1 = list(g.keys())[random.randint(0, len(g) - 1)]
#     # print('im v1', g.keys())
#     lenvList = list(g[v1])
#     # print('im v1', lenvList)
#     lenvLen = len(lenvList) - 1 if len(lenvList) > 1 else 0
#     print('im v2 len', lenvLen)
#     print('im v2 list', lenvList)
#     randomGen = random.randint(0, lenvLen)
#     print('im randomgen', randomGen)
#     v2 = lenvList[randomGen]
#     return (v1, v2)
#
#
# minlist = []
#
# # Repeat 10 times to get a minimum
# for i in range(0, 20):
#     g = load_graph()
#
#     # Keep contracting the graph until we have 2 vertices
#     while (len(g) > 2):
#         contract_edge(get_random_edge())
#     print('########## im min list##', g[g.keys()[0]])
#     minlist.append(len(g[g.keys()[0]]))
#
# print
# min(minlist)

from random import choice
from copy import deepcopy

def contract(graph):
    u = choice(list(graph.keys()))
    v = choice(graph[u])
    new_key = u+"-"+v
    graph[new_key] = graph[u] + graph[v]
    del graph[u]
    del graph[v]
    for key in graph.keys():
        copy = graph[key][:]
        if new_key == key:
            for item in copy:
                if item == u or item == v:
                    graph[key].remove(item)
        else:
            for item in copy:
                if item == u or item == v:
                    graph[key].remove(item)
                    graph[key].append(new_key)


def min_cut(graph):
    n = len(graph)
    minimum = n*(n-1)//2
    for i in range(n):
        copy =  deepcopy(graph)
        while len(copy) > 2:
            contract(copy)
            minimum = min(minimum , len(list(copy.values())[0]))
    return minimum


graph = {}
with open('kargerMinCut.txt') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(str,line.split('\t')[:-1]))
        graph[str(elements[0])] = elements[1:]
f.close()
print(min_cut(graph))