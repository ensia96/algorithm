n = int(input())
s = [int(input()) for _ in range(n)]
if n == 1:
    exit(print(s.pop()))
d = [(s[0], 0), (s[1], s[0]+s[1])]
_ = [d.append((max(d[i-2])+s[i], d[i-1][0]+s[i])) for i in range(2, n)]
print(max(d[n-1]))
