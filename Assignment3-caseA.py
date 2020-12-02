def swap(a, p, q):
    a[p],a[q] = a[q], a[p]
    return a

def partition(a, l, r):
    # l is the POSITION of pivot not pivot
    p = a[l]
    i = l + 1
    print('val of p, l, r: ', p,l,r)
    for j in range(l+1, r):
        print('j is: ', j)
        if a[j] < p:
            a = swap(a, i, j)
            i += 1
    a = swap(a, l, i - 1)
    return a, i - 1

def choosePivot_left_right(a, flag):
    if flag == 0:
        return 0, len(a)
    if flag == 1:
        return len(a)-1,0

def QuickSort(a, flag):
    # base case
    if len(a) < 2:
        return a, 0
    else:
        print('full array is: ', a)
        l,r = choosePivot_left_right(a, flag) #case 1
        # l,r = choosePivot_left_right(a, flag) #case 2
        print('pivot is: ', a[l])
        # print('left and right is: ', l, r)
        a, newPivotPos= partition(a,l,r)
        A = a[0:newPivotPos]
        B = a[newPivotPos + 1:]
        print('A is : ', A)
        print('B is : ', B)
        a[0:newPivotPos], left = QuickSort(A, flag)
        a[newPivotPos + 1:], right = QuickSort(B, flag)
        # left = QuickSort(A, flag)
        # right = QuickSort(B, flag)

    print('final array and (left, right)comparisons: ', a, left, right)
    return a, left+right + len(a) - 1

a = [35, 50, 15, 25, 80, 20, 90, 45]
print(QuickSort(a, 0))
# with open('QuickSort.txt') as f:
#     lines = [line.rstrip() for line in f]
# a = list(map(int, lines))
# print(QuickSort(a,0))
# case 1: 162085
