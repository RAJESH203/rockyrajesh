from itertools import combinations
strin,num=map(int,input().split())
c=len(str(strin))
t=list(combinations(str(strin),c-num))
t=(sorted(t))
y="".join(t[0])
print(y)
