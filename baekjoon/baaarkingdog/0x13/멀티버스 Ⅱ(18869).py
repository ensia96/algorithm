import sys
m, n = map(int, input().split())
T = [(*map(lambda x:x[0], sorted(enumerate(map(int,
      sys.stdin.readline().split())), key=lambda x:x[1])),)for _ in ' '*m]
print(sum(T[i] == T[j]for i in range(m)for j in range(i+1, m)))
