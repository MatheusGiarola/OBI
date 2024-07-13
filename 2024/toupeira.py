def verificar_passeio_possivel(saloes, tuneis, passeios):
    # Criar um dicionário para representar os túneis
    mapa_tuneis = {}
    for x, y in tuneis:
        if x not in mapa_tuneis:
            mapa_tuneis[x] = set()
        if y not in mapa_tuneis:
            mapa_tuneis[y] = set()
        mapa_tuneis[x].add(y)
        mapa_tuneis[y].add(x)

    # Função para verificar se um passeio é possível
    def passeio_possivel(passeio):
        for i in range(len(passeio) - 1):
            atual, proximo = passeio[i], passeio[i + 1]
            if proximo not in mapa_tuneis.get(atual, set()):
                return False
        return True

    # Verificar cada sugestão de passeio e contar quantas são possíveis
    contador_possiveis = 0
    for passeio in passeios:
        if passeio_possivel(passeio):
            contador_possiveis += 1

    return contador_possiveis

# Ler a entrada
S, T = map(int, input().split())
tuneis = [tuple(map(int, input().split())) for _ in range(T)]
P = int(input())
passeios = [list(map(int, input().split()))[1:] for _ in range(P)]

# Verificar o número de sugestões de passeio possíveis
resultado = verificar_passeio_possivel(S, tuneis, passeios)
print(resultado)
