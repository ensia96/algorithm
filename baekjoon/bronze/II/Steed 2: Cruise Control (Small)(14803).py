def I(): return map(int, input().split())


for i in range(*I()):
    d, n = I()
    print(f'Case #{i+1}:', min(s*d/(d-k)for k, s in [I()for _ in ' '*n]))
