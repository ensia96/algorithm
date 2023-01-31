x, y, z = 'a', '*', 'ptr'
print('int a;')
for i in range(int(input())):
    print(f"int *{y*i}{z} = &{x};")
    x, z = z, z[:3]+f'{i+2}'
