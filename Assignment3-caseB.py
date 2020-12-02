#quicksort using last element of array as the pivot
def partition(A, l, r):
   piv = A[l];
   i = l+1
   for j in range(l+1, r):
     if A[j] <piv:
       A[j], A[i] = A[i], A[j]
       i = i+1
   A[l], A[i-1] = A[i-1], A[l] #swap pivot into rightful place
   return i
def quickSort(A, l, r):
   count = 0
   if l<r:
     A[l], A[r-1]= A[r-1], A[l]
     count = r-l-1
     split = partition(A,l,r)
     lc = quickSort(A,l,split-1) #during the for loop, this ends one before pivot
     rc = quickSort(A,split,r) #because the split is the lower bound, syntax of for loop makes it one after the pivot
     return count +lc +rc
   else:
     return 0
inFile = open("QuickSort.txt", 'r')
with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]
tot = quickSort(numList, 0, len(numList))
print(tot)