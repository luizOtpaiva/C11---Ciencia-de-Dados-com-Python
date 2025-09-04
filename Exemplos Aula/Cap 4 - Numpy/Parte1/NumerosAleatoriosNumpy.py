import numpy as np # importando o numpy

#Numeros Aleatorios com Numpy
# gerando numeros aleatorios

arr = np.random.randint(1, 100, size=10) # gerando 10 numeros aleatorios entre 1 e 100
print("Numeros aleatorios gerados:", arr) # imprimindo os numeros aleatorios


#Semente aleatoria - é quando você define um valor inicial para o gerador de numeros aleatorios
# isso garante que os numeros aleatorios gerados sejam os mesmos toda vez que o codigo for executado
# isso é util para reproduzir resultados em testes ou experimentos

np.random.seed(42) # definindo a semente para gerar numeros aleatorios
arr_seeded = np.random.randint(1, 100, size=10) # gerando 10 numeros aleatorios entre 1 e 100 com a semente definida
print("Numeros aleatorios com semente 42:", arr_seeded) # imprimindo os numeros aleatorios com semente


np.random.seed(10) # redefinindo a semente para garantir que os numeros aleatorios sejam os mesmos
arr_seeded_10 = np.random.randint(1, 10, size=10) # gerando 10 numeros aleatorios entre 1 e 10 com a semente definida
print("Numeros aleatorios com semente 10:", arr_seeded_10) # imprimindo os numeros aleatorios com semente 10


# A unique retorna os valores unicos do array, ou seja, remove os duplicados, de maneira ordenada

print(np.unique(arr_seeded_10)) # imprimindo os valores unicos do array com semente 10

# Unique para retornar quantas vezes cada valor aparece no array
print("Valores unicos e suas contagens:", np.unique(arr_seeded_10, return_counts=True)) # imprimindo os valores unicos e suas contagens

