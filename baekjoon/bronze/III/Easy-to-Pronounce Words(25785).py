a = [i in 'aeiou'for i in input()]
a, b = a[::2], a[1::2]
print((not any(a) and all(b)) or (not any(b) and all(a)))
