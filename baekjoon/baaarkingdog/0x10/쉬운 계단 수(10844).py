n = int(input())
d = [[0]+[1]*9]+[[] for _ in range(n-1)]
_ = [d[i].append((d[i-1][j-1] + d[i-1][j+1] if 0 < j < 9 else d[i-1]
                 [[8, 1][not j]]) % 10**9) for i in range(1, n) for j in range(10)]
print(sum(d[n-1]))
