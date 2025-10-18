for l in[*open(0)][2::2]:l=0,*map(int,l.split()),1440;print('YNEOS'[sum((j-i)//120for i,j in zip(l,l[1:]))<2::2])
