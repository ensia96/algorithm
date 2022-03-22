def sol(a):
    for i in range(a // 5 + 1, -1, -1):
        for j in range(a // 3 + 1):
            if (5 * i) + (3 * j) == a:
                return i + j
    return -1


print(sol(int(input())))
