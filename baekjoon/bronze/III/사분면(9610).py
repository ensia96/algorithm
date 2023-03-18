A = [0]*5
for _ in ' '*int(input()):
    x, y = map(int, input().split())
    a, b = x < 0, y < 0
    A[[0, 1+(a or b)*(2-a+b)][bool(x*y)]] += 1
for i in range(1, 5):
    print(f'Q{i}:', A[i])
print('AXIS:', A[0])
