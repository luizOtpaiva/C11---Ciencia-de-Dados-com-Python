import numpy as np # Importando a biblioteca NumPy

def main():

    # criando um numpy array de 2 dimensoes
    mtz = np.arange(1, 10, 1).reshape(3,3) # cria uma matriz 3x3 com valores de 1 a 9
    print("Matriz 3x3:\n", mtz)  # imprimindo a matriz

    # verificando se os elementos da matriz sao maiores que 5
    print("Elementos maiores que 5 ", mtz > 5)  # Verifica se os elementos da matriz são maiores que 5 e retorna um array booleano
    # ele retorna True para os elementos maiores que 5 e False para os menores ou iguais a 5

    # extraindo os elementos da matriz que sao maiores que 5
    print(mtz[mtz > 5])  # Exibe os elementos da matriz que são maiores que 5

    # extraindo os elemntos pares da matriz
    print("Elementos pares da matriz:", mtz[mtz % 2 == 0])  # Exibe os elementos pares da matriz  






    








if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main()  