for _ in ' '*int(input()):
    a, *A = map(int, input().split())
    print('Denominations:', *A)
    print(['Bad', 'Good'][all(A[i] >= A[i-1]*2 for i in range(1, a))],
          'coin denominations!\n')
