f = lambda: [*map(int, input().split())]
while sum(A := f()):
    n, w, l, h, a, m = A
    print(-((2 * (h * w + l * h) + l * w - sum(eval(input().replace(*' *'))
          for _ in '_' * m)) * n // -a))
