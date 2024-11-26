s=int(input())
a=int(input())
b=int(input())
quantidade=0
for i in range(a,b+1):
    numero=str(i)
    soma=0
    for n in numero:
        aux=int(n)
        soma+=aux
    if soma==s:
        quantidade+=1
print(quantidade)