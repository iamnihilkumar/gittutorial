f = open("Python/Demo/demo.txt", "r")
l = 1
for x in f.readlines():
    c = 0
    print("Length of character in line", l, "is=", len(x))
    l += 1
