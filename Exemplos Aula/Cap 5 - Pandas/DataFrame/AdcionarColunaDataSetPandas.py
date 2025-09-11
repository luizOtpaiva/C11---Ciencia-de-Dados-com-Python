import numpy as np
import pandas as pd


def main():
    
    
    # trazendo o dataset de um arquivo csv
    ds = pd.read_csv(r'C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\Cap 5 - Pandas\DataFrame\paises.csv', 
                     delimiter = ';')
    
    print(ds.columns)
    
    print(ds.head(2)) # o 2 representa as 2 primeiras linhas
    print(ds.tail(2)) # o 2 representa as 2 ultimas linhas
    
    # criando uma nova coluna que mostra a porcentagem da população de  cada pais em relacao a populacao global
    
    soma_populaçao = ds['Population'].sum() # soma a coluna população
    print('Soma da população: ', soma_populaçao)
    
    # agora vendo a porcentagem de cada pais em relacao a populacao global
    
    populationPerc = ds['Population'] / soma_populaçao
    print('Porcentagem: ', populationPerc)
    
    # adicionando a nova coluna ao dataset
    ds['PopulationPerc'] = populationPerc
    print(ds)
    
    # Criando uma nova versão do dataset
    
    ds.to_csv(r'C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\Cap 5 - Pandas\DataFrame\paises_v2.csv', 
              sep = ';')
    
    print ('Dataset salvo com sucesso')
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()