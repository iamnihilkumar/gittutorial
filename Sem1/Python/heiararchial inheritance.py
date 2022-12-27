


class Values:
    def __init__(self,a,b):
        self.v1=a
        self.v2=b
class Sum(Values):
    def __init__(self,a,b):
        Values.__init__(self,a,b)
        self.c=self.v1+self.v2
    def display(self):
        print('Sum=',self.c)
class Product(Values):
    def __init__(self,a,b):
        Values.__init__(self,a,b)
        self.p=self.v1*self.v2
    def display(self):
        print('Product=',self.p)
o1=Sum(10,20)
o1.display()
o2=Product(30,40)
o2.display 