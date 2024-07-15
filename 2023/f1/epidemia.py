pessoasI=int(input())
fatorR=int(input())
PaInfectar=int(input())
aumento=0
totalpD= pessoasI
nDias=0
while totalpD<PaInfectar:
    aumento=pessoasI*fatorR
    totalpD+=aumento
    pessoasI=aumento
    nDias+=1
print(nDias)
