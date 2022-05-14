n = int(input())
A = [*map(int, input().split())]
r = 1
for a in A:
    r += a
    r % 7 == 5 and exit(print('YES'))
print('NO')
