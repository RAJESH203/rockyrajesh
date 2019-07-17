import math
ps1,rs1=map(int,input().split())
rrs=[]
sss=list(map(int,input().split()))
for i in range(0,rs1):
        uu,vv =map(int,input().split())
        rrs.append([uu,vv])
for i in rrs:
        xx=i[0]-1
        yy=i[1]-1
        print(math.gcd(sss[xx],sss[yy]))
