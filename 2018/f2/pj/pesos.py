n=int(input())
lista=[int(x) for x in input().split()]
anterior=0
verifier=0
for i in range(n):
    if (lista[i]-anterior)>8:
        print('N')
        break
    else:
        verifier+=1
        anterior=lista[i]
if verifier==n:
    print('S')