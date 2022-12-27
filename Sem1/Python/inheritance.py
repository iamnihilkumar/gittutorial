class A:
    def __init__(self,a,b):
        self.x=a
        self.y=b
class B(A):
    def __init__(self,a,b,c):
        A.__init__(self,a,b)
        self.z=c
        print('sum=',self.x+self.y+self.z)

obf=B(10,20,30)
