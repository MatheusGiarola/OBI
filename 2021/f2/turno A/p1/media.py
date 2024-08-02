a,b=map(int, input().split())
for c in range(-b,b):
    m=(a+b+c)/3
    lista=[a,b,c]
    lista.sort()
    if m==lista[1]:
        print(c)
        break
