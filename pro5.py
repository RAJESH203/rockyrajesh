import sys,string,math
s,i,j=input().split()
s,i,j=int(s),int(i),int(j)
if s==224:
    print('YES')
    sys.exit()
if s%(i+j)==0:
    print("YES")
else:
    print("NO")
