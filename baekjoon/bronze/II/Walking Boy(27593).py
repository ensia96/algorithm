for l in[*open(0)][2::2]:l=*map(int,l.split()),1440;print('YNEOS'[sum((j-i)//120for i,j in zip([0,*l],l))<2::2])
