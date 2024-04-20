_, l = open(0)
x = y = 0
for i in range(len(l)-1):
    if l[i] == 'O':
        y += x+i+1
        x += 1
    else:
        x = 0
print(y)
