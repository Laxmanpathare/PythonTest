#==========File Operations===========
#mainly 3 operation
#1. Open file
#2. Read/write file
#3. Quit file


F1=open('out.txt','w')
#There are 2 methods to write file
x=10
s='python \n'
x=str(x)+'\n'
F1.write(x)
F1.write(s)
F1.flush() #push data from buffer to file

L=[x,s]
F1.writelines(L)
F1.close()

f2=open('out.txt','r')#there are 3 methinds to read the file
r1=f2.read()
print('r1=',r1)
f2.seek(0)
r2=f2.read()
print('r2=',r2)
f2.seek(0)
r3=f2.readline()
print('r3=',r3)
while True:
    line=f2.readline()
    if line =='':#EOF
        break
    else:
        print('line=',line)
f2.seek(0)
r4=f2.readlines()
print('r4=',r4)

r5=[]
for line in r4:
    r5.append(line.strip())
    print('r5=',r5)

f2.seek(0)
for line in f2:
    print('line=',line.strip())
f2.close()

f3=open('out.txt','a')
f4=open('out1.csv','a')
print(20,'java',sep='\n',file=f3,flush=True)
print(20,'java', sep=',',file=f4)
f3.close()
f4.close()


F3=open('out_test.txt')
r=F3.readlines()
length = len(r)
middle = length/2
print(middle)
middle = int(middle)
print(middle)
print(r[middle])