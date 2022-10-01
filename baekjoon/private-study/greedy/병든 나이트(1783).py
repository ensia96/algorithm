n, m = map(int, input().split())
if n == 1:
    A = 1
elif n == 2:
    A = min((m+1)//2, 4)
elif m < 7:
    A = min(m, 4)
else:
    A = m-2
print(A)
