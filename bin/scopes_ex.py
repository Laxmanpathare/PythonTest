x=10 #Global scope whioch we access everywhere in the program
def f1():
    #x=20 #Enclosed scope
    def f2():
        #global x
        #nonlocal x
        #x=30 #Local Scope, if you comment this variable then f1 variable becomes Enclosed scope
        print('f2=',x)
    f2()
    print('f1=',x)
f1()
print('global=',x)
print(dir(__builtins__))# Builtin scope
count=0
def create_acc():
    global count
    count=count+1
def del_acc():
    global count
    count=count-1
def total_acc():
    print('total accounts=',count)
create_acc()
create_acc()
del_acc()
count=100
total_acc()
def account():
    count=0
    def create_acc():
        nonlocal count
        count=count+1
    def del_acc():
        nonlocal count
        count=count-1
    def total_acc():
        print('total account=',count)
    return create_acc,del_acc,total_acc
r1=account()
ca,da,ta=account()
ca()
ca()
da()
ta()

