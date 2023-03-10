n = int(input())
print('\n'.join((n > 1)*[' '*(n-1)+'*']+[' '*(n-i)+'*' +
      ' '*(2*i-3)+'*'for i in range(2, n)]+['*'*(2*n-1)]))
