import collections as C
n = int(input())
l = [*map(int, input().split())]
D = [8**7]*(n+1)
for i in range(n):
    c = l[i]
    D[c] = min(D[c-1], i)
print(n-C.Counter(D).most_common()[0][1])
