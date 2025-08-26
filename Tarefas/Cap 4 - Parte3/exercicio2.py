import numpy as np

def main():

    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    print("Dataset carregado:\n", ds)


    arr_cost = ds[1:, 6]  # do índice 1 até o fim , só a coluna 6
    print("Coluna de custo (cost):\n", arr_cost)  # Exibe a coluna de custo

    # convertendo a coluna de custo para float
    arr_cost_float = arr_cost.astype(float)  # Converte a coluna de custo para float

    # agora vendo a media dos custos sendo eles maior que 0
    arr_cost_float_maior = arr_cost_float[arr_cost_float > 0]  # Filtra os custos maiores que 0
    media_cost = np.mean(arr_cost_float_maior) 
    print("Média dos custos (cost) maiores que 0:", media_cost)  


if main() == '__main__':  
    main()