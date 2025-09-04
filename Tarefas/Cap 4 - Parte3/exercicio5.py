import numpy as np

def main():
    
    
    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )
    
    empresas_missoes_espaciais = ds[1:,1] #pega as empresas
    
    
    ## Assim você terá dois arrays paralelos:
    ## empresas[i] → nome da empresa
    ## contagens[i] → quantidade de missões daquela empresa
    #o parâmetro return_counts=True, ele também devolve quantas vezes cada valor aparece.
    
    empresas, contagens = np.unique(empresas_missoes_espaciais, return_counts=True)
    
    # Mostra os resultados
    for i in range(len(empresas)):
        print(empresas[i], " realizou ", contagens[i], " de missões espaciais.")
    

if __name__ == '__main__':
    main()