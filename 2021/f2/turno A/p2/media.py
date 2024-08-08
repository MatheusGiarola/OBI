a,b=map(int, input().split())
for c in range(-b,b):
    media=(a+b+c)/3
    mediana=[a,b,c]
    mediana.sort()
    mediana=mediana[1]
    if int(media)==mediana:
        print(c)
        break