L=['python',5,'Pune']
print(L[0])

D={'course':'python','dur':5,'loc':'Pune'}

print(D)

print(D['course'])

r1=D.get('author','No such key')
print('R1=',r1)

r2=D.get('course','No such key')
print('R2=',r2)

#add & Update

D['course']=['java','c']
print('D=',D)


E=D.copy()
r1=D.pop('course')
print(D,r1)

del D['dur']
X=10
del X

print(D)

D1={'course':'python','dur':5,'loc':'Pune'}
r2=D1.popitem()
print(r2)

k=E.keys()
v=E.values()
i=E.items()
print(k,v,i,sep='\n')
