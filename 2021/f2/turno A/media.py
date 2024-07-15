a,b=map(int, input().split())
x=b/2
for c in range(b):
    lista=[a,b,c]
    lista.sort()
    if ((a+b+c)/3)==lista[1]:
        print(c)
        break
