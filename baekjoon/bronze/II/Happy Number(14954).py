n = int(input())
while (n != 1)*(n != 4):
    n = sum(i*i for i in map(int, f"{n}"))
print('UN'*(n > 1)+'HAPPY')
