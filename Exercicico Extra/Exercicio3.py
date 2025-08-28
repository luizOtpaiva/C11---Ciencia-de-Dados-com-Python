import numpy as np


def main():

    # mostrando a taxa media de alfabetização

    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    alfabetizados = ds[1:,9 ]
    alfabetizados_float = alfabetizados.astype(float)

    media = np.mean(alfabetizados_float)
    
    print(media)

if __name__ == '__main__':  # para poder mostrar que esse é o programa principal
    main() 