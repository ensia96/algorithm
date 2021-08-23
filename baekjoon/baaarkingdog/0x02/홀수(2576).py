l = [*filter(lambda x: x % 2, map(int, [*open(0)]))]

if l:
    print(sum(l))
    print(min(l))
else:
    print(-1)
