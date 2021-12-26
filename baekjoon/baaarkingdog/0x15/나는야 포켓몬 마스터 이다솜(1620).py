n, m, P = *map(int, input().split()), {}
for i in range(n):
    N = input()
    P[N], P[str(i+1)] = i+1, N
for _ in ' '*m:
    print(P[input()])
