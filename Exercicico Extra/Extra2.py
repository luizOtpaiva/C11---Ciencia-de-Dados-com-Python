import numpy as np

def main():
    
    
    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )
    
    regioes = ds[1:, 1] # pega so as regioes e pula o cabeçalho
    
    print("Todas as regiões registradas: ", regioes)
    
    # pegando a quantidade de regiões
    
    
    
    contando = np.unique(regioes) # conta as regioes e armazenas elas assim  [ "eua", "br"]
    
    print( "A quantidade de regiões presentes eh de : ", len(contando))
    
    
    
if __name__ == '__main__':
    main()