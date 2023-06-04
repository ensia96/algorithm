A = [int(input())]
x = 0
while A and A[0] != 1:
    a = A.pop()
    A += a+1 if a % 2 else a//2,
    x += 1
print(x)
