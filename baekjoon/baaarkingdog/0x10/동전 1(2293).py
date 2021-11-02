n, k = map(int, input().split())
d = [1]+[0]*k
for _ in range(n):
    c = int(input())
    for i in range(1, k+1):
        d[i] += d[i-c]*(i >= c)
print(d[k])
