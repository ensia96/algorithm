n = int(input())
S = input()
C = S.count('C')
F = len(S)-C+1
print(C//F+bool(C % F)if F-1 else C)
