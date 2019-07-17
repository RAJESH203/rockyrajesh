s=int(input())
m=list(map(int,input().split(None,s)[:s]))
m.sort(key=None,reverse=True)
if m.count(0)==len(m):
    print(0)
else:
    print("".join(map(str,m)))
