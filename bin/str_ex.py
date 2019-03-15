a='Person'
b="Person's"
c='''Person's height is 2"'''
print(a)
print(b)
print(c)
e= '''line1
 line 2'''
print(e)

f='line1 \
   line2'
print(f)
g='PERSON\'S'
print(g)
h='C:\\newfolder\\search_file.py'
print(h)
i=r'C:\newfolder\test.py'
print(i)
j='WEL COME'
print(j)
print(len(j))
print(j[1])
print(j[1:6])
print(j[:6])
print(j[1:])
print(j[:])
print(j[1:6:3])
print(j[::-1])
print(j[6:1:-2])
print(j[len(j)-1])
print(j[-1])
print(j[-4:])
r1=j.startswith('WEL')
print(r1)
r2=j.endswith('COME')
print(r2)
r3=j.isupper()
print(r3)
r4=j.islower()
print(r4)
r5=j.upper()
r6=j.lower()
print(r5)
print(r6)
r7=j.istitle()
r8=j.title()
print(r7,r8)
k='abc'
r9=k.isalpha()
l='123'
r10=l.isdigit()
m='abc123'
r11=l.isalnum()
print(r9,r10,r11)
r13=m[-3:].isdigit()
print(r13)
r14=j.replace('E','e')
print(r14)
r15=j.index('E')
r16=j.find('E')
print(r15)
print(r16)

r17=j.index('E',3)
r18=j.find('X')
print(r17)
print(r18)
S1='Hello'
S2='py'
r19=j.index('E',3,8)
print(r19)
r20=S1+S2
print(r20)
r21=S1*10
print(r21)
line='='*40
print(line)

n=' Wel  come  '
r22=n.strip()
r23=n.lstrip()
r24=n.rstrip()
print(r22,r23,r24)

P='[wel[come][]'
r26=P.strip('][ew')
r27=P.lstrip('w[')
r28=P.rstrip('][e')
print(r26,r27,r28)
r29=j.count('E')
print(r29)

X=10
Y=20
Z=X+Y
r30='add of {} &{} is {}'.format(X,Y,Z)
print(r30)

r31='add of {1} &{0} is {2}'.format(X,Y,Z)
print(r31)

r32=f'addition of {X} & {Y} is {Z}'
print(r32)

r33=j.split()
print(r33)

r34=j.split('E')
print(r34)

r35='XYZ'.join(r34)
print(r35)
