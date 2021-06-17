import re
virus=input()
sa=virus
n=int(input())
count=0
a=[]
for i in range(n):
    s=input()
    a.append(s)
for i in range(len(a)):
    for j in range(len(a[i])):
                   ind=sa.find(a[i][j])
                   sa=sa[ind+1:]
                   if (ind)!=(-1):
                       count=count+1
                   else:
                       print("NEGATIVE")
                       break
                   if count==len(a[i]):
                       print("POSITIVE")
    count=0
    sa=virus
  
