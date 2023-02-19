n, d = map(int, input().split())
A = [int(input())for _ in ' '*n]
x = d//sum(A)
for a in A:
    print(x*a)
