n = int(input())
a, b = input(), input()
print(sum(a[i] != b[i]for i in range(n)))
