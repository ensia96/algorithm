x, k = map(int, input().split())
a, b, c, d = k//4, k//2, k*2, k*4
print(max(0, a+b+k*(a+b+k < x), b+k+c*(b+k+c < x), k+c+d*(k+c+d < x)))
