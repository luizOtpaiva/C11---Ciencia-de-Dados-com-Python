import numpy as np # importando o numpy


# matriz desse jeito : 
#               Agua   Luz  Net
# Janeiro      
# Feveiro
# Marco

# operações com matrizes numpy
mtz = np.array([50, 10, 100, 60, 25, 100, 75, 80,100]).reshape(3,3) # criando uma matriz 3x3
print("Matriz:\n", mtz) # imprimindo a matriz

print("Soma dos elementos da matriz:", mtz.sum()) # somando todos os elementos da matriz
print("Soma dos elementos por coluna:", mtz.sum(axis=0)) # somando os elementos por coluna
print("Soma dos elementos por linha:", mtz.sum(axis=1)) # somando os elementos por linha

# pegando so o quanto tem em um especifico ponto, no caso de net
print("Soma da conta de Net nesses meses: ", mtz.sum(axis=0)[2]) # soma dos elementos da terceira coluna (Net) # soma dos elementos da terceira coluna (Net)




