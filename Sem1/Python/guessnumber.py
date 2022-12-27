#guess number
from operator import truediv


n=int(input('enter the number='))
for x in range(1,101):
    if n==x:
        print('the number is =',x)
        result=True
        break
if result==False:
        print(n,'not found')
# write a program to calculate the factorial of number from 1 to 10
for x in range(1,11):
    f=1
for a in range (1,x+1):
        f=f*a
        print('factorial of',x,'is=',f)
a=int(input('enter no='))
b=int(input('enter no='))
for  x in range(a,b+1):
    f=1
    for a in range (1,x+1):
        f=f*a
        print('factorial of',x,'is=',f)
for x in range(a-1,b+2,2):
    f=1
    for a in range(1,x+1):
        f=f*a
        print('fcatorial of ',x,'is=',f)
#how to generate random using for loop
import random as r
a= int(input('enter the beginnig value of ='))
b=int(input('enter the end value of='))
if a>b:
    print('not allowed')
else:
    n=r.randint(a,b)
    for x in range(a,b+1):
        if n==x:
            print('guessed number=',x)
            break
#
import random as r
n=6
a=0
b=0
c=0
d=0
e=0
f=0
for x in range(n):
    num=r.randint(1,6)
    if num==1:
        a=a+1
    elif num==2:
        b=b+1
    elif num==3:
        c=c+1
    elif num==4:
        d=d+1
    elif num==5:
        e=e+1
    else:
        f=f+1
print('1 comes on dice',a,'times')
print('2 comes on dice',b,'times')
print('3 comes on dice',c,'times')
print('4 comes on dice',d,'times')
print('5 comes on dice',e,'times')
print('6 comes on dice',f,'times')


        
        



        


