#Tuple-> class
T=(10,2.5,'python',['a','b'],(30,40))
print(T)

print(T[1])
print(T[1:])

i=T.index('python')
c=T.count(2.5)

print(i,c)

#Conversion of Tuple to List

L=list(T)
print('L=',L)

L.append(20)

T=tuple(L)

print('T=',T)

    
