x = 0
for l in [*open(0)][1:-1]:
    if '고' in l:
        x += 2-3*(x != 0)
    else:
        x += 1
print(['힝구', '고무오리야 사랑해'][x == 0])
