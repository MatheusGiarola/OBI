n=int(input())
string=input()
rle=''
anterior=''
counter=0
for i in string:
    if i==anterior:
        counter+=1
        anterior=i
    else:
        if anterior=='':
            counter+=1
            anterior=i
        else:
            rle+= f'{counter} {anterior} '
            counter=1
            anterior=i
rle+= f'{counter} {anterior}'
print(rle)