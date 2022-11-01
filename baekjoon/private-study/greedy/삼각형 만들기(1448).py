*A, a, b, c = sorted(int(input())for _ in ' '*int(input()))
while A and c >= a+b:
    a, b, c = A.pop(), a, b
print(-(c >= a+b) or a+b+c)
