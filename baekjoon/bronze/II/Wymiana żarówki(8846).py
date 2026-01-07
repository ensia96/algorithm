M = 500000009
a = b = 1
for _ in '_' * ~-int(input()):
    b = b * 4 % M
    a = (a + b) % M
print(a)
