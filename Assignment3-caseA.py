def swap(a, p, q):
    a[p],a[q] = a[q], a[p]
    return a

def partition(a, q):
    # q is the POSITION of pivot not pivot
    p = a[q]
    i = q + 1
    for j in range(q + 1, len(a)):
        if a[j] < p:
            a = swap(a, i, j)
            i += 1
    a = swap(a, q, i - 1)
    return a, i - 1


def choosePivot(a, flag):
    if flag == 0:
        return 0

def QuickSort(a, flag):
    # base case
    if len(a) < 2:
        return a, 0
    else:
        p = choosePivot(a, 0)
        a, newPivotPos= partition(a, p)
        A = a[0:newPivotPos]
        B = a[newPivotPos + 1:]
        a[0:newPivotPos], left = QuickSort(A, flag)
        a[newPivotPos + 1:], right = QuickSort(B, flag)
        print('A is : ', A)
        print('B is : ', B)
    print('final array and (left, right)comparisons: ', a, left, right)
    return a, left+right + len(a) - 1

# a = [35, 50, 15, 25, 80, 20, 90, 45]
# print(QuickSort(a, 0))
with open('QuickSort.txt') as f:
    lines = [line.rstrip() for line in f]
a = list(map(int, lines))
print(QuickSort(a,0))
