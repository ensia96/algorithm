while (A := input()) != '0 0':
    n, m = map(int, A.split())
    A = [*map(int, input().split())]
    print(sorted([A[i]+A[j]for i in range(n)
          for j in range(i+1, n)if A[i]+A[j] <= m] or ['NONE'])[-1])
