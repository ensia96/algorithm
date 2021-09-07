n, k = map(int, input().split())
D = [0]+[10001]*k
for _ in range(n):
    c = int(input())
    for i in range(c, k+1):
        D[i] = min(D[i], D[i-c]+1)
a = D[k]
print([a, -1][a == 10001])
