n = int(input())
s = [int(input()) for _ in range(n)]
if n < 3:
    exit(print(sum(s)))
d = s[:3]
_ = [d.append(min(d[i-2], d[i-3])+s[i]) for i in range(3, n)]
print(sum(s)-min(d[-1], d[-2]))
