I = input
exec(
    "t=sum(eval(I().replace(*' *'))for _ in[0]*int(I()));print(1296//t,2592//t,3888//t);" * int(I()))
