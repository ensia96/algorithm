n, q, *A = map(int, open(0).read().split())
t = [*("SciComLove" * 8**5)[:n]]
for a in A:
    t[a - 1] = t[a - 1].swapcase()
    print(sum(map(str.isupper, t)))
