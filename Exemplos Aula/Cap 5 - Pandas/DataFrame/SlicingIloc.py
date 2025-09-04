import pandas as pd
import numpy as np

def main():
    
    np.ramdom.seed(10) # semente para gerar os mesmos numeros aleatorios
    
    # lembrar que no dataframe temos indices para linhas e colunas
    
    df = pd.DataFrame(
        index = ['A', 'B', 'C', 'D', 'E'],
        columns=['W', 'X', 'Y', 'Z'],
        data = np.ramdom.randint(1,40[5,4])
    )
    
    print(df)
    
    # fazendo slicing com iloc, padrao numpy ( indices numericos)
    
    print('Slicing com iloc', df.iloc[0:2,:]) # mostra as linhas 0 e 1, todas as colunas
    
    # fazendo slicing com loc
    print('Slicing com loc', df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']]) # mostra as linhas A e B, todas as colunas
    
    # ou por exemplo pegando so a coluna W e Y
    print('Slicing com loc', df.loc[['A', 'B'], ['W', 'Y']]) # mostra todas as linhas A e B, colunas W e Y
    
    # ou para poder pegar usando apenas as colunas
    print(df[['W', 'Y']]) # mostra todas as linhas, colunas W e Y
 
if __name__ == '__main__':
    main()