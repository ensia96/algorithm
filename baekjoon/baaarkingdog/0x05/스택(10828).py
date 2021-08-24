s, r = [], []

for _ in range(int(input())):
    c = input()
    if "push" in c:
        s.append(c.split().pop())
    if c == "pop":
        r.append(s.pop() if s else "-1")
    if c == "size":
        r.append(len(s))
    if c == "empty":
        r.append("0" if s else "1")
    if c == "top":
        r.append(s[-1] if s else "-1")

print("\n".join(r))
