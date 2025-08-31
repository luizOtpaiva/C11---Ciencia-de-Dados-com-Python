import numpy as np # Importando a biblioteca NumPy


def main():

    # criando um matriz 4x4 formada por numeros aleatorios de 1 a 50, use seed = 10 antes que faz a geração dos números aleatórios
    np.random.seed(10)  # Define a semente para garantir a reprodutibilidade
    matriz = np.random.randint(1, 51, size=(4, 4))  # Cria uma matriz 4x4 com números aleatórios entre 1 e 50
    print("Matriz 4x4 com números aleatórios entre 1 e 50:\n", matriz)

    # mostrando a media de cada linha e coluna
    media_linhas = np.mean(matriz, axis=1)  # Calcula a média de cada linha
    media_colunas = np.mean(matriz, axis=0)  # Calcula a média de cada coluna
    print("Média de cada linha:", media_linhas) # imprimindo a média de cada linha
    print("Média de cada coluna:", media_colunas) # imprimindo a média de cada coluna


    #apresentando o maior valor das medias das linhas e colunas
    maior_media_linha = np.max(media_linhas)  # Encontra o maior valor entre as médias das linhas
    maior_media_coluna = np.max(media_colunas)  # Encontra o maior valor entre as médias das colunas
    print("Maior média entre as linhas:", maior_media_linha)  # imprimindo o maior valor entre as médias das linhas
    print("Maior média entre as colunas:", maior_media_coluna)  # imprimindo o maior valor entre as médias das colunas 

    # motrando a quantidade de aparições de cada um dos numeros gerados na matriz
    
    print(np.unique(matriz, return_counts=True))  # Exibe os números únicos na matriz e suas contagens

    #mostrando agora os numeros que aparecem apenas duas vezes
    numeros_duas_vezes = matriz[np.isin(matriz, np.unique(matriz, return_counts=True)[0][np.unique(matriz, return_counts=True)[1] == 2])]
    print("Números que aparecem exatamente duas vezes:", numeros_duas_vezes)


if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main()  