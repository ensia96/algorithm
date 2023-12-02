n = int(input())
*A, = map(int, input().split())
s = sum(A)
print((max(s-a for a in A)if s % 2 else s)//2)
