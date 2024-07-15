countV=0
for i in range(6):
    x=input()
    if x =="V":
        countV+=1
if countV>4:
    print(1)
elif 2<countV<5:
    print(2)
elif countV==0:
    print(-1)
else:
    print(3)
    