# meta characters are characters with special mean
# "[ ]=[a-m]"
# \ --> signal with special sequence alse used to escape special characters
# . -->single character
# ^-->starts with (mention befoe word)
# $-->ends with(mention after word)
# ..-->any two character
# .*-->many character
# +--> one or more
#{}-->exactly specific number of occurences
# *-->0 or more
# set-->a set is set of character keep inside to pair of square brackets which has a special meaning
# "[arn]"--> return a match where one of the specified character between a r n
# "[a-z]"-->return a match for any lower case letters between a to z
# "^[arn]"-->
# "[0123]"-->match between characters 0 to 3
# "[0-9]"-->match between characters 0 to 9
# "[0-5][0-9]"-->returns a match between 002-59
import re
s="Eat 4 times before 11:45"
t=re.findall("[0-5][0-9]",s)
print(t)
# [a-z A-Z 0-9]
a=re.findall("[a-zA-Z0-9]",s)
print(a)
# write a program that accepts the string containing your email,validate the email using the 
# concept of regular expression
s=input('enter your email=')
t=re.match("[a-zA-Z0-9-_]+@[a-zA-Z]+\.[a-z]{3}",s)
if t:
    print("email valid")
else:
    print("not valid")
# validate your mobile no
b=input("enter your mobile no=")
c=re.fullmatch("[6-9][0-9]{9}",b)
if t!=None:
    print('vaild')
else:
    print('Invalid')





