n,t=map(int,input().split())
for i in range (n+1,t):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i, end=' ')
