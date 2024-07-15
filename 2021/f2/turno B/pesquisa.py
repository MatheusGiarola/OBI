n=int(input())
verifier=0
for i in range(n):
    lista=[x for x in input().split()]
    if (0.7*float(lista[2]))>=float(lista[1]):
        print(lista[0])
        verifier+=1
if verifier==0:
    print('*')