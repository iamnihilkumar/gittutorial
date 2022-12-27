# Name: nikhil
# loction:amritsar
# date 05/11/22


def display(*args):
    for x in args:
        print(x)


display(15, 16, 17, 18)


def my_fun(*args):
    mx = args[0]
    for x in args:
        if mx < x:
            mx = x
    mn = args[0]
    for x in args:
        if mn > x:
            mn = x
    total = 0
    for x in args:
        total = total+x
    return mx, mn, total


a = int(input("Enter first no."))
b = int(input("Enter second no."))
c = int(input("Enter third no."))
d = int(input("Enter fourth no."))
max, min, sum = my_fun(a, b, c, d)
print("max=", max)
print("min=", min)
print("total sum=", sum)

