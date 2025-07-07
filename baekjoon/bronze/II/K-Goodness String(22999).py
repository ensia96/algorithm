t = 0
for _ in ' '*int(input()):
    n, k = map(int, input().split())
    A = input()
    t += 1
    print(f"Case #{t}:", abs(k-sum(A[i] != A[n-i-1]for i in range(n//2))))
