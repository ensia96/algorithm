n, q, *A = map(int, open(0).read().split())
t = [*("SciComLove" * 8**5)[:n]]
x = sum(map(str.isupper, t))
for a in A:
    t[a - 1] = t[a - 1].swapcase()
    print(x := x + (t[a - 1].isupper() * 2 - 1))
