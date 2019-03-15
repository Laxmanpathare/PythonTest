#set->class
#unordered
#Ni index
#No Key
#Sets & Unions
#Unique values

S={10,10,'python','python'}
print(S)

S.add(20)
print(S)

S.add(20)
print(S)

t=S.copy()

r1=S.remove('python')
r2=S.pop()
print(S,r1,r2)

L=list(t)
print('L=',L)

M=[10,10,20,20]

S1=set(M)
print('S1=',S1)

L=[]
print(dir(L))

print(help(L.append))
