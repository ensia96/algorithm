s = []

for _ in range(int(input())):
    c = input()
    if c == "pop":
        print(s.pop() if s else "-1")
    elif c == "size":
        print(str(len(s)))
    elif c == "empty":
        print("0" if s else "1")
    elif c == "top":
        print(s[-1] if s else "-1")
    else:
        s.append(c.split().pop())
