a=int(input())
s=int(input())
d=int(input())
dias=0
h=0
while h<a:
    dias+=1
    h+=s
    if h>=a:
        break
    h-=d
print(dias)