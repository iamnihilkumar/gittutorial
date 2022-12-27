def square(n):
    return n**2
l=[2,4,6,8,10,12,14,16,18,20]
result=map(square,l)
sl=list(result)
print(sl)
# 
m=[1,3,5,7,9,11,13,15,17,19]
result=map(lambda x:x**2,m)
sm=list(result)
print(sm)
# 
def factorial(n):
    f=1
    for x in range(1,n+1):
        f=f*x
    return f
l=[2,4,6,8]
result=map(factorial,l)
fl=list(result)
print(fl)
