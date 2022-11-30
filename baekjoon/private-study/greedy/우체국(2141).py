n = int(input())
A = sorted([*map(int, input().split())]for _ in ' '*n)
t = ~-sum(a for _, a in A)//2
c = 0
for x, y in A:
    c += y
    c > t and exit(print(x))
