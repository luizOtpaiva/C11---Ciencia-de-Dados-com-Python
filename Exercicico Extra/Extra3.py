import numpy as np

def main():
    
    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )
    
    taxa_alfabetizacao = ds[1:, 9] # pega apenas a coluna da taxa de alfabetização
    print(taxa_alfabetizacao)
    
    taxa_alfabetizacao_float = taxa_alfabetizacao.astype(float) # transforma para float para poder fazer a media depois
    
    media_alfabetizacao = np.mean(taxa_alfabetizacao_float)
    
    print( "A taxa media de alfabetização desse data set eh de: ", media_alfabetizacao)
    
    
if __name__ == '__main__':
    main()