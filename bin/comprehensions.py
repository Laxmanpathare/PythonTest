#Comrehensions

#List Comprehensions
L1=[i for i in range(10)]
L2=[i*i for i in L1 if i%2==0]
print(L1,L2)

#Tuple Comprehensions
T1=(i*i for i in L1 if i%2==0)
print(list(T1))
print(list(T1))

#Comprehensions for file ops
f=open('out.txt')
L3=[line.strip() for line in f]
print(L3)

#using Lambda
L4=[(lambda i:i*i)(i) for i in L1 if i%2==0]
print(L4)

f2=open(r'C:\Users\Admin\Desktop\Laxman\log\server_log.txt')
ip=[line.split()[0] for line in f2 if line[:3].isdigit()]
print(ip)

k=['k1','k2']
v=[10,20]
D={k:v for k,v in zip(k,v)}
E={k:(lambda x:x+10)(v) for k,v in zip(k,v)}
print(E)
f=dict(zip(k,v))
print(f)
print(D)


