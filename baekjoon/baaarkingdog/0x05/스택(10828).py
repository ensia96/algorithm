import sys

s = []

for _ in range(int(input())):
    c = sys.stdin.readline().split()
    if c[0] == "pop":
        print(s.pop() if s else -1)
    elif c[0] == "size":
        print(str(len(s)))
    elif c[0] == "empty":
        print(0 if s else 1)
    elif c[0] == "top":
        print(s[-1] if s else -1)
    else:
        s.append(c.pop())
