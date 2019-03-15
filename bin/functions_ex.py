a=10
if a==10:
    pass
def add1():
    pass
def add2():
    a=10
    b=20
    c=a+b
    print('c=',c)

add2()
print('some line')
add2()
#print('c=',c)
def add3():
    a=10
    b=20
    c=a+b
    #return c
    #print('add3=',c)
    #return
    #return [a,b,c]
    #return a,b,c
    return (a+b)/(a-b)
add3()
r1=add3()
print('r1=',r1)

#==========Positional Arguments===============

def add4(a,b):
    return a+b
r2=add4(5,10)
print('r2=',r2)

#=============Positional Argumnets with default value===================
def add5(a,b=10):
    return a+b
r3=add5(1)
print('r3=',r3)

#===============Variable Arguments===========
def add6(a,b=10,*c):
    print('Remaining arguments passed:',c)
    r=a+b
    for i in c:
        r=r+i
    return r
r4=add6(2,4,5,5,5,5,5,5,100)
print('r4=',r4)

#============Keyword only arguments==========
def add7(a,b=10,*c,d,e):
    r=a+b+d+e
    for i in c:
        r=r+i
    return r
r5=add7(2,4,3,4,e=50,d=60)
print('r5=',r5)

#===========variable keyword only arguments=============
def add8(a,b=10,*c,d,e,**f):
    print('Remaining Keyword only args:',f)
    r=a+b+d+e
    for i in c:
        r=r+i
    for j in f.values():
        r=r+j
    return r
r6=add8(1,2,3,4,4,4,d=4,e=2,f=5,g=2)
print(r6)

L=[10,20,30,40,50,60]
r7=add6(*L)
print(r7)

D={'d':50,'e':60}
r8=add7(*L,**D)
print(r8)
#add()- normal function
#add(a,b)-positional arguments
#add(a=10,b=20)-positional arguments with default values
#add(*a) positional only arguments
#add(*a,**b)-
#add(*,a,b) - keword arguments
#add(**a)Keyword only arguments