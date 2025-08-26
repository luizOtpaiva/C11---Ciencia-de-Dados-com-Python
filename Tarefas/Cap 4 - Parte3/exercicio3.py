import numpy as np


def main():

    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    # pegando todas as missoes realizadas no eua
    arr_missoes_realizadas_no_eua = ds[1:, 2]  # do índice 1 até o fim , só a coluna 2
    print("Coluna de missoes realizadas no EUA:\n", arr_missoes_realizadas_no_eua)  # Exibe a coluna de missoes realizadas no EUA


    count_missoes_realizadas = np.sum(np.char.find(arr_missoes_realizadas_no_eua, 'USA'))
    print("Número de missões realizadas nos EUA:", count_missoes_realizadas)


if __name__ == '__main__':  
    main()  