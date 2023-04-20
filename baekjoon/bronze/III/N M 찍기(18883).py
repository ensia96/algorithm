x, y = map(int, input().split())
for i in range(x):
    print(*[i*y+j+1 for j in range(y)])
