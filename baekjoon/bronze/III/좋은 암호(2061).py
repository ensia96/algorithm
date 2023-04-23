k, l = map(int, input().split())
for i in range(int(k**.5)+1, 1, -1):
    not k % i and i < l and exit(print('BAD', i))
print('GOOD')
