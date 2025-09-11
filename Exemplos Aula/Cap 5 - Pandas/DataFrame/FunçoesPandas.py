import numpy as np
import pandas as pd


# Funcao que da um desconto de 10% em algo
def tenpercent(x):
    return x * 0.9 #


def main():
    
    ds = pd.read_csv(r'C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\Cap 5 - Pandas\DataFrame\paises_V2.csv', 
                     delimiter = ';')
    
    # pegando a taxa de mortaliade e aplicando a funcao tenpercent
    taxaMort = ds['Deathrate']
    
    # criando uma nova series que desconta 10% da taxa de mortalidade
    novaTaxaMort = taxaMort.apply(tenpercent) # apply aplica a funcao em cada elemento da series
    print('Taxa de Mortalidade com 10% de desconto: \n', novaTaxaMort)
    
    
    # criando um novo dataframe apenas com estas duas series
    
    df2 = pd.concat([taxaMort, novaTaxaMort], axis = 1) # concatena as duas series em um novo dataframe, junta os dois em formato de coluna
    df2.columns = ['Taxa de Mortalidade', 'Taxa de Mortalidade com 10% de desconto'] # renomeia as colunas
    print(df2)
    
    
    
    
     
if __name__ == '__main__':
    main()