import numpy as np # Importando a biblioteca NumPy



def main():
    # criando dois numpys arrays unidimensional, um de numeros pares de 0 a 51  e outro de pares de 100 a 50

    array_pares_0_50 = np.arange(0, 52, 2)  # Cria um array de números pares de 0 a 50
    array_pares_100_50 = np.arange(100, 48, -2)  # Cria um array de números pares de 100 a 50

    # concatenando os resultados e ordenando os valores
    array_concatenado = np.concatenate((array_pares_0_50, array_pares_100_50))
    array_ordenado = np.sort(array_concatenado)  # Ordena o array concatenado
    
    # Exibindo os resultados ordanados
    print("Array de números pares de 0 a 50:", array_pares_0_50)
    print("Array de números pares de 100 a 50:", array_pares_100_50)
    print("Array concatenado e ordenado:", array_ordenado)

if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main()  

    

