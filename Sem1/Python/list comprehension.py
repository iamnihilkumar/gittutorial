# new list=[exp for loop if statement]
'''L=[1,2,3,4,5,6,7,8,9,10]
NL=[x**2 for x in L]
print('new list')
print(NL)
L1=[x for x in L if x%2!=0]
L2=[x for x in L if x%2==0]
print(L1)
print(L2)
#  Write a program in python accepting n random element from user for empty list use
# the list and filter with those element which are div by 5 and add it to new list nl
L=[]
n=int(input('Ente rthe size of list='))
for x in range(n):
    e=int(input('Enter element='))
    L.append(e)
nl=[m for m in L if m %5==0]
print('original list')
print(L)
print('new list')
print(nl)
L[0],L[-1]=L[-1],L[0]
print('swapped list')
print(L)
L[0]=L[0]+L[-1]
L[-1]=L[0]-L[-1]
L[0]=L[0]-L[-1]
print(L)'''
'''def display(L):
    total=0
    for x in range(len(L)):
        total=total=L[x]
    return total
x=[38,56,43,72,89,77,98]
s=display(x)
print('total sum=',s)
def MAXMIN(L):
    MX=L[0]
    MN=L[0]
    for x in L:
        if MX<x:
            MX=x
    for y in L:
        if MN>y:
            MN=y
    return MX,MN
x=[38,56,43,72,89,12,77,98]
a,b=MAXMIN(x)
print('maximum=',a,'minimum=',b)'''
def prime(l):
    for a in range(len(l)):
        dc=0
        for b in range(1,l[a]+1):
            dc=dc+1
    if dc==1 or dc==2:
        print(l[a])
x=[ ]
n=int(input('enter size of l='))
for x in range(n):
    e=int(input('enter element='))
    x.append(e)
prime(x)
# L=[1,2,3,4]list 
# t=(1,2,3,4)tuple
a=(10,)
print(type(a))
p=1,2,3,4,5
print(type(p))
T=(10,20,30,40,50,60,70)
# accessing individual elements
print(T[3])
print(T[-2])
print(T[::-1])
T=()
L=list(T)
T=tuple(L)
print(T)