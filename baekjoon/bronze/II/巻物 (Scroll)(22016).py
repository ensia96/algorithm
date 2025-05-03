n, k = map(int, input().split())
A = input()
print(''.join([[A[i].upper(), A[i].lower()]
      [ord(A[i]) < 97], A[i]][i < k-1]for i in range(n)))
