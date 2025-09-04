import numpy as np

# funcoes para manipular numpy arrays

# 1 dimensional array de 1s
arr = np.ones(10)  # cria um array de 1s com 10 elementos
print("Array de 1s:", arr)

# 2 dimensional array de 0s 
mtz_zeros = np.zeros((10))  # cria  uma array de 0s com 10 elementos, unidirecional
print("Matriz de 0s:", mtz_zeros)

# 2 dimensional array de 0s com Reshape, transforma um array unidimensional em uma matriz 2D. 5x2 nesse caso
mtz_zeros_2d = np.zeros((10)).reshape(5,2)  # cria uma matriz de 0s com 5 linhas e 2 colunas
print("Matriz de 0s 2D:", mtz_zeros_2d)

# 2 dimensional array de 0s com Reshape, transformando a array em uma matriz 5x2
mtz_ones_2d = np.zeros((5,2)) # ja colocando a forma 5x2
print("Matriz de 0s 2D:", mtz_ones_2d)

# Arrange - cria um array com valores de 0 a 9
arrange_array = np.arange(10, 101, 10) # cria um array com valores de 10 a 101, pulando de 10 em 10
print("Array com arange:", arrange_array)

# menor valor desse array
print("Menor valor do array:", arrange_array.min())  # imprime o menor valor do array

# maior valor desse array
print("Maior valor do array:", arrange_array.max())  # imprime o maior valor do array

# indice do menor valor
print("Índice do menor valor:", arrange_array.argmin())  # imprime o índice do menor valor do array

# indice do maior valor
print("Índice do maior valor:", arrange_array.argmax())  # imprime o índice do maior do valor do array




