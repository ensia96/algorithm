a, b, c = sorted(map(int, input()))
print(('un'*(c-b == b-a)*(c-b in [1, 3])+'locked').capitalize())
