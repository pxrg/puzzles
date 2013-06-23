# -*- coding: latin1 -*-
# Questão do Diamantes
 
 
letra = raw_input("Digite uma letra: ").upper()
lista_espacos = []
lista_espacos.append(0)
espaco = 1
for i in range(0, 26, 1): 
   lista_espacos.append(espaco)
   espaco += 2
indice_letra = ord(letra) - 65+1
indice = 0
for i in xrange(indice_letra, 0, -1):
   char = chr(65 + indice)
   if(i == indice_letra):
      print ' '* i, char
   else:
      print ' '*i,char+' ' * lista_espacos[indice] + char
   indice += 1

indice -= 2
for i in xrange(2, indice_letra + 1):
   char = chr(65 + indice)
   if(i == indice_letra):
      print ' '* i, char
   else:
      print ' '*i,char+' ' * lista_espacos[indice] + char
   indice -= 1
   
