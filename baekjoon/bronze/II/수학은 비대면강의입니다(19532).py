a, b, c, d, e, f = map(int, input().split())
t = a*e-b*d
print((c*e-b*f)//t, (a*f-c*d)//t)

# ax + by = c
# dx + ey = f
#
# ax + by - c = dx + ey - f
#
# adx + bdy - cd = adx + aey - af
#
# (bd - ae) * y = cd - af
#
# y = (cd - af) // (bd - ae)
#
# y = (af - cd) // (ae - bd)
