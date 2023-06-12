from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    a, b, c, x, y, z = map(int, input().split())
    print(c+z+abs(x-a)+abs(y-b))
