n=int(input())
lista=[x for x in input().split()]
contador=1
if len(lista) ==1:
    print(contador)
else:
    escadinha=int(lista[1])-int(lista[0])

    for i in range(n-1):
        x=int(lista[(i+1)])-int(lista[i])
        if x != escadinha:
            contador+=1
            escadinha=x
    print(contador)