# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
a=['g','g','c']
for i in range(random.randint(1,100)):
    random.shuffle(a)
k=0
ch=0
nch=0
for i in range(1000000):
    c=random.randint(1,3)-1
    t=-121
    d=-121
    for m in range(3):
        if m==c:
            continue
        if a[m]=='g':
             t=m
    if a[c]=='c':
        nch+=1
    for la in range(3):
        if la==c or la==t:
            continue
        d=la
    if a[d]=='c':
        ch+=1
    k+=1
pc=ch/k
pnc=nch/k
print(pc,pnc)
    
