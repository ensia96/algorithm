from itertools import combinations as c
n = int(input())
s = [[*map(int, input().split())] for _ in range(n)]
b, r = map(set, c(range(n), n//2)), {*range(n)}

print(min(abs(sum(s[i][j] for i in c for j in c) -
      abs(sum(s[i][j] for i in r-c for j in r-c))) for c in b))
