*A, = map(int, input())
for i in range(2, len(A)+1, 2):
    A[-i] = [2*A[-i], sum(map(int, str(2*A[-i])))][A[-i] > 4]
print('DNAE'[sum(A) % 10 > 0::2])
