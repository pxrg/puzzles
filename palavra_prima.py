#-*- encoding:latin1-*-
# Palavras Primas
# http://dojopuzzles.com/problemas/exibe/palavras-primas/

import string
import math

def retorna_total_palavra():
    letras = string.ascii_letters
    palavra = raw_input("Digite uma palavra: ")
    if not palavra.isalpha():
        print "Digite apenas letras!!"
        return None
    total = 0
    for letra in palavra:
        total += (letras.find(letra)+1)
    return total

def numero_primo(numero):
    rad = int(math.sqrt(numero))
    for val in xrange(2, rad+1):
        if ((numero % val) == 0):
            return False
    return True

def palavra_prima():
    total = retorna_total_palavra()
    if total == None:
        return;
    if numero_primo(total):
        print "A palavra digitada é prima!!"
    else:
        print "Palavra comum"

if __name__ == '__main__':
    palavra_prima()
    
    
