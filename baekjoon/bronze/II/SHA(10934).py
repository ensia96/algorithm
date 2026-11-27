from struct import *
s = input().encode()
w = unpack(">16I", pack(">60sI", s + b"\x80", len(s) * 8))
H = S = [a := 0x67452301, b := 0xefcdab89, ~a, ~b, 0xc3d2e1f0]
M = 2**32
P = M + 1
for i in range(80):
    a, b, c, d, e = S
    x = c ^ d
    j = i // 20
    w += w[-3] ^ w[-8] ^ w[-14] ^ w[-16],
    S = [((a * P >> 27) + [d ^ b & x, b ^ x, d ^ (b ^ d) & x, b ^ x][j] +
          int([2, 3, 5, 10][j]**.5 * M / 4) + e + w[i]) % M, a, b * P >> 2, c, d]
print("%08x" * 5 % tuple((x + H.pop(0)) % M for x in S))

