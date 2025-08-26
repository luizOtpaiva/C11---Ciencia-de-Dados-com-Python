import numpy as np

def main():

    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    #empreas de missoes especiais

    # loop para ver quantas vezes cada empresa aparece

    arr_empresa = ds[1:, 1]  # do índice 1 até o fim , só a coluna 1
    print("Coluna de empresa:\n", arr_empresa)  # Exibe a coluna de empresa

    achando_spaceX = np.char.find(arr_empresa, "SpaceX")
    print(achando_spaceX)

    #para contar as missões da SpaceX
    quantidade_de_vezes = np.sum(arr_empresa == "SpaceX")
    
    print("\nQuantidade de missões da SpaceX:")
    print(quantidade_de_vezes)

if __name__ == '__main__':  
    main() 