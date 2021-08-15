d = {ord(c): 0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
m = 0

for s in input():
    c = ord(s)
    if c > 96:
        c -= 32
    d[c] += 1
    if m < d[c]:
        m = d[c]

print(
    "?"
    if list(d.values()).count(m) > 1
    else chr(sorted(d.items(), key=lambda x: x[1]).pop()[0])
)
