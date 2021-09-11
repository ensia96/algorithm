n = int(input())
d = [int(input()) for _ in range(n)]
t = {i: d.count(i) for i in set(d)}
a = {i: [] for i in set(t.values())}
_ = [a[t[i]].append(i) for i in t]
b = a[max(a)]

print(sum(d)//n)
print(sorted(d)[n//2])
print(sorted(b)[1] if len(b) > 1 else b[0])
print(max(d)-min(d))
