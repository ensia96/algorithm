C = [0]*12
for l in [*open(0)][1:]:
    C[int(l.split('/')[1])-1] += 1
for i in range(12):
    print(i+1, C[i])
