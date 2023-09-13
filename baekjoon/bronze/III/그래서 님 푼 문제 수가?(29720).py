n, m, k = map(int, input().split())
t = n-m*k
print(max(0, t), t+m-1)
