f, n = lambda x: str(x)if x < 9 else f(x//9)+str(x % 9), int(input())
print(f(n))
