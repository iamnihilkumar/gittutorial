# write a program in python that converts all the characters of the file in toggle case
f=open('abc.txt','w')
f.write("this class is python programming\n")
f.write("COURSE Code int108\n")
f.write("section KOC03\n")
f.write("numbers of student=72\n")
f.close()

with open('abc.txt','r') as ab:
    data=ab.read()
f=open('new.txt','w')
e=''
for x in data:
    if ord(x)>=65 and ord(x)<=90:
        t=ord(x)
        t=t+32
        e=e+chr(t)
        f.write(e)
    elif ord(x)>=47 and ord(x)<=122:
        t=ord(x)
        t=t-32
        e=e+chr(t)
        f.write(e)
    else:
        e=e+x
        f.write(e)
f.close()

