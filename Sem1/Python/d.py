menu={'rice':100,'burger':60,'dosa':120,'roti':20,'cheese chilli':200,'egg roll':70}
total=0
for x in menu.values():
    total=total+x
print('bill slip')
for a,b in menu.items() :
    print(a,":",b)
print("total bill=",total)
#dictname={k:v for loop in zip project}
L=['apple','banana','guava','orange','grape']
C=['red','yellow','black','grew','green']
fruit={k:v for (k,v) in zip(L,C)}
print(fruit)
D={x:x**2 for x in range(1,11)}
print(D)
# 
old_price={'milk':5,'bread':3,'butter':2,'cheese':1}
d_r=81.25
new_price={key:value*d_r for key,value in old_price.items()}
print(new_price)
import string as s
L=list(s.ascii_uppercase)
print(L)
import string as s
A=list(s.ascii_uppercase)
N=list(range(1,27))
D={k:v for (k,v) in zip(A,N) if v%2 == 0}
D1={k:v for (k,v) in zip(A,N)if v%2!=0}
print(D)
print(D1)