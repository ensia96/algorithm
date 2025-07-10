n = int(input())
A = input()
for _ in ' '*n:
    x = y = ''
    for a in A+' ':
        if y == '' or y[-1] == a:
            y += a
        else:
            x += str(len(y))+y[-1]
            y = a
    A = x
print(A)
