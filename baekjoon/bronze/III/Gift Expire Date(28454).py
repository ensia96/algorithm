y, m, d = map(int, input().split('-'))
t = 0
for _ in ' '*int(input()):
    a, b, c = map(int, input().split('-'))
    t += a > y or b > m or (b == m and c >= d)
print(t)
