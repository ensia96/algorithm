for l in[*open(0)][1:]:a,b,c,d=sorted(map(int,l.split()));print(*[sum(((s:=x*x+y*y-z*z)==0,s>0,s<0)[i]for x,y,z in[(a,b,c),(a,b,d),(a,c,d),(b,c,d)]if x+y>z)for i in(0,1,2)])
