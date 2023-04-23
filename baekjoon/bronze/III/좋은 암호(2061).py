k, l = map(int, input().split())
for i in range(2, l):
    k % i or exit(print('BAD', i))
print('GOOD')
