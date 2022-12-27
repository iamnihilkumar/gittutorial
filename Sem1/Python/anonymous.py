#anonymous func are that func are created by lambda func
# which takes n numb of arguments but it can have only one argunment
# add 10 to argunment a and return the result
x= lambda a :a+10
print(x(5))
#multiply a and b and return the result
x= lambda a,b:a*b
print(x(10,20))
#the power of lamda are better known if we use anonymous function in another  function
def user(n):
    return lambda a:a*n
    x=user(2)
    print(a(3))
    #write the anonymous function which will return area of the circle
area=lambda r:3.14*2**2
print(area(3.5))
rad=float(input('enter radius='))
print('area of the circle=',area(rad))
#MAX fuction
MAX=lambda x,y,z :x if x>y and x>z else y if y>z else z




