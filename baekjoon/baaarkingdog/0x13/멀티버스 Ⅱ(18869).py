m, n = map(int, input().split())
T = [(*map(lambda x:x[1], sorted(map(lambda x:x[::-1],
      enumerate(map(int, input().split()))))),)for _ in ' '*m]
print(sum(T[i] == T[j]for i in range(m)for j in range(i+1, m)))
