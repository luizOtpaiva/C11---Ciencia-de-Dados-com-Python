import numpy as np

def main ():


    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    # pegando os paises e custo

    paises = ds[1:,[0,1,8]] # pega os paises e custo
    print(paises)

    # encontrando o com a maior renda

    paises = paises[paises[:,1] == "LATIN AMER. & CARIB    "]
    custos = np.max(paises[:, 2].astype(float))

  # converter para float
    custos = paises[:,2].astype(float)

    # encontrar índice do maior custo
    idx_max = np.argmax(custos)

    # pegar o país correspondente
    pais_max = paises[idx_max, 0]
    custo_max = custos[idx_max]

    print("País com maior renda per capita:", pais_max, "-", custo_max)

if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main() 