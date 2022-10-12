f, c = lambda: sorted(map(int, input().split()))[::-1], 0
_, A, _, B = input(), f(), input(), f()
max(B) > max(A) and exit(print(-1))
while B:
    for a in A:
        for b in B:
            if a >= b:
                B.remove(b)
                break
    c += 1
print(c)
