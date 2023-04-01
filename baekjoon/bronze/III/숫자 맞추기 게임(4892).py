*A, _ = open(0)
for i, j in enumerate(map(int, A)):
    x = (j//2*2)//2
    print(f'{i+1}.', 'eovdedn'[not x*3 % 2::2], x)
