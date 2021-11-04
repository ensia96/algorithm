N = int(input())
n, f = abs(N), N >= 0
d = [0, 1][::f or -1]
for i in range(2, n+2-f):
    v = [d[i-2]-d[i-1], d[i-1]+d[i-2]][f]
    d += [[v % 1000000000, -(-v % 1000000000)][v < 0]]
v = d[n and -1]
print(int(v > 0 or (v < 0)*-1))
print(abs(v))
