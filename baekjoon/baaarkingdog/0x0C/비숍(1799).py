i, a = input, [0]*2
n = int(i())
m = [[*map(int, i().split())] for _ in range(n)]
e, f = [0] * (2*n-1), [0] * (2*n-1)


def t(x, y, c, o):
    if y >= n:
        x, y = x+1, y % 2 == 0
    if x >= n:
        a[o] = max(a[o], c)
        return
    if m[x][y] and not e[x+y] and not f[y-x+n-1]:
        e[x+y] = f[y-x+n-1] = 1
        t(x, y+2, c+1, o)
        e[x+y] = f[y-x+n-1] = 0
    t(x, y+2, c, o)


t(0, 0, 0, 0)
t(0, 1, 0, 1)

print(sum(a))

# 풀이 참고 : https://j2wooooo.tistory.com/80
