import numpy as np
import pandas as pd


def main():
    
    
    # trazendo o dataset de um arquivo csv
    ds = pd.read_csv('C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\Cap 5 - Pandas\DataFrame\paises.csv', 
                     delimiter = ';')
    
    print(ds.columns)
    
    print(ds.head) # mostra as  primeiras linhas do dataset
    print(ds.tail) # mostra as ultimas linhas do dataset
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()