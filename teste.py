def p(n):
    if n%2==0:
        return n
    else:
        return None
numeros=[]
numeros.extend([p(2),p(6)])
numeros.append(p(3))
print(numeros)