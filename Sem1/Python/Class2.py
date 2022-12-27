# create a class in python having name employee cpntaining constructor define to initalize the class variable name id and departement
# use this class to create class accounts having one method get define to initalize two class members account numbers and salary
# use this calss to create another class class bonus ccontaining constructor define to containig the constructor
# defined to calculate the bonus as per detail.
'''class Employee:
    def __init__(self,n,a,i,d):
        self.name=n
        self.age=a
        self.id=i
        self.dept=d
class Accounts:
    def get(self):
        self.acctno=479324
        self.sal=24973
class Bonus(Accounts):
    def  __init__(self,n,a,i,d):
        Employee.__init__(self,n,a,i,d)
        Accounts.get(self)
        if self.sal>21600:
            self.Bonus=0
        elif self.sal<=1000:
            self.Bonus=self.Sal*0.10
        else:
            self.Bonus=5000
def display(self):
    print('Name=',self.name)
    print('Age=',self.age)
    print('Id=',self.id)
    print('Sal=',self.sal)
    print('Bonus=',self.Bonus)
obj=Bonus("NIKHIL",19,12215880,"CSE")
obj.display()'''

class User:
    def get(self):
        self.name=input('Enter name=')
        self.age=int(input('Enter age='))
        self.add=input('Enter address=')
        self.mob=input('Enter mobile no=')
class Company():
    def getdetails(self):
        self.cname=input('Enyer company name=')
        self.noe=int(input('Enter no of employees='))
        self.cadd=input('Enter company add=')
class Performance(User,Company):
    def __init__(self,g):
        self.grade=g
    def display(self):
        User.get(self)
        Company.getdetails(self)
        print('Name=',self.name)
        print('age=',self.age)
        print('Address=',self.add)
        print('Grade=',self.grade)
        if self.grade=='O':
            print('Outstanding')
        elif self.grade=='A':
            print('Excellent')
        else:
            print('Poor')
G=input('Enter grade value=')
G=G.upper()
if len(G)==1:
    obj=Performance(G)
    obj.display()
    
        

