I = input
print('NTIAEK'[not {*range(1, int(I()) + 1)} - {*map(int, I().split())}::2])
