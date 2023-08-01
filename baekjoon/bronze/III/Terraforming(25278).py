a, b, c = 'oxygen', 'ocean', 'temperature'
D = {a: 0, b: 0, c: 0}
for l in [*open(0)][1:]:
    x, y = l.split()
    D[x] += int(y)
print('not '*-~-((D[a] > 13)*(D[b] > 8)*(D[c] > 37))+'liveable')
