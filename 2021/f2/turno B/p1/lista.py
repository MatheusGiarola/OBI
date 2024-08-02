n=int(input())
lista=[int(x) for x in input().split()]

start=0
stop=n-1
counter=0
while start<stop:
    if lista[start]==lista[stop]:
        start+=1
        stop-=1
    else:
        if lista[start]<lista[stop]:
            lista[start+1]+=lista[start]
            lista.pop(start)
            stop-=1
            counter+=1
        else:
            lista[stop-1]+=lista[stop]
            lista.pop(stop)
            stop-=1
            counter+=1
print(counter)