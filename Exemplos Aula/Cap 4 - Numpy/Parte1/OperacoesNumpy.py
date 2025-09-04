import numpy as np # importando o numpy

# operações com numpy arrays

arr = np.arange(1, 10, 1) # criando um array de 1 a 10 com passo 1
array_2 = np.arange(9, 0, -1) # criando um array de 9 a 1 com passo -1

print("Array de 1 a 10:", arr) # imprimindo o array 
print("Array de 9 a 1:", array_2) # imprimindo o array

print("Soma dos arrays:", arr + array_2) # somando os dois arrays
print("Subtração dos arrays:", arr - array_2) # subtraindo os dois arrays
print("Multiplicação dos arrays:", arr * array_2) # multiplicando os dois arrays

# concatenando os arrays
concatenated_array = np.concatenate((arr, array_2)) # concatenando os dois arrays ( junta elas )
print("Array concatenado:", concatenated_array) # imprimindo o array concatenado

