x = y = z = 0
for i in input():
    z += i.isupper()
    if i.lower() in "qwertyasdfgzxcvb":
        x += 1
    elif " " == i:
        z += 1
    else:
        y += 1
for _ in " " * z:
    if x > y:
        y += 1
    else:
        x += 1
print(x, y)
