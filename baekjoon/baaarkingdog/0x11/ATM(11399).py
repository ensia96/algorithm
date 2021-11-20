n = int(input())
d, l = [0]*n, sorted(map(int, input().split()))
for i in range(n):
    d[i] = d[i-1]+l[i]
print(sum(d))
