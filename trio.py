def isTriangle(a,b,c):
    if a>b and a>c:
        if b+c>a:
            return True
    elif b>a and b>c:
        if a+c>b:
            return True
    else:
        if a+b>c:
            return True
    return False
n=int(input())
lista=[int(x) for x in input().split()]
sides=[]
for i in range(n):
    intervalo=lista[i+1:]
    tam=len(intervalo)
    for j in range(tam):
        lados=(lista[i],intervalo[j],i,-(tam-j))
        sides.append(lados)
for p in sides:

    print()