a, b, x, y = map(int, open(0).read().split())
print(
    2
    if a and b
    else 3 if not a and not x and y < b else 3 if not b and not y and x < a else 1
)
