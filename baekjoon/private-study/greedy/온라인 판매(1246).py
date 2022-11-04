n, m = map(int, input().split())
print(*max(((j, j*min(m-i, n))for i, j in enumerate(sorted(int(input())
      for _ in ' '*m))), key=lambda x: (x[1], -x[0])))
