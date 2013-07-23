#-*- encoding:latin1-*-
# Matrizes Espiral
# http://dojopuzzles.com/problemas/exibe/matriz-espiral/

# Cria a matriz base
def cria_matriz(x, y):
    matriz = []
    for e in range(x):
        matriz.append([])
        for i in range(y):
            matriz[e].append(0)
    return matriz

def montar_matriz_espiral(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    valor_inicial = preenche_linha_matriz(matriz, 0, 0, 0, colunas)
    if linhas == 1:
        return matriz;
    # defininado ponteiros para auxiliar na alteracao da matriz
    linha_atual = 0
    coluna_atual = colunas
    limite = (linhas * colunas)
    try:
        while valor_inicial < limite:
            # Percorre a coluna mais a direita sempre descendo
            valor_inicial = preenche_coluna_matriz(matriz, coluna_atual-1, valor_inicial, linha_atual + 1, linhas - linha_atual)
            
            # Percorre a linha inferior da direita para esquerda
            valor_inicial = preenche_linha_matriz(matriz, (linhas - linha_atual) -1, valor_inicial, coluna_atual-2, (colunas - coluna_atual)-1)
            
            # Percorre a coluna mais a esquerda sempre subindo
            valor_inicial = preenche_coluna_matriz(matriz, (colunas-coluna_atual), valor_inicial, (linhas - linha_atual) -2, linha_atual)
            
            # Percorre a linha superior sempre da esquerda para direita
            valor_inicial = preenche_linha_matriz(matriz, linha_atual + 1, valor_inicial, (colunas - coluna_atual)+1, coluna_atual -1)
            
            linha_atual += 1
            coluna_atual -= 1
    except:
        print "ex"
        pass
    return matriz

# define o passo que o for vai ter(incremento ou decremento)
def calcula_passo_for(ini, fim):
    if ini < fim:
        return 1
    else:
        return -1

# Preenche a matriz na linha especifica, com o valor inicial
# incrementando-o da posicao ini até fim
# podendo ser crescente ou decrescente)
def preenche_linha_matriz(matriz, linha, valor_inicial, ini, fim):
    for e in range(ini, fim, calcula_passo_for(ini, fim)):
        matriz[linha][e] = valor_inicial
        valor_inicial += 1
    return valor_inicial

# Preenche a matriz na coluna especifica em todas as linhas,
# com o valor inicial incrementando-o da posicao ini até fim
# podendo ser crescente ou decrescente)
def preenche_coluna_matriz(matriz, coluna, valor_inicial, ini, fim):
    for e in range(ini, fim, calcula_passo_for(ini, fim)):
        matriz[e][coluna] = valor_inicial
        valor_inicial += 1
    return valor_inicial   

# Apenas imprime a matriz
def imprime_matriz(matriz):
    print ''
    # Verifica se é matriz
    if matriz == None:
        print "Os parametros informados nao definem uma matriz!"
    else:
        for linha in matriz:
            for coluna in linha:
                print str(coluna).zfill(2) ,
            print ''

def matriz_espiral(linhas, colunas):
    matriz = cria_matriz(linhas, colunas)
    matriz = montar_matriz_espiral(matriz)
    imprime_matriz(matriz)

def main():
    linhas = int(raw_input("Quantidade de linhas: "))
    colunas = int(raw_input("Quantidade de colunas: "))
    matriz_espiral(linhas,colunas)

if __name__ == '__main__':
    main()
    
    
