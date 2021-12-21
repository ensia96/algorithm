n, k = map(int, input().split())
S = [*map(int, input().split())]
a = c = j = 0
for i in range(n):
    while j < n and c <= k:
        c, j = c+(S[j] % 2), j+1
    a, c = max(a, j-i-c), c-(S[i] % 2)
print(a)
