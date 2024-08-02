s=int(input())
a=int(input())
b=int(input())
n=0
for i in range(a,b+1):
    num=[int(x) for x in str(i)]
    soma=sum(num)
    if soma==s:
        n+=1
print(n)