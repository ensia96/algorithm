for l in [*open(0)][1:]:
    a, b = l.split()
    print(f"{float(a)*{'kg':2.2046,'lb':0.4536,'l':0.2642,'g':3.7854}[b]:.4f}", {
          'kg': 'lb', 'lb': 'kg', 'l': 'g', 'g': 'l'}[b])
