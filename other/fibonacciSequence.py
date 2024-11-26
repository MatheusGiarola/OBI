n=int(input())
terms=[0 for _ in range(n+1)]
terms[0]=0
terms[1]=1
for i in range(2,n+1):
    terms[i]=terms[i-1]+terms[i-2]
print(terms[n])