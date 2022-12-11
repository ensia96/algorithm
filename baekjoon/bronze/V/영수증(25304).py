x = int(input())
n = int(input())
for _ in ' '*n:
    a, b = map(int, input().split())
    x -= a*b
print('No'if x else'Yes')
