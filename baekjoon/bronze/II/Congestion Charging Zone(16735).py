T = [t for l in [*open(0)][1:]for h, m in [l.split(":")]
     if 390 <= (t := int(h) * 60 + int(m)) <= 1140]
print(T and [168, 240, 240, 360]
      [(min(T) < 601) * 2 + (max(T) > 960)] * 100 or 0)
