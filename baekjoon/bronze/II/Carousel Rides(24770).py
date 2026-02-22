"""
f=lambda:[*map(int,input().split())]
while(L:=f())[0]:r=[(b/a,-a,a,b)for a,b in[f()for _ in"_"*L[0]]if a<=L[1]];print(r and"Buy %d tickets for $%d"%min(r)[2:]or"No suitable tickets offered")
"""

f = lambda: [*map(int, input().split())]
while (L := f())[0]:
    r = [(b / a, -a, a, b)for a, b in [f()for _ in "_" * L[0]]if a <= L[1]]
    print(r and "Buy %d tickets for $%d" %
          min(r)[2:] or "No suitable tickets offered")
