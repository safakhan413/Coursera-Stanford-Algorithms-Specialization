
########### Random Contraction Algorithm ############################
# While more than 2 vertices
# pick a remaining edge (u,v) uniformly at random
# merge (or contract) u and v into a single vertex
# remove self loops

# def kargerMinCut(adjmatrix, remainingVertices, rand):
#     # while remainingVertices > 2:
#         adjmatrix
import random
from random import randint

#loading data from the text file#
with open('sampleMinCut.txt') as req_file:
    mincut_data = []
    for line in req_file:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            mincut_data.append(line)
print('im min cut data', mincut_data)
#extracting edges from the data #
edgelist = []
nodelist = []
for every_list in mincut_data:
    print('im everylist', every_list[0])
    nodelist.append(every_list[0])
    temp_list = []
    for temp in range(1,len(every_list)):
        temp_list = [every_list[0], every_list[temp]]
        flag = 0
        print('im edge_list', edgelist)

        for ad in edgelist:
            if set(ad) == set(temp_list):
                print('im ad', ad)

                flag = 1
        if flag == 0 :
            edgelist.append([every_list[0],every_list[temp]])


#karger min cut algorithm#
while(len(nodelist) > 2):
    val = randint(0,(len(edgelist)-1))
    print(val)
    target_edge = edgelist[val] # pick random edge
    replace_with = target_edge[0]
    should_replace = target_edge[1]
    for edge in edgelist:
        if(edge[0] == should_replace):
            edge[0] = replace_with
        if(edge[1] == should_replace):
            edge[1] = replace_with
    edgelist.remove(target_edge)
    nodelist.remove(should_replace)
    for edge in edgelist:
        if edge[0] == edge[1]:
            edgelist.remove(edge)

print ('edgelist remaining: ',edgelist)
print ('nodelist remaining: ',nodelist)