import sys
D = [0, 1, 3]
for _ in ' '*248:
    D += D[-1]+D[-2]*2,
for i in sys.stdin.readlines():
    print(D[int(i)])
