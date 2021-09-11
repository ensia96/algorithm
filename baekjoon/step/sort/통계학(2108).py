import collections as c
n = int(input())
b = sorted([int(input()) for _ in range(n)])
a = c.Counter(b).most_common()

print(sum(b)//n)
print(b[len(b)//2])
print(a[1][0] if len(a) > 1 and a[0][1] == a[1][1] else a[0][0])
print(max(b)-min(b))
