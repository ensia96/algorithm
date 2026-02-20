for i in[*open(0)][1::2]:
 i=len(l:=[*map(int,i.split())])
 while i>1and l[-1]-l[-2]==l[i-1]-l[i-2]:i-=1
 print(i)
