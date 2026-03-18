exec(
    "W=eval('input(),'*3);print('YNeos'[any(x in(y[:len(x)],y[-len(x):])for x in W for y in W if x!=y)::2]);" * int(input()))
