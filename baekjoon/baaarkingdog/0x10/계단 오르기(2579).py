n = int(input())
s = [0] + [int(input()) for _ in range(n)]
if n <= 2:
    exit(print(sum(s)))
d = s[:4]
_ = [d.append(min(d[i-2], d[i-3])+s[i]) for i in range(4, n)]
print(sum(s)-min(d[n-1], d[n-2]))
