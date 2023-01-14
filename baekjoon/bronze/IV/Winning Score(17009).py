a, b, c = int(input()), int(input()), int(input())
x, y, z = int(input()), int(input()), int(input())
A = 3*(a-x)+2*(b-y)+c-z
print('A'if A > 0 else 'B'if A < 0 else 'T')
