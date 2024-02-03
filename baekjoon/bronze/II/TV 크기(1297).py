I = int
d, h, w = map(I, input().split())
x = d/(h*h+w*w)**.5
print(I(x*h), I(x*w))
