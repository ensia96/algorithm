n = int(input())
d = [int(input()) for _ in range(n)]
t, m = {}, 0

for i in set(d):
    a = d.count(i)
    t[a] = t.get(a, [])
    t[a] += [i]
    m = max(a, m)

print(sum(d)//n)
print(sorted(d)[n//2])
print(sorted(t[m])[len(t[m]) > 1])
print(max(d)-min(d))
