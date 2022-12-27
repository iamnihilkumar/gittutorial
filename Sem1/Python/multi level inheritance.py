class student:
    def __init__(self,n,b,r):
        self.name=n
        self.reg=r
        self.branch=b
class course(student):
    def __init__(self,n,b,r,c1,c2,c3,c4,c5):
        student.__init__(self,n,b,r)
        self.co1=c1
        self.co2=c2
        self.co3=c3
        self.co4=c4
        self.co5=c5
class Result(course):
    def __init__(self,n,b,r,c1,c2,c3,c4,c5):
        course.__init__(self,n,b,r,c1,c2,c3,c4,c5)
        self.total=self.co1+self.co2+self.co3+self.co4+self.co5
        self.per=(self.total/500)*100
        self.cgpa=self.per/10
    def display(self):
        print("Name=",self.name)
        print("Reg=",self.reg)
        print("Percentage=",self.per)
        print("CGPA=",self.cgpa)

obj=Result("Nikhil","CSE",12215880,100,100,100,100,100)
obj.display()
class radius():
    def __init__(self,r):
        self.radius=r
class height():
    def __init__(self,h):
        self.height=h
class volume(radius,height):
    def __init__(self,r,h):
        radius.__init__(self,r)
        height.__init__(self,h)
    def display(self):
        print('vol=',3,14*(self.radius**2)*self.height)
o=volume(7.8,9.2)
o.display()
class radius:
    radius=40.5
class height:
    height=10.3
class volume(radius,height):
    def display(self):
        print('vol=',3.14*(self.radius**2)*self.height)
o=volume()
o.display()



