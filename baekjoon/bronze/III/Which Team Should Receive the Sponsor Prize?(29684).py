n = int(input())
while n:
    *A, = map(int, input().split())
    print(min((abs(2023-A[i]), i)for i in range(n))[1]+1)
    n = int(input())
