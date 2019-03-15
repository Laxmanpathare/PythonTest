#list->Class
L=[10,26.22,30,'python',['a','b']]
print(L)

print(L[1])

print(L[3][1])

print(L[3:])

L[1]=24

print(L)

print('Update=',L)

L.append(200)

print('append=',L)

L.insert(2,'C++')

print('insert=',L)

L1=[10,20]
L2=['a','b']
L3=L1+L2
L4=L1*10
print(L3)
print(L4)

L1.extend(L2)

print('new :',L1)

print(L1)

r1=L.pop()
print('Pop: ',L,r1)

r2=L.pop(2)
print('Pop2=',r2,L)

r3=L.remove('python')
print('remove=',L)

L5=[20,10,40]
L5.sort()

print(L5)
L6=['X','T','N']
L6.sort(reverse=True)
i=L6.index('T')
c=L6.count('T')

print(i,c)

L7=[10,20,['a','b']]
L8=L7
L9=L7.copy()

print(L7)

L9[1]=30
print(L7)
print(L8)
print(L9)

import copy

L10=copy.deepcopy(L8)

print(id(L8[0]),id(L8[2]))
print(id(L10[0]),id(L10[2]))

L10.clear()

