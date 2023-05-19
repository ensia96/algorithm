n = int(input())
x = '@'*n
y, z = [x*5]*n, [x]*n
print('\n'.join(y+z+y+z+z))
