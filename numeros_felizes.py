#-*- encoding: latin1-*-
# Numeros Felizes
# http://dojopuzzles.com/problemas/exibe/numeros-felizes/

def numero_feliz(numero):
    total = 0
    saida = ""
    for num in numero:
        valor = int(num)**2
        saida += " %s²(%d) +"%( num, valor)
        total += valor
    saida = saida[:len(saida)-1]
    print "%s = %d"%(saida, total)
    if total == 1:
        print "----- Numero Feliz -----  :-)"
        return
    elif total == 4:
        print "***** Numero Triste *****  :-("
        return
    numero_feliz(str(total))

def main():
    numero = raw_input("Digite um numero: ")
    if not numero.isdigit():
        print "Parametro inválido,, digite apenas numeros!"
        return
    numero_feliz(numero)


if __name__ == "__main__":
    main()
