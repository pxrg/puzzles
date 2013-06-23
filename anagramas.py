# -*- coding: latin1 -*-
# Questão dos Anagramas

def anagrama():
   def combina(palavra, indice, combinacao):
      letra = palavra[indice]
      nova_palavra = palavra[0:indice]+palavra[indice+1:]
      combinacao += letra
      if len(nova_palavra) == 0:
         print combinacao,
         return;
      for indice_aux in xrange(len(nova_palavra)):
         combina(nova_palavra, indice_aux, combinacao)

    
   palavra = raw_input("Digite uma palavra: ")
   for indice in xrange(len(palavra)):
      combinacao = ""
      combina(palavra, indice, combinacao)
      print "\n"

if __name__ == "__main__":
   anagrama()

      

