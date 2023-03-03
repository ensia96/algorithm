for l in open(0):
    x, y = map(float, l.split())
    print(['AXIS', f'Q{(x<0)+(y<0)*2*(1+(x>0))+(y>0)}'][bool(x*y)])
