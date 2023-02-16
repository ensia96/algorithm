D = [0]*2
x, y = 'A', 'AB'
for i in input():
    if i in y:
        x = ord(i)-65
    else:
        D[x] += int(i)
    if (max(D) > 10)*(max(D)-min(D) > 1):
        exit(print(y[D[0] < D[1]]))
