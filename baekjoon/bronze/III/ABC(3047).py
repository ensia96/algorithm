A = sorted(map(int, input().split()))
print(*[A[ord(i)-65]for i in input()])
