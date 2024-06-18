n = int(input())
i = 0
while n >= i:
    i = i*10+1
print(max(1, len(str(i))-1))
