n,f=map(int, input().split())
lista=[int(x) for x in input().split()]
moedas=0
dias=0
while moedas<f:
    moedas=0
    dias+=1
    for i in range(n):
        x=dias//lista[i]
        moedas+=x
    #     print(moedas)
    # print('dia fechado:',dias)
print(dias)