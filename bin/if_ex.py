a=0

if a==10:
    print('a eq 10')
if a>10:
    print('a gt 10')
if a<10:
    print('a lt 10')

b=10

if b==10 :
    print('b eq 10')
elif b>10:
    print('b gt 10')
elif b<10:
    print('b lt 10')


c=30

if c==10 :
    print('c eq 10')
elif c>10:
    print('c gt 10')
else :
    print('c lt 10')


S='python'

if not S.startswith('java'):
    print('Not Java')
if S!='C':
    print('Not C')
if 'th'in S :
    print('Substring found')

#--------------------------------------------------
L1=[10,20]
L2=L1
L3=L1.copy()

if 20 in L1:
    print('20 Found')
if L1 is L2 : #Reference equality
    print('Both refers same object')
if L1==L3 :#Object equality
    print('Contents are same')

#==================================================

D={'A':10,'B':20}

if 'B'in D:
    print('Key : B found')

if 20 in D.values():
    print('value 20 found')

if ('B',20) in D.items():
    print('Item Found')


    
    
          
    

