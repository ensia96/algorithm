h,k,v,s=map(int,input().split())
x=0
while h:v+=s;v-=v//10or 1;h+=v>=k;h-=0<v<k;v*=(h>=1or v>=k)*(v>0);h*=v>0;x+=v;s-=s>0
print(x)
