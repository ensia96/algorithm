I = input
exec('A=[[*map(int,I().split())]for _ in" "*int(I())];print(*min(((p[0]-q[0])**2+(p[1]-q[1])**2,p+q)for p in A for q in A if p is not q)[1]);' * int(I()))
