f, g = lambda: map(int, input().split()), lambda x: f"Case #{x}:"
for i in range(int(input())):
    m, n, p = f()
    A = [*zip(*[[*f()]for _ in ' '*m])]
    print(g(i+1), sum(max(A[i])-A[i][p-1]for i in range(n)))
