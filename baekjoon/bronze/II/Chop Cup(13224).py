p = 1
for i in input():
    if i == "A" and p != 3:
        p = 1 + (p == 1)
    if i == "B" and p != 1:
        p = 2 + (p == 2)
    if i == "C" and p != 2:
        p = 3 - 2 * (p == 3)
print(p)
