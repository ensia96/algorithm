x, y, z = map(int, input().split())
n = int(input())
D = [0]*20
for _ in ' '*n:
    a, b = map(int, input().split())
    D[a] = b
w = r = 0
for i in range(19, -1, -1):
    w <<= 3
    t = min(D[i], (x >> i)*(y >> i)*(z >> i)-w)
    w += t
    r += t
print(-1 if x*y*z-w else r)
