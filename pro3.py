import sys, string, math
t1,t2 = input().split()
n1 = len(t1)
n2 = len(t2)
if n2 > n1 :
    i = 0
    while i<n1 and t1[i] == t2[i] :
        i += 1
    print(n2-i)
elif n2 == n1 :
    i = 0
    while i<n2 and t1[i] == t2[i] :
        i += 1
    print(n2-i)
else :

    i = 0
    while i<n2 and t1[i] == t2[i] :
        i += 1
    t31 = t1[i:]
    t32 = t2[i:]
    L = list(t31)
    k = 0
    for c in t32 :
        if c in L :
            k += 1
            L.remove(c)
    print(n1-i-k)
