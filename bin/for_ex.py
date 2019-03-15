S='python'

for a in S :
    print('a=',a)

L=[10,20,30]
b='java'

for b in L :
    print('b=',b)
print('Now a & b=',a,b)


#---------------------------------------------

D={'A':10,'B':20}

for K in D :
    print('K=',K,'V=',D[K])

for v in D.values():
    print('V=',v)

for i in D.items() :
    print(i,i[0],i[1])

for i,j in D.items():
    print(i,j)

#==============================================================================
L1=[10,20,30]
L2=['a','b']
r1=zip(L1,L2)
print(r1)
print(list(r1))
for i,j in zip(L1,L2):
    print(i,j)
#==============================Compare or find===============================================
comp=['IBM','SYN1','SAP','SYN2']
for i in comp:
    if i.startswith('OLD'):
        print('Found')
        break
else:
    print('NF')

for j in comp:
    if j.startswith('SYN'):
        continue
    if j.startswith('SYN'):
        print('some logic')
    print('end of for')


#==============================Range===========================================

#for(i=2;i<10;i=2)

r1=range(10)
r2=range(1,10)
r3=range(1,10,2)
print(list(r1),list(r2),list(r3),sep='\n')
for i in range(2,10,2):
    print(i)
for j in comp[1:]:
    print(j)
for k in range(0,len(comp)):
    print(comp[k])

