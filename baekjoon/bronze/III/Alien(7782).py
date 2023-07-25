n = int(input())
x, y = map(int, input().split())
for _ in ' '*n:
    a, b, c, d = map(int, input().split())
    a <= x <= c and b <= y <= d and exit(print('Yes'))
print('No')
