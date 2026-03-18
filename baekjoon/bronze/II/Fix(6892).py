exec(
    "W=eval('input(),'*3);print('YNeos'[any((x:=W[i])in(W[j][:len(x)],W[j][-len(x):])for i in(0,1,2)for j in(0,1,2)if i-j)::2]);" * int(input()))
