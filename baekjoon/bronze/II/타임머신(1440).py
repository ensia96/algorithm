h, m, s = map(int, input().split(":"))
f, g = lambda x: 0 < x < 13, lambda x: x < 60
print(
    bool(h + m + s)
    * (2 * f(h) * g(m) * g(s) + 2 * f(m) * g(h) * g(s) + 2 * f(s) * g(h) * g(m))
)
