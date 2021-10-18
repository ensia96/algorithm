n, r = int(input()), range
b = [[*map(int, input().split())]for _ in r(n)]
y = x = n//2
p = [(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1),
     (0, -2, 5), (1, -1, 10), (1, 0, 7), (1, 1, 1), (2, 0, 2)]
a = sum(map(sum, b))


def f(d):
    global y, x, b
    for _ in r(d):
        x -= 1
        a, b[y][x], t = b[y][x], 0, 0
        for v, h, c in p:
            i, j, u = y+v, x+h, int(a*c/100*10//10)
            t += u
            if (0 <= i < n)*(0 <= j < n):
                b[i][j] += u
        b[y][x-1] = b[y][x-1]+(a-t)*(0 < x)
    y, x, b = x, n-y-1, [*map(list, zip(*b[::-1]))]


_ = [f(i)for i in r(1, n) for _ in r(2+(i == n-1))]
print(a-sum(map(sum, b)))
