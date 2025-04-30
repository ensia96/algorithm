a, b = input().split()
for i in range(int(a)+1, 63):
    if str(2**i)[0] == b:
        exit(print(i))
print(0)
