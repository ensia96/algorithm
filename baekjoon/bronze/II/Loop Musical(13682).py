while '0' < input():
    l = *map(int, input().split()),
    print(sum((b > a) ^ (c > b)for a, b, c in zip(l[-1:] + l, l, l[1:] + l)))

