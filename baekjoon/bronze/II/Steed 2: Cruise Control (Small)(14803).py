I = input
for i in range(int(I())):
    d, n = map(int, I().split())
    print(f'Case #{i+1}:', min(s*d/(d-k)
          for k, s in [map(int, I().split())for _ in ' '*n]))
