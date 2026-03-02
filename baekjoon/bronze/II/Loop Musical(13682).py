while '0' < input():
    *l, = map(int, input().split())
    print(sum((a < b) ^ (b < c)for a, b, c in zip(l, l[1:] + l, l[2:] + l)))
