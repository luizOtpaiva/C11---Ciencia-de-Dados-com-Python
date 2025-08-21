import numpy as np # importando o numpy

mtz = np.array([50, 10, 100, 60, 25, 100, 75, 80,100]).reshape(3,3) # criando uma matriz 3x3
print("Matriz:\n", mtz) # imprimindo a matriz

print(mtz/10) # dividindo todos os elementos da matriz por 10