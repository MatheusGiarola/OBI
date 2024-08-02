n=int(input())
lado=3
if n==1:
    npontos=lado**2
else:
    aumento=0
    for i in range(1,n):
        aumento+=2**i
    lado+=aumento
    npontos=lado**2
print(npontos)