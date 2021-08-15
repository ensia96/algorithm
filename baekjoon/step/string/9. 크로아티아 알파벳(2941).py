d = [
    "c=",
    "ć",
    "c-",
    "dž",
    "dz=",
    "đ",
    "d-",
    "lj",
    "lj",
    "nj",
    "nj",
    "š",
    "s=",
    "ž",
    "z=",
]

s, c = input(), 0

for a in d:
    if a in s:
        c += s.count(a)
        s = s.replace(a, " ")
s = s.replace("=", "")
s = s.replace("-", "")

print(c + len("".join(s.split())))
