for l in[*open(0)][1:]:i,*I=[chr(i|32)if 96<(i|32)<123else"-"for i in map(int,l.split())];print(*I,i,"ay",sep="")
