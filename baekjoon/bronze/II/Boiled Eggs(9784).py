f = lambda: map(int, input().split())
for i in range(*f()):
    n, p, q = f()
    w = 0
    print(f"Case {i + 1}:",
          min(p, sum([q >= (w := w + a)for a in sorted(f())])))
