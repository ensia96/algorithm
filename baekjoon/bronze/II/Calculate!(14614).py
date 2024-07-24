a, b, c = map(int, input().split())
for _ in c % 2 * " ":
    a ^= b
print(a)
