D = [1, 1, 5, 11]
for _ in ' '*18:
    D += D[-1]+5*D[-2]+D[-3]-D[-4],
for _ in ' '*int(input()):
    print(D[int(input())])
