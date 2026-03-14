t,*A=map(int,open(0).read().split());k=0
while k<t:n,m,*A=A;k+=1;P=A[4*m:];print(f'Data Set {k}:',*[i+1for i in range(m)if A[(j:=4*i)]<(A[j+3]-A[j+1])*min(P[:n].count(i+1),A[j+2])],'',sep='\n');A=P[n:]
