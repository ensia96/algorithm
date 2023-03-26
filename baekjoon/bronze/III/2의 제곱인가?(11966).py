n, x = int(input()), 0
while n*(not x):
    n, x = divmod(n, 2)
print('01'[n < 1])
