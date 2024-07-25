a, b = 1, 0
for i in range(int(input())):
    if a == 1:
        a = b + 1
        b = 1
    else:
        a -= 1
        b += 1
print(a, b)
