# quicksort using median of three as pivot
def partition(A, l, r):
    piv = A[l];
    i = l + 1
    for j in range(l + 1, r):
        if A[j] < piv:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[l], A[i - 1] = A[i - 1], A[l]  # swap pivot into rightful place
    return i


def isMedian(a, b, c):
    if (a <= b and b <= c) or (a >= b and b >= c):
        return True


def quickSort(A, l, r):
    count = 0
    if l < r:
        mid = l + (r - l + 1) / 2 - 1  # find out middle element
        if isMedian(A[l], A[mid], A[r - 1]):
            A[l], A[mid] = A[mid], A[l]  # switch middle (if it is median) to be the first element and use as pivot
        elif isMedian(A[l], A[r - 1], A[mid]):
            A[l], A[r - 1] = A[r - 1], A[l]  # switch last (if it is median) to be first element and use as pivot
        count = r - l - 1
        split = partition(A, l, r)
        lc = quickSort(A, l, split - 1)  # during the for loop, this ends one before pivot
        rc = quickSort(A, split,
                       r)  # because the split is the lower bound, syntax of for loop makes it one after the pivot
        return count + lc + rc
    else:
        return 0


NUMLIST_FILENAME = "QuickSort.txt"
inFile = open(NUMLIST_FILENAME, 'r')
with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]
# numList = [line.rstrip() for line in open('integerArray.txt')]
tot = quickSort(numList, 0, len(numList))
print(tot)
