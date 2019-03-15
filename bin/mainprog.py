import mymodule
import sys
#print(sys.path)
#sys.path.append(r'directory path of lib')
print(mymodule.msg)
print(mymodule.add(10,20))
line='='*40
print(line)

#import module using alias

import mymodule as m
print(m.msg)
print(m.add(30,40))
print(line)
#another way to import modules
from mymodule import msg,add
print(msg)
print(add(100,200))

#alias for each variable name

print(line)
from mymodule import msg as m, add as a
print(m)
print(a(10,10))

#one more way to import
print(line)
from mymodule import *
print(msg)
print(add(50,10))
print(line)
#importing packages
import project.net.mymodule
print(project.net.mymodule.msg)
print(project.net.mymodule.add(100,500))

print(line)
import project.net.mymodule as m
print(m.msg)
print(m.add(11,22))
print(line)
from project.net.mymodule import add,msg
print(msg)
print(add(11,22))

