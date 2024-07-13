c=int(input())
contador=0
for i in range(3):
    x=int(input())
    if c-x>=0:
        contador+=1
        c-=x
print(contador)