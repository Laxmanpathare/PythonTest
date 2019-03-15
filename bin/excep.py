a=10
b=10
e=20
try:
    r=a/b
    print('r=',r)
except:
    print('Some Error')

c=10
d=0
try:
    r=c/d
except ZeroDivisionError:
    print('ZDE')
except NameError:
    print('NE')

try:
    r1=c/d
except:
    print('some error')
else:
    print('In else')
    r2=a/b

try:
    r=a/c
finally:
    print('In Finally')

try:
    r=a/f
except Exception as e:
    print(e)
    print(type(e))

try:
    if d==0:
        raise ZeroDivisionError
    r=c/d
except:
    print('From Raise')

result='Test Failed'
try:
    assert 'Success' in result,'testcase got failed'
    print('Test Completed Successfully')
except AssertionError as a:
    print('a=',a)

class MyError(Exception):
    def __init__(self,m):
        self.msg=m
    def __str__(self):
        return  'Details :'+ self.msg


x=0
try:
    if x==0:
        raise MyError('X is Zero')
except MyError as m:
    print('m=',m)







