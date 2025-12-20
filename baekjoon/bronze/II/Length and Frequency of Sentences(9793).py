_, *L = open(0)
S = [0] * 76
for l in L:
    S[len(l.split())] += 1
for i in range(76):
    S[i] > 0 == print(i, S[i])
