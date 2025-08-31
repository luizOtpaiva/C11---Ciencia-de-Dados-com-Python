import numpy as np # Importando a biblioteca NumPy

#  Crie dois NumPy Arrays unidimensionais de tamanho 8,  um formado apenas por 1’s e outro formado por números aleatórios entre 0 e 9 

def main():
    array_ones = np.ones(8)  # Cria um array de 1's com tamanho 8
    array_random = np.random.randint(0, 10, size=8)  # Cria um array de números aleatórios entre 0 e 9 com tamanho 8

    print("Array de 1's:", array_ones)
    print("Array de números aleatórios:", array_random)

    # Somando estes arrays e guardando o resultado em um novo array
    array_sum = array_ones + array_random
    print("Array resultante da soma:", array_sum)

    print(array_sum.sum())  # Exibe a soma dos elementos do array resultante
    
    if array_sum.sum() > 40:
        # caso a soma seja maior que 40, ele vai formar uma outra matriz com mais linhas do que colunas
        array_reshaped = array_sum.reshape(2, 4)  # Reshape para 2 linhas e 4 colunas
        print("Array reshaped (2 linhas, 4 colunas):", array_reshaped)
    else:
        # caso a soma seja menor ou igual a 40, ele vai formar uma matriz com mais colunas do que linhas
        array_reshaped = array_sum.reshape(4, 2)  # Reshape para 4 linhas e 2 colunas
        print("Array reshaped (4 linhas, 2 colunas):", array_reshaped)


if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main()


