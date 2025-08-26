f, i = lambda: map(int, input().split()), 0
for _ in ' '*int(*f()):
    n, p, q = f()
    w = 0
    i += 1
    print(f"Case {i}:", min(p, sum([q >= (w := w+a)for a in sorted(f())])))
