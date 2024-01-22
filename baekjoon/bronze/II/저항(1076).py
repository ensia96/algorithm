A = ['black', 'brown', 'red', 'orange', 'yellow',
     'green', 'blue', 'violet', 'grey', 'white']
x, y, z = map(A.index, [input()for _ in ' '*3])
print((x*10+y)*10**z)
