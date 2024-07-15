string=input()
alfabeto='abcdefghijlmnopqrstuvxz'
count=0
for letter in alfabeto:
    if letter not in string:
        print('N')
        count+=1
        break
if count==0:
    print('S')