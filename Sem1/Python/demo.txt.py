with open('demo.txt','r') as ab:
    data=ab.readlines()
    lines=0
    for x in data:
        lines+=1
    print('No of lines=',lines)
with open('demo.txt','r') as ab:
    data=ab.read()
    words=0
    for x in data:
        if ord(x)==32:
            words+=1
    print('No of words in file=',words+1)