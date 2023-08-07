A = input()
x, y = A.find('U'), A[::-1].find('F')
print('-'*x+'U'+'C'*(len(A)-x-y-2)+'F'+'-'*y)
