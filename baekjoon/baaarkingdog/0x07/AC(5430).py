import sys
import collections as c

i = sys.stdin.readline

for _ in range(int(i())):
    p, _, d, r, f = i().strip(), i(), c.deque(i()[1:-2].split(',')), 0, 0
    for a in p:
        if a == 'R':
            r = not r
        else:
            if not d or not d[0]:
                f = 1
                break
            else:
                d.pop() if r else d.popleft()

    print('error' if f else f"[{','.join(reversed(d) if r else d)}]")
