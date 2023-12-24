p, T = 0, []
for _ in ' '*int(input()):
    a, b = input().split()
    b = int(b)
    if a == 'jinju':
        p = b
    T += b,
print(p)
print(sum(t > p for t in T))
