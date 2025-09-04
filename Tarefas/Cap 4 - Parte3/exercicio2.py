import numpy as np

def main():
    
    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )

    print(ds)
    
    # pegando apenas a coluna dos custos
    
    custos = ds[1:, 6] # linha 1 para frente, coluna 6
    
    custos_float = custos.astype(float) # converte os valores para float, para poder fazer a media dps
    
    custos_maior = custos_float[custos_float > 0]
    
    custos_medio = np.mean(custos_maior)
    
    print("Valor medio do custo eh de :", custos_medio)
    



    
if __name__ == '__main__':  
    main()  

