T = "KOREA"
l = 0
for i in input():
    l += i == T[l % 5]
print(l)
