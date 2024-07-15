y=input()
pal=list(y)
cifra=''
for i in range(len(pal)):
    if pal[i] == 'a' or 'e' or 'i' or 'o' or 'u':
        cifra+=pal[i]
    else:
        c=pal[i]
        x=pal[i]
        ordem=['a','e','i','o','u', c].sort()
        v1=ordem[(ordem.index(c)-1)]
        v2=ordem[(ordem.index(c)+1)]
        if c-v1 > v2-c:
            x+=v1
        else:
            x+=v2
        if chr(ord(c)+1) =='e' or 'i' or 'o' or 'u':
            x+= chr(ord(c)+2)
        else:
            x+=chr(ord(c)+1)
        cifra+=x
print(cifra)