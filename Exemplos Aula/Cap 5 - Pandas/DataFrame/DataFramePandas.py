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
    

if __name__ == '__main__':
    main()