import numpy as np # Importando a biblioteca NumPy 

# criando uma matriz de tamanho 4x4 formado por numeros aleatórios entre 0 e 9
def main():
    mtz = np.random.randint(0,10, size=(4,4))  # Cria uma matriz 4x4 com números aleatórios entre 0 e 9
    print("Matriz 4x4 com números aleatórios:\n", mtz)

    # extraindo o numero de colunas e linhas da matriz e multiplicando eles
    linhas, colunas = mtz.shape  # Obtém o número de linhas e colunas da matriz
    produto = linhas * colunas  # Multiplica o número de linhas pelo número de colunas
    print("Número de linhas:", linhas)
    print("Número de colunas:", colunas)
    print("Produto do número de linhas e colunas:", produto)

    # dizendo se com esse produto, ela poderia se tornar uma matriz ou nao
    if produto % 2 == 0:
        print("A matriz pode ser transformada em uma matriz quadrada.")
    else:
        print("A matriz não pode ser transformada em uma matriz quadrada.")



if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main()