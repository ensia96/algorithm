r, c = map(int, input().split())
B = [[*input()]for _ in ' '*r]


def f(x, y):
    if y == c-1:
        return 1
    for i in [-1, 0, 1]:
        if 0 <= x+i < r and y+1 < c and B[x+i][y+1] == '.':
            B[x+i][y+1] = 'x'
            if f(x+i, y+1):
                return 1
    return 0


print(sum(f(i, 0)for i in range(r)))
