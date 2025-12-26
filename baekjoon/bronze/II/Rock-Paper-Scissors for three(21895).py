_, A, B = open(0)
D = {'R': 'P', 'S': 'R', 'P': 'S'}
for a, b in zip(A[:-1], B):
    print(D[[a, b][a == D[b]]], end='')
