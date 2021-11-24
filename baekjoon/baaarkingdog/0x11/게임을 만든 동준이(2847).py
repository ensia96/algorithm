I, R = input, range
n, a = int(I()), 0
l = [int(I())for i in R(n)][::-1]
for i in R(1, n):
    if l[i-1] <= l[i]:
        a, l[i] = a+l[i]-l[i-1]+1, l[i-1]-1
print(a)
