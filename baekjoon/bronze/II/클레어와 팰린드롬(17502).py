n = int(input())
A = input().replace("?", "a")
print("".join([max(A[i], A[~i]) for i in range(n)]))
