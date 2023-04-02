a, b, c = sorted(map(int, input().split()))
x, y = b-a, c-b
print([c+y, a+y, b+x][(x > y)+2*(x < y)])
