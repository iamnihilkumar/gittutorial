class calculte:
    def area(self,*args):
        if len(args)==1:
            self.side=args[0]
            print('area of surface=',self.side*self.side)
        if len(args)==2:
            self.L=args[0]
            self.B=args[1]
            print('area of rectangle=',self.L*self.B)
        if len(args)==3:
            self.L=args[0]
            self.B-args[1]
            self.H=args[2]
            print('area of cuboid=',self.L*self.B*self.H)

o=calculte( )
o.area(10)
o.area(10,20)
o.area(10,20,30)
n=int(input('enter your device='))
if n==1:
    x=int(input('enter the side of square='))
    obj=calculte()
    obj.area(x)
elif n==2:
    x=int(input('enter length='))
    y=int(input('enter breadth='))
    obj=calculte()
    obj.area(x,y)



