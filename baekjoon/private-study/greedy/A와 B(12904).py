S = input()
T = input()
while len(S) < len(T):
    T = T[:-1]if T[-1] == 'A'else T[-2::-1]
print(+(S == T))
