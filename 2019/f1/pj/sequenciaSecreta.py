n=int(input())
counter=0
aux=0
for i in range(n):
    x=int(input())
    if x != aux:
        counter+=1
    aux=x
print(counter)