n, m = map(int, input().split())
P = [0]+[input()for _ in ' '*n]
N = {P[i]: i for i in range(n+1)}
for _ in ' '*m:
    q = input()
    print(P[int(q)]if q.isdigit()else N[q])
