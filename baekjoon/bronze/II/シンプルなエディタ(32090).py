while n := int(input()):
    s = ''
    c = 0
    exec(
        "x=input();s=s[:c]+x[-1]*(x<'L')+s[c:];c=max(0,min(len(s),c+1-2*(x[2]<'G')));" * n)
    print(s)
