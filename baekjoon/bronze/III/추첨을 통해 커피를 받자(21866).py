*A, = map(int, input().split())
for i in range(9):
    -~(i//2)*100 < A[i] and exit(print('hacker'))
print('ndornaew'[sum(A) > 99::2])
