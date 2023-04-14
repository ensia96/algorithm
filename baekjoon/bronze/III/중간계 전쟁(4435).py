A = [1, 2, 3, 3, 4, 10]
B = [1, 2, 2, 2, 3, 5, 10]
C = ['No victor on this battle field', 'Good triumphs over Evil',
     'Evil eradicates all trace of Good']
for i in range(int(input())):
    x, y = [*map(int, input().split())], [*map(int, input().split())]
    X, Y = sum(A[i]*x[i]for i in range(6)), sum(B[i]*y[i]for i in range(7))
    print(f'Battle {i+1}:', C[(X > Y)+2*(X < Y)])
