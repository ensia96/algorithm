a, c = 1, 0
for i in range(int(input())):
    a *= i+1
while 1:
    if a % 10:
        exit(print(c))
    a, c = a//10, c+1
