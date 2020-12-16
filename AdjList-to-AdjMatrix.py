########## Derive data and put in adjMatrix ####################
import numpy as np

arrays = [np.array(list(map(int, line.split()))) for line in open('sampleMinCut.txt')]
maxLen = arrays[len(arrays)-1][0]
edgeIndexList = []
def convert(adj, V):
    matrix = [[0 for j in range(V)]
              for i in range(V)]
    for i in range(V):
        for j in adj[i]:
            print(i,j)
            if (i+1) == j:
                matrix[i][j-1] = 0
            else:
                matrix[i][j-1] = 1
                edgeIndexList.extend([i,j-1])
            # j-1 so that when j is 200, we don't get list index out of range
    return matrix

# Remember that dimensions of matrix are 200,200 and index 0-199
adjmatrix = convert(arrays,maxLen)



print(adjmatrix[0:])

