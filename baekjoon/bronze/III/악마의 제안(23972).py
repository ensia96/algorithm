k, n = map(int, input().split())
print([-(n*k//(1-n)), k+1][k == n]if n > 1 else -1)
