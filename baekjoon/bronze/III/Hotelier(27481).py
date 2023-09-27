n = int(input())
*A, = '0'*10
R = range(10)
for i in input():
    if i == 'L':
        for i in R:
            if A[i] == '0':
                A[i] = '1'
                break
    elif i == 'R':
        for i in R[::-1]:
            if A[i] == '0':
                A[i] = '1'
                break
    else:
        A[int(i)] = '0'
print(''.join(A))
