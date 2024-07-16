n=int(input())
posMoeda=input()
for i in range(n):
    x=int(input())
    if x==1:
        if posMoeda=='A':
            posMoeda='B'
        elif posMoeda=='B':
            posMoeda='A'
    elif x==2:
        if posMoeda=='C':
            posMoeda='B'
        elif posMoeda=='B':
            posMoeda='C'
    else:
        if posMoeda=='A':
            posMoeda='C'
        elif posMoeda=='C':
            posMoeda='A'
print(posMoeda)