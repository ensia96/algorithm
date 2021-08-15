a, b, i = int(input()), 0, 1

while b + i < a:
    b += i
    i += 1

c = a - b
d = i + 1 - c

print(f"{c}/{d}" if i % 2 == 0 else f"{d}/{c}")
