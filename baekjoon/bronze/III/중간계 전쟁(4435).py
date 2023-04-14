A = [1, 2, 3, 3, 4, 10]
B = [1, 2, 2, 2, 3, 5, 10]
C = ['Evil eradicates all trace of Good',
     'Good triumphs over Evil', 'No victor on this battle field']
for i in range(int(input())):
    x, y = sum(A[i]for i in map(int, input().split())), sum(B[i]
                                                            for i in map(int, input().split()))
    print(f'Battle {i}?:', C[x > y+2*(x < y)])
