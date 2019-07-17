ah=int(input())
qt=[]
for i in range(ah):
  ass=input()
  qt.append(ass)
ma2=min(qt,key=len)
qt.remove(ma2)
for i in range(len(ma2)):
  for j in range(len(qt)):
     ba1=qt[j]
     if ma2[:i+1]==ba1[:i+1]:
       result=ma2[:i+1]
     else:
       break
print(result)
