x, y = map(float, input().split())
for _ in ' '*int(input()):
    n, N = input().split()
    print(eval(f'{n}/'+'y*x'[::1-2*(not ord(N)-65)]))
