import numpy as np

def main():


    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    paises =  ds[1:,1] # pega apenas as linhas da regiao, 

    count_missoes_realizadas = np.sum(np.char.find(paises, 'NORTHERN AMERICA') >= 0) # lembrar do >= 0 na prova
    print(count_missoes_realizadas)


if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main() 