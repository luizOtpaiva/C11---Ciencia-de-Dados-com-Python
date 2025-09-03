import numpy as np 

def main():
    
    
    ds = np.loadtxt(r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", delimiter=';', dtype=str, encoding='utf-8')
    
    
    print(ds) # dataset carregado
    
    # lendo apenas as colunas das missoes
    
    status_missao = ds[1:, 7] # le a partir da linha 1, a coluna 8
    
    # vendo a quantidade de missoes que deram certas
    
    missoes_corretas = np.sum(status_missao == "Success,,,,,," )
    print(missoes_corretas)
    
    # vendo a porcentagem de missoes
    
if __name__ == '__main__':  
    main()