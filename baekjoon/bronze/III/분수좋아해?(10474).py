for l in open(0):
    x, y = map(int, l.split())
    y and print(*divmod(x, y), f'/ {y}')
