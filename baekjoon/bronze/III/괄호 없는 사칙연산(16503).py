a, x, b, y, c = input().split()
a, b, c = map(int, [a, b, c])


def f(a, b, op): return a+b if op == '+'else a-b if op == '-'else a * \
    b if op == '*'else -1*(abs(a)//abs(b))if a*b < 0 else a//b


print(*sorted([f(f(a, b, x), c, y), f(a, f(b, c, y), x)]))
