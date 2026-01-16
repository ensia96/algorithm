I = input
t = 0
exec('S=[I().split()for _ in"0"*int(I())];t+=1;print("Test case #%d:"%t)\nfor _ in"0"*int(I()):i=j=I();[j:=j.replace(*s)for s in S];print(i,"YNEOS"[j!=j[::-1]::2])\nprint()\n' * int(I()))
