'''f=open('file.txt','w')
f.write("xyz\n")
f.write("computer science and engineering\n")
f.write("KOC03\n")
f.write("12215880\n")
f.write("address\n")
f.close()'''
# ord('A')-->65
# ord('Z')-->90
# ord('a')-->97
# ord('z')-->122
# ord('O')-->48
# ord()
upper=0
lower=0
vowels=0
spaces=0
digits=0
others=0
with open('file.txt','r')as ab:
    data=ab.read
    newdata=data[0::1]
for x in newdata:
    print(x)

for x in newdata:
    if ord(x)>=65 and ord(x)<=90:
        upper+=1
    elif ord(x)>=97 and ord(x)<=122:
        lower+=1
    elif ord(x)>=45 and ord(x)<=57:
        digits+=1
    elif ord(x)==32:
        spaces+=1
    else:
        others+=1
print("uppercase letters=",upper)
print("lowercase letters=",lower)
print("digits=",digits)
print("spaces=",spaces)
print("special characters=",others)
f=open('abc.txt','w')
f.write(S.ascii_lowercase)
f.close()
f=open('xyz.txt','w')
f.write(ascii_uppercase)
f.close()


# color of apple is red'
# color of grappe is green and black
# color of bananans are yellow 
# color of mangos are green and yellow




