n=int(input())
soma=0
for i in range(n):
    num=input()
    l=len(num)
    p=num[l-1]
    base=''
    for j in range(l-1):
        base+=num[j]
    pot=int(base)**int(p)
    soma+=pot
print(soma)