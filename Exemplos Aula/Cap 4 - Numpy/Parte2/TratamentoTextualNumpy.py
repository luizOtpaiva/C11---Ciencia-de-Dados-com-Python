import numpy as np # Importando a biblioteca NumPy  

#subpacote char

def main():

    arr = np.array(["Goku", "Goten", "Gohan", "Trunks", "Bulma"]) # Cria um array unidimensional com nomes de personagens
    print("Array original:", arr)  # Imprime o array original

    # usando o subpacote char para manipular strings
    encontrando = np.char.find(arr, "Go")  # Verifica se a letra "Go" está presente em cada string do array
    print("Encontrando 'Go':", encontrando)  # Imprime o resultado da busca
    # o -1 e quando a letra nao e encontrada, e o indice 0 é quando a letra e encontrada

    #buscando quem tem "ha" no nome
    buscando = np.char.find(arr, "ha")  # Verifica se a letra "ha" está presente em cada string do array
    print("Buscando 'ha':", buscando)  # Imprime o resultado da busca
    # o 2 e quando a letra e encontrada, e o -1 é quando a letra nao e encontrada, e o 2 significa a posicao da letra "h" na string "Gohan"

    # agora querendo que ele returne apenas true or false
    buscando_bool = np.char.find(arr, "Go") >= 0  # Verifica se a letra "Go" está presente em cada string do array e retorna um array booleano
    print("Buscando 'GO' (booleano):", buscando_bool)  # Imprime o resultado booleano  

    # agora mostrando apenas os nomes que tem "Go" no nome
    print("Nomes que que tem a letra 'Go' : ", arr[np.char.find(arr, "Go") >= 0])  # Exibe os nomes que contêm "Go" no array original

    np.char.upper(arr)  # Converte todos os nomes do array para maiúsculas
    print("Nomes em maiúsculas:", np.char.upper(arr))  # Imprime os nomes em maiúsculas

    # procurando o mesmo "Go" agora
    print(arr[np.char.find(arr, "GO") >= 0])  # Exibe os nomes que contêm "GO" no novo array em maiúsculas


if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main()