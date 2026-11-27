from base64 import *
from zlib import *
l, r = map(int, input().split())
print(
    *decompress(b85decode('c-lphYi{E(41}*T2QYkxMf-DG>=kH<aS7<*N@C8xBgaVq1A<Lz<{Q#~Ytsxnx@W|iYD2dH$vPH<TDpdz!y6>pVLe#cp~=RI&ssF#*R3P5$@}XfqzpxOb|3sSG#|CC_@hOoAj)AIyKh#`bJWHMcN?O(Nw8$y`igH)NnRhGelOM2L(r+F1$&dbMIoBnO-o$y;Y~K1<W`=5KA^=iI*F8)1S&G7*~K=KfmlBaeyGy4&3D=sFM&b}qERU$cq7SUVDH;IvtL%tSSLjj&ZVYgfh>_Izb^R-E55rT&uYhJ8y!7UE!o+m9Br-<cTa~8Vcf@lgd?T=V3)4=*F?LPF{5XmggcrJ<9UC?sfFZ2+bRA%gB-QHwmEGN=MJ*$MPTuHb;Xxx;Bfl<2S~YGVrRr_d|c`n#@#JkaZ2x1z6ywL%NrJ{ZY(kEnU6A%fEul?{{bzc?<f')).decode().split()[l - 1:r])

