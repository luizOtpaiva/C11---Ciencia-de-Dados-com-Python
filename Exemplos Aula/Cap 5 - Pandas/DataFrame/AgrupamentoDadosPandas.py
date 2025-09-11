import numpy as np
import pandas as pd


def main():
    
    
    ds = pd.read_csv(r'C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\Cap 5 - Pandas\DataFrame\paises_V2.csv', 
                     delimiter = ';')
    
    # agrupando os dados do dataset por região
    
    grroup_region = ds.groupby('Region')
    print(grroup_region) # a saida mostra que é um objeto do tipo DataFrameGroupBy
    
    # agora vendo os dados de deste dataframe agrupado
    
    print(grroup_region.count()['Country']) # mostra a contagem de paises por regiao
    print(grroup_region.sum()['Country']) # mostra a soma de paises por regiao, seria quais paises pertencem a cada regiao
    
    print(grroup_region.sum()['Population']) # mostra a soma da populacao por regiao
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()