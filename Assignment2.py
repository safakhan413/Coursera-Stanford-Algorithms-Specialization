
def mergeSortInversions(a):
    n = len(a)
    if n == 1:
        return a,0
    else:
        A = a[:len(a)//2]
        B = a[len(a)//2:]
        A, ai = mergeSortInversions(A)
        B, bi = mergeSortInversions(B)

        i, j = 0, 0
        inversion = 0 + ai +bi
        c = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                c.append(A[i])
                i = i +1
            else:
                c.append(B[j])
                j = j + 1
                inversion += (len(A) - i)
                #inversion: how many times do you interchange value to sort
    c += A[i:]
    c += B[j:]
    print(' \n A is: %s inver: %d \n B is: %s inver: %d \n C is: %s' % (A, ai, B, bi, c))
    print('inversion on this: %d' % (inversion))
    return c, inversion

# a = [6, 1, 3, 4]
with open('IntegerArray.txt') as f:
    lines = [line.rstrip() for line in f]
a = list(map(int, lines))
print(mergeSortInversions(a))
