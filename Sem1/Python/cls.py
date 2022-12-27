"""class player:
    def get(self):
        self.name="xyz"
        self.age=20
        self.country="India"
    def dispaly(self):
        print("name=",self.name)
        print("age=",self.age)
        print("country=",self.country)
obj=player()
obj.get()
obj.display()"""
# 
'''class student():
    def get(self,n,r,b):
        self.name=n
        self.reg=r
        self.branch=b

    def display(self):
        print("name=",self.name)
        print('reg=',self.reg)
        print('branch=',self.branch)
o=student()
name=input('Enter student name=')
reg=int(input('enter student reg='))
branch=input('enter branch=')
o.get(name,reg,branch)
x.display()'''
# 
'''class student:
    def __init__(self,n,r,b):
        self.name=n
        self.reg=r
        self.branch=b
    def dispaly(self):
        print('name=',self.name)
        print('reg=',self.branch)
        print('branch=',self.branch)

name = input()
reg=int(input())
b=input()
o=student(name,reg,b)
o.display()'''
# create a class
'''class volume:
    def __init__(self,r,h):
        self.radius=r
        self.height=h
    def display(self):
        self.vs=1.33*3.14*(self.radius**3)
        print("volumeof sphere=",self.vs)
        self.vc=3.14*(self.radius**2)*self.height
        print('volume of cylinder=',self.vc)
r=float(input('Enter radius='))
h=float(input('Enter height='))
obj=volume(r,h)
obj.display()'''        
# create a class containing a user defined function get used to 
# define to initalize the student name,age,reg,student branch.teh class containing two more function having name display.
# the cal is defined to cal the % and cgpaby taking marks from various courses while display method display the complete detail of student
class student:
    def get(self,n,r,a):
        self.name=n
        self.age=a
        self.reg=r
    def calculate(self,m1,m2,m3,m4,m5):
        self.marks1=m1
        self.amrks2=m2
        self.marks3=m3
        self.marks4=m4
        self.marks5=m5
    def display(self):
        self.per=(self.marks1+self.marks2+self.marks3+self.marks4+self.marks5/500)*100
        print("name=",self.name)
        print("reg=",self.reg)
        print("per=",self.per)

o=student()
o.get("abc",123,20)
o.calculate(97,63,82,75,64)
o.display()