h,k,v,s=map(int,input().split())
x=0
while h:v+=s;v-=v//10or 1;h=(v>0)*(h+(v>=k)-(v<k));x+=v*(h>0);s-=s>0
print(x)
