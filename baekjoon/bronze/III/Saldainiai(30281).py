n = int(input())
A = sorted(map(int, input().split()))
print(max(s//2*-~-(s % 2)for s in [sum(A[i:])for i in range(n)]))
