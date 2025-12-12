f=lambda I:[ord(i)-97for i in I[:-1]]
*L,=open(t:=0)
for S,C in zip(L[1::2],L[2::2]):t+=1;S=f(S);C=f(C);print(f"Case #{t}:",sum(map(min,zip(*[[min((m:=abs(s-c)),26-m)for s in S]for c in C]))))
