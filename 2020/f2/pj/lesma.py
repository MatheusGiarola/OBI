h=int(input())
s=int(input())
d=int(input())
dias=0
acumulado=0
while acumulado<h:
    dias+=1
    acumulado+=s
    if acumulado>=h:
        print(dias)
        break
    acumulado-=d

    