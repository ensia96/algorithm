n = int(input())
s, d = [0]*305, [0]*305
for i in range(1, n+1):
    s[i] = int(input())
if n <= 2:
    exit(print(sum(s)))
d[1] = s[1]
d[2] = s[2]
d[3] = s[3]
for i in range(4, n):
    d[i] = min(d[i-2], d[i-3])+s[i]
print(sum(s)-min(d[n-1], d[n-2]))
