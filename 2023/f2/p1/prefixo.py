n1=int(input())
word1=input()
n2=int(input())
word2=input()
lpref=0
if n1<n2:
    for i in range(n1):
        if word1[i]==word2[i]:
            lpref+=1
        else:
            break
    print(lpref)
else:
    for i in range(n2):
        if word1[i]==word2[i]:
            lpref+=1
        else:
            break
    print(lpref)
        