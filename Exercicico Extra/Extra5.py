import numpy as np

def main():
    
    ds = np.loadtxt(r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
                    delimiter = ';', 
                    dtype=str,
                    encoding='utf-8'
    )
    
    paises = ds[1:,[0,1,8]]
    
    # pegando os com maior renda
    
    paises = paises[paises[:,1] == "LATIN AMER. & CARIB    "] # pwga a regiao do caribe
    custos = np.max(paises[:, 2].astype(float)) # pega qual o maior custo desse novo paises que definimos acima

    
    print(custos, paises) # para podemos visualizar 
    
    custos = paises[:,2].astype(float) # converte para float 
    
    # encontrar índice do maior custo
    idx_max = np.argmax(custos) # pega onde esta o indice de maior valor, se vemos no print anterios veremos que é o 10
    print("Inidice de onde esta o maior custo: " , idx_max) # printa o maior indice

    # pega o pais de indice maximo
    pais_max = paises[idx_max, 0] # nesse caso vai na linha 10 e pega a coluna 0, correspondente a paises
    
    custo_max = custos[idx_max]
    print("Valor do custo Maximo : ", custo_max) # mostra qual o amior custo que como ja sabemos e no indice 10
    
    print("País com maior renda per capita:", pais_max, "-", custo_max)
    
if __name__ =='__main__':
    main()
    
    
    