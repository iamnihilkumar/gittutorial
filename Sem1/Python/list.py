#accesising elements
l=[10,20,30,40,50,60,70,80,90,100]
# lisT index
print(l[4])
print(l[7])
print(l[-5])
# 
l[4]=50
print(l)
l[7:10]=[100,100,100]
print(l)
#operation on th list
#repetition
m=[5,10,15]
mn=m*3
print(mn)
# max(),min(),sum()
l=[10,15,23,92,7,86,44,17,58]
print(max(l))
print(min(l))
print(sum(l))
print(sum(l)/len(l))
# list slicing
# list[start:stop:step]
l=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
l2=l[-5:-10:-1]