x, y = {}, {}

for i, j in [map(int, input().split()) for i in range(3)]:
    if i not in x:
        x[i] = 0
    if j not in y:
        y[j] = 0
    x[i] += 1
    y[j] += 1

for i in x:
    if x[i] == 1:
        x = i
        break
for j in y:
    if y[j] == 1:
        y = j
        break

print(x, y)
