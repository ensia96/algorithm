s = []

for _ in range(int(input())):
    c = input()
    if "push" in c:
        s.append(c.split().pop())
    if c == "pop":
        print(s.pop() if s else -1)
    if c == "size":
        print(len(s))
    if c == "empty":
        print(0 if s else 1)
    if c == "top":
        print(s[-1] if s else -1)
