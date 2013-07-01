#-*- encoding: latin1-*-
# Distribuição de Mictórios
# http://dojopuzzles.com/problemas/exibe/distribuicao-de-mictorios/

def distribui():
    num_mictorios = int(raw_input("Quantidade de mictórios: "))
    mic_usados = raw_input("Mictorios já usados( user ',' para separar mais de um): ").split(",")
    try:
        mic_usados = map(int, mic_usados)
        mics = ["." for e in range(num_mictorios)]
        for mic in  mic_usados:
            if mic > num_mictorios:
                raise ValueError("Mictório usado passado maior que o numero de mictórios!")
            if mic == 0:
                continue
            mics[mic -1] = "X"
        print "Mictórios : ", ["." for e in range(num_mictorios)]
        print "Mictórios Usados : ", mics
        count = 0
        while(count < num_mictorios):
            if mics[count] != "X":
                livre = False
                if (count + 1) < num_mictorios:
                    livre = mics[count + 1] == "."
                else:
                    livre = True
                if (count - 1) >= 0:
                    livre = mics[count - 1] == "." and livre
                if livre:
                    mics[count] = "O"
                    count += 1
            count += 1
        livre = mics.count("O")
        print "%d pessoa(s) pode(m) entrar"%livre
        if livre > 0:
            print "Nos seguintes locais --"
            print "Mictórios Livres : ", mics
        
    except Exception as ex:
        print "\nError --------------------"
        print ex
        

if __name__ == "__main__":
    distribui()
