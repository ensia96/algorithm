n, *A = open(0)
x = y = 0
B = []
while A:
    try:
        x += int(A.pop())
        y += 1
    except:
        B += bool(x % y),
        x = y = 0
for b in B[::-1]:
    print('YNEOS'[b::2])
