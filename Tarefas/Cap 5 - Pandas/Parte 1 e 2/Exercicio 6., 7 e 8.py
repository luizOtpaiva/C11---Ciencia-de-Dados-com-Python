import numpy as np
import pandas as pd


def main():
    
    # Exercicio 6: 
    
    dic_dados = {
        "W": [10, 29, 30, 43, 37],
        "X": [37, 26, 9, 41, 48],
        "Y": [16, 30, 10, 37, 12],
        "Z": [1, 49, 1, 17, 25]
    }

    df = pd.DataFrame(dic_dados, index=["A", "B", "C", "D", "E"])
    print(df)
    
    # media dos elementos da coluna X menores que 30
    media_coluna_X = df[df['X'] < 30]['X'].mean()
    print('Média dos elementos da coluna X menores que 30: ', media_coluna_X)
    
    # Exercicio 7:

    
    # media dos elementos da linha D 
    media_linha_B = df.loc['D'].mean()
    print('Média dos elementos da linha D: ', media_linha_B)
    
    # soma de cada uma das linhas :
    soma_linha_E = df.iloc[4].sum()
    print('Soma dos elementos da linha E: ', soma_linha_E)
    
    # Exercicio 8:
    
    # Pegando apenas as linhas A, B e E e as colunas X e Y
    linhas_requeridas = df.loc[['A', 'B', 'E'], ['X', 'Y']]
    print("Linhas pedidas: \n", linhas_requeridas)
    
    # Somando cada linha e cada coluna
    soma_linhas_A = linhas_requeridas.iloc[0].sum()
    print('Soma dos elementos da linha A: ', soma_linhas_A)
    soma_linhas_B = linhas_requeridas.iloc[1].sum()
    print('Soma dos elementos da linha B: ', soma_linhas_B)
    soma_linhas_E = linhas_requeridas.iloc[2].sum()
    print('Soma dos elementos da linha E: ', soma_linhas_E)

    soma_coluna_X = linhas_requeridas['X'].sum()
    print('Soma dos elementos da coluna X: ', soma_coluna_X)
    soma_coluna_Y = linhas_requeridas['Y'].sum()
    print('Soma dos elementos da coluna Y: ', soma_coluna_Y)
    
if __name__ == '__main__':
    main()