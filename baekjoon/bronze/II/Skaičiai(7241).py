input()
a, b, c = map(int, input())
print(2 * ((a > b) + (a > c)) + (b > c) + 1)
