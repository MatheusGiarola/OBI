n=int(input())
string=input()
anterior=''
count=0
rle=''
for i in string:
    if anterior=='':
        count+=1
        anterior=i
    else:
        if i==anterior:
            count+=1
            anterior=i
        else:
            rle+=f'{count} {anterior} '
            count=1
            anterior=i
rle+=f'{count} {anterior}'
print(rle)