r, f = range, lambda: [*map(int, input().split())]
for i in r(*f()):
    f()
    A = f()
    T = [*zip(A[::2], A[1::2])]
    print(f"Case #{i + 1}:", *[sum(a <= c <= b for a, b in T)
          for c in [f()[0]for _ in r(*f())]])
    f()
