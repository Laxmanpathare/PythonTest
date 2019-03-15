#Multiple objects
#Inheritance
#Operator Overloading
class Account1:
    def adduser(self,n):
        self.name=n
    def viewuser(self):
        return self.name
    bank='ICICI'
    def bankrules():
        return 'Bank Rules'
    #print(bank)
    def __init__(self):
        print('SB ACC#')
cust1=Account1()
cust2=Account1()
cust1.adduser('C1')
cust2.adduser('C2')
print(cust1.viewuser())
print(cust2.viewuser())
print(Account1.bank)
print(Account1.bankrules())

#Inheritance
class Account2(Account1):
    def addadhar(self,a):
        self.aadhar=a
    def viewadhar(self):
        return self.aadhar
    def viewuser(self):
        return 'Welcome '+self.name
    def __init__(self):
        print('C ACC#')
        super().__init__()
        #Account1.__init__(self)


cust3=Account2()
cust3.adduser('C3')
print(cust3.viewuser())
print(Account2.bank)
print(Account2.bankrules())
cust3.addadhar('A1')
print(cust3.viewadhar())


class RBI:
    def viewrules(self):
        return 'RBI Rules'

class Account3(Account2,RBI):
    def message(self,):
        return 'In Acc3'
cust4=Account3()
print(cust4.viewrules())

class Govt:
    def viewrules(selfs):
        return 'Govt Rules'

class Acc4(Account3):
    def __init__(self):
        self.gov=Govt()

cust5=Acc4()
print(cust5.viewrules())
print(cust5.gov.viewrules())

class Account5:
    def __init__(self,n):
        self.name=n
    def __add__(self, other):
        return 'Hello '+self.name+' and '+other.name

a=Account5('abc')
b=Account5('xyz')
c=a+b
print('C=',c)
