n, k = map(int, input().split())
A = input()
print(''.join([A[i].swapcase(), A[i]][i < k-1]for i in range(n)))
