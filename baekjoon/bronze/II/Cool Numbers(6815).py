a, b = map(int, open(0))
print(sum(b >= i**6 >= a for i in range(100)))
