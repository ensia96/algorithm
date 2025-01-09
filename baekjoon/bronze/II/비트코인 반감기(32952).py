r, k, m = map(int, input().split())
for i in range(m // k):
    r //= 2
print(r)
