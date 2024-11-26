n=int(input())
lista=[int(x) for x in input().split()]
contracao=0
for i in range(n//2):
    if lista[i]!=lista[n-1-i]:
        x=lista[i]
        y=lista[n-1-i]
        if x>y:
            y+=lista[n-2-i]
        else:
            x+=lista[i+1]
        contracao+=1
print(contracao)