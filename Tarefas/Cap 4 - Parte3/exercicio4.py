import numpy as np 

def main():

    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    # pegando a missao mais cara realizada pela SpaceX
    arr_cost = ds[1:, 6]  # do índice 1 até o fim , só a coluna 6 para pegar o custo
    arr_empresa = ds[1:, 1]  # do índice 1 até o fim , só a coluna 1 para pegar a empresa

    # convertendo a coluna de custo para float
    arr_cost_float = arr_cost.astype(float)  # Converte a coluna de custo para float

    # armazendo aonde tem a empresa SpaceX
    spaceX = np.char.find(arr_empresa, "SpaceX") >= 0

    
    maior_custo_spacex = np.max(arr_cost_float[spaceX])# Filtra os custos da SpaceX e encontra o maior
    print("Maior custo de missão realizada pela SpaceX:", maior_custo_spacex)  # Exibe o maior custo

if __name__ == '__main__':  
    main()