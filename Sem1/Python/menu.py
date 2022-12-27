veg=["rice","dal","burger","roti","dosa","soup","paneer"]
vp=[100,120,60,15,120,60,180]
nveg=['chicken','egg','fish']
np=[200,30,150]
snack=['manchurian','spring roll','noodles']
sp=[130,70,110]
n=int(input('Enter no of items ordered='))
for a in range(len(veg)):
    veg[a]=veg[a].upper()
for b in range(len(nveg)):
    nveg[b]=nveg[b].upper()
for c in range(len(snack)):
    snack[c]=snack[c].upper()
n=int(input('Enter the no of veg items ordered='))
menu={}
for x in range(n):
    name=input('Enter veg dish name=')
    name=name.upper()
    quantity=int(input("enter quantity="))
    for a in range(len(veg)): 
        if veg[a]==name:
            menu.update({name:quantity*vp[a]})
p=int(input('Enter no nveg item ordered='))
for x in range(p):
    name=input('Enter nveg dish name=')
    quantity=int(input('Enter quantity='))
    for b in range(len(nveg)):
        if nveg[b]==name:
            menu.update({name:quantity*np[b]})
s=int(input('Enter no snack item ordered='))
for x in range(s):
    name=input('Enter snack dish name=')
    quantity=int(input('Enter quantity='))
    for c in range(len(snack)):
        if snack[c]==name:
            menu.update({name:quantity*sp[c]})  
print('ordered menu',menu)
for a,b in menu.items():
    print(a,':',b)
total=0
for x in menu.values():
    total=total+x
    print('Total bill=',total)    



