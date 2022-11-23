n = int(input())
S = C = 0
for i in map(int, input().split()):
    S += i
    C += i//2
print('YNEOS'[S % 3 or C < S//3::2])
