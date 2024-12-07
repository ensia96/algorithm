a, b, c, *_ = input()
a = ord(a) - 97
b = ord(b) - a
b += 26 * (b < 97)
c = ord(c) - a
c += 26 * (c < 97)
print(["BHA", "SJA", "NLCS", "KIS"][["qz", "br", "be", "eh"].index(chr(b) + chr(c))])
