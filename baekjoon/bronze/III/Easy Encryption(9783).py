A = ''
for i in input():
    t = ord(i)
    A += [[[i, f'#{i}'][i.isdigit()], f'{t-96:02d}'][i.islower()],
          f'{t-38:02d}'][i.isupper()]
print(A)
