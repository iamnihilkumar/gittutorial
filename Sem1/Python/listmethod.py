l=[]
# append method are used to elements at the end of the list.
# list.append(element)
l.append(10)
l.append(20)
l.append(30)
print(l)
# index method insert element at given index position
# insert()
# list.insert(index,element)
l.insert(0,40)
print(l)
l.insert(2,50)
# remove
M=[1,2,3,4,4,5,6]
M.remove(4)
print(M)
M.pop()
M.pop(1)
print(M)
# del
x=['a,','b','c']
y=['e','f','g']
del(x)
del(y[0])
print(y)
# print(x)--permanentaly deleted so error is the output
# index()
W=[10,20,30,50,40,60,70,50]
i=W.index(50)
print(i)
c=W.count(50)
print(c)
# reverse()
W.reverse()
print(W)
# sort()
L1=[27,53,49,16,72,35]
L2=[18,9,53,36,74,29,63]
L1.sort()
print(L1)
L2.sort(reverse=True)
print(L2)
# extend()
L1.extend(L2)
print(L1)
L2.extend([10,20,30,40])
print(L2)
# clear()
P=['a','b','c','d','e']
P.clear()
print(P)
L=list()
n=int(input('enter size of list='))
for x in range (n):
    e=int(input('enter element='))
    L.append(e)
print('create list')
print(L) 

