a, b = map(int, input().split())
for _ in ' '*int(input()):
    x = int(input())
    print(x, a*min(x, 1000)+b*max(x-1000, 0))
