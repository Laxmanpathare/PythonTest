#Decorators
def add(a,b):
    print('result is:')
    print(a+b)
    print('End of the result')
def sub(a,b):
    print('result is:')
    print(a-b)
    print('End of the result')
add(10,20)
sub(10,20)

def my_dec(func_to_be_deco):
    def decorated_func(a,b):
        print('Result is :')
        func_to_be_deco(a,b)
        print('End of result:')
    return decorated_func
@my_dec
def add(a,b):
    print(a+b)
@my_dec
def sub(a,b):
    print(a-b)

add(20,30)
sub(20,30)

def add2(a,b):
    print(a+b)
f=my_dec(add2)
f(100,200)

