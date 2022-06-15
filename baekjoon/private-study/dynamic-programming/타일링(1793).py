import sys
D = [1, 1]
for _ in ' '*249:
    D += D[-1]+D[-2]*2,
for i in sys.stdin.readlines():
    print(D[int(i)])
