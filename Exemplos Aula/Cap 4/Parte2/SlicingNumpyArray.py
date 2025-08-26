import numpy as np # Importando a biblioteca NumPy

def main():

    # criando um numpy array de 2 dimensoes
    mtz = np.arange(1, 10, 1).reshape(3,3) # cria uma matriz 3x3 com valores de 1 a 9
    print("Matriz 3x3:\n", mtz)  # imprimindo a matriz


    # extrair a primeira linha e coluna da matriz
    terceira_linha = mtz[2]  # Extrai a terceira linha da matriz ou pode ser mtz[2, :] para extrair a terceira linha
    print("Primeira linha:", terceira_linha)  # Imprime a primeira linha

    #extraindo a segunda coluna da matriz
    segunda_coluna = mtz[:, 1]  # Extrai a segunda coluna da matriz
    print("Segunda coluna:", segunda_coluna)  # Imprime a segunda coluna

    #extraindo todas as linhas e colunas da matriz
    todas_linhas = mtz[:] # Extrai todas as linhas da matriz
    print("Todas as linhas:\n", todas_linhas)  # Imprime todas as linhas

    # exatrindo da primeira coluna para frente 
    primeira_coluna_para_frente = mtz[:, 1:]  # Extrai a primeira coluna para frente
    print("Primeira coluna para frente :", primeira_coluna_para_frente)  # Imprime a primeira coluna 

    # exatraindo a segunda linha e terceira coluna
    segunda_linha_terceira_coluna = mtz[1, 2]  # Extrai o elemento da segunda linha e terceira coluna
    print("Elemento da segunda linha e terceira coluna:", segunda_linha_terceira_coluna)  # Imprime o elemento
   









if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main()