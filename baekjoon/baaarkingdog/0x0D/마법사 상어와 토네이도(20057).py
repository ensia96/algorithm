n, r = int(input()), range
b = [[*map(int, input().split())]for _ in r(n)]
y = x = n//2
p = [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [
    5, 0, 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]
a, k, l = sum(map(sum, b)), [(0, -1), (1, 0), (0, 1), (-1, 0)], 0


def f(d):
    global y, x, p, l
    for _ in r(d):
        e, g = k[l]
        y, x = y+e, x+g
        a, b[y][x], t = b[y][x], 0, 0
        for m in r(5*5):
            i, j = m//5, m % 5
            v, h, u = y+i-2, x+j-2, int(a*p[i][j]/100*10//10)
            t += u
            if (0 <= v < n)*(0 <= h < n):
                b[v][h] += u
        if (0 <= y+e < n)*(0 <= x+g < n):
            b[y+e][x+g] += (a-t)
    p, l = [*map(list, zip(*p))][::-1], (l+1) % 4


_ = [f(i)for i in r(1, n)for _ in r(2+(i == n-1))]
print(a-sum(map(sum, b)))
