I = input
d = {*eval('I(),' * int(I()))}
D = {i + j for i in d for j in d}
exec("print(+((w:=I())in d or 2*(w in D)));" * int(I()))
