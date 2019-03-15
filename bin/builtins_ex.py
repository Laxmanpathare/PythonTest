#map function
L=[100,200,300,400]
def disc(p):
    return p/10
r1=map(disc,L)
print(list(r1))
print(list(r1))

#filters - one function and one collection
def filt(p):
    return p>100 and p<400
r2=filter(filt,L)
print(list(r2))

#reduce - not in builtins
from functools import reduce
def red(p,q):
    return p+q
r3=reduce(red,L)
M=['w','e','l']
r4=reduce(red,M)
print(r3,r4)

#Lambda functions
r5=map(lambda p:p-10,L)
print(list(r5))

add=lambda a,b:a+b
r6=add(100,200)
print(r6)
L=[lambda a,b:a+b]
r7=L[0](10,20)
print(r7)
