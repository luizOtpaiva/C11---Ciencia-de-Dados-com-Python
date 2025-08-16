#dando exemplos de tuplas

tupla = ("Goku", "Vegeta","Trunks", "Gohan") # uma tupla e uma coleção imutavel, nao da para mudar em temp de exec
print(tupla) # printando a tupla

#alterar elementos

 # tupla[0] = "Bulma" # isso da um erro

#slicing de elementos ( fatiamento)
print(tupla[1:3]) # pega o vegeta e trunks - primeira opção e inclusive e a ultima e é exclusiva
                  # ou seja nesse caso pega o elemento da frente, que vai pegar o anterior que é

print(tupla[2:]) # nesse caso nao colocar nada ele pega tudo para frente do trunks, e o 2 pega o trunks

print(tupla[-2]) # nesse caso ele pega de tras para frente, pega o trunks

print(len(tupla)) # vai contar o numero de elemntos da tupla
print(max(tupla)) # pegou em ordem alfabetica e pegou o ultimo ( max)
print(min(tupla)) # tranformou em ordem alfabetico e pegou o minimo ( primeiro)
# print(avg(tupla))







