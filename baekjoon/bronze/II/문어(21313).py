n = int(input())
print(*n//2*'12'+n % 2*f'{1+2*(n>1)}')
