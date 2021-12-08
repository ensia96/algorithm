g, n = lambda a, b: (a == 0)*b or g(b % a, a), input()
m, *l = map(int, input().split())
for x in l:
    y = g(m, x)
    print(f"{m//y}/{x//y}")
