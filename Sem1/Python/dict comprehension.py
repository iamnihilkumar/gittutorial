reg=int(input('Enter student reg no='))
ccode=input('Enter course code=')
tmarks=0
mte=int(input('Enter your marks='))
tmarks=tmarks+(mte//2)
LD=int(input('Enter the no lectures delivered='))
LA=int(input('Enter the no of lectures attended='))
atp=(LA/LD)*100
atp=int(atp)
print('current attendance percentage=',atp)
if atp>=90:
    tmarks=tmarks+5
elif atp>=84 and atp<=89.8:
    tmarks=tmarks+4
elif atp>=80 and atp<=83:
    tmarks=tmarks+3
elif atp>=75 and atp<=79:
    tmarks=tmarks+2
else:
    tmarks=tmarks+0
ca1=int(input('Enter the marks of ca1='))
ca2=int(input('Enter the marks of ca2='))
ca3=int(input('Enter the marks of ca3='))
b1=0
b2=0
if ca1>ca2:
    b1=ca1
else:
    t=ca1
    ca1=ca2
    ca2=t
    b1=ca1
if ca2>ca3:
    b2=ca2
else:
    b2=ca3
cam=((b1+b2)/60)*25
import math as m
cam=int(m.cal(cam))
tmarks=tmarks+cam