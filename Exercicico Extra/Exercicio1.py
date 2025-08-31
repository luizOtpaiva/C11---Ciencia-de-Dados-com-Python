import numpy as np


def main():

    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )
     
    
    
    # mostrar apenas o País (Country), Região (Region), População (Population) e Area (Area (sq. mi.)) dos países

    todos_pedidos = ds[:, :4]  # do índice 1 até o fim , só a coluna 1 para pegar a empresa

    print(todos_pedidos)

if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main() 