O = '+-*/'
a, b, c = input().split()
print(min(int(A)for i in O for j in O if (
    A := eval("(" + a + i + b + ")" + j + c)) % 1 == 0 and A >= 0))
