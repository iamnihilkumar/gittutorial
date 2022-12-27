# 
'''a = int(input())
x=a/0
print(x)'''
# try and except statement are used to catch a handle
'''try:
    a=int(input('enter value='))
    b=int(input('enter another value='))
    x=a/b
    print(x)
except ZeroDivisionError:
    print('cant divide by zero')
l=[1,2,3,4,5]
try:
    print('new element=',l[3])
    print('new element=',l[5])
except:
    print('new element not present')'''
# try block can have multiple except block
'''def fun(n):
    if n<4:
        x=n/n-3
    print(x)
try:
    fun(3)
    fun(4)
except ZeroDivisionError:
    print('new element not present')
except NameError:
    print("variable not defined") ''' 
# 
'''try:
    a=int(input('enter the value of a='))
    b=int(input('enter the value of b='))
    c=a/b
except ZeroDivisionError:
    print('cant divide by zero')
else:
    print('value of c=',c)
finally:
    print('end of the program')'''

