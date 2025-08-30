_, c, g = input().split()
print(r := sum(i == j for i, j in zip(c, g)), sum(
    min(c.count(chr(65 + i)), g.count(chr(65 + i)))for i in range(26)) - r)
