a, *A = input().split()
B = a[0].upper()
for a in A:
    if a not in ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']:
        B += a[0].upper()
print(B)
