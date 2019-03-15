a=0
while a<10:
    print('a',a)
    a=a+1 #a+=1

#============Collection===========

s='python'
i=0
while i <len(s):
    print(s[i])
    i=i+1

#=====================================

L=[10,20,30]
while L:
    x=L.pop()
    print('processed:',x)

#=====================================

L=['l1','l2','TS','R1','l1','TS','R2','l1']
i=0
while i <len(L):
    if L[i].startswith('TS'):
        i+=1
        print('Here you find it :',L[i])
        i+=1
    else:
        i+=1

 #=============================

k=0
while k < len(L):
    if L[k].startswith('R'):
        print('R Foound',k)
        break
    else:
        k=k+1
else:
    print('NF')

#====================================

n=0
while n < len(L):
    if not L[n].startswith('R'):
        n=n+1
        continue
    print (L[n])
    n=n+1
    print('End of while')

#===================================

cart=[]
while True:
    i=input('Enter Item:')
    cart.append(i)
    ch=input('Quit (y/n)?:')
    if ch=='y':
        print('çart is :',cart)
        break

