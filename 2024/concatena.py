n,q=map(int, input())
lista=input().split() #linha:começo   cooluna:fim
valores=[[0 for _ in range(n)]for _ in range(n)]
for _ in range(q):
    start,stop=map(int, input().split()) #1,5
    intervalo=lista[(start-1):stop]
    tam=len(intervalo)
    pot=0
    found=False
    if tam==1:
        print(0)
    else:
        toMap=[]
        for i in range((stop-1),-1,-1): #2
            if valores[start-1][i]!=0:
                pot+=valores[start-1][i]
                toMap=intervalo[-i:stop]
                found=True
                break
        for char in toMap:
            for j in range(tam):
                num=str(char)+intervalo[j]
                pot+=int(num)
            valores[start-1][char]=pot