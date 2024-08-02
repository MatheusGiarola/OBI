n=int(input())
arvores=list(map(int, input().split()))
l=sum(arvores)
if l%4!=0:
    print('N')
else:
    l=int(l/4)
soma=0
verifier=0
for i in arvores:
    soma+=i
    if soma==l:
        soma=0
        verifier+=1
    else:
        if soma>l:
            print('N')
            break
if verifier>3:
    print('S')