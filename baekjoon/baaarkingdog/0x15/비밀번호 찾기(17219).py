import sys
I, T = sys.stdin.readline, {}
n, m = map(int, I().split())
for _ in ' '*n:
    a, p = I().split()
    T[a] = p
for _ in ' '*m:
    print(T[I().strip()])
