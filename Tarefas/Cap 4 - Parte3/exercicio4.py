import numpy as np

def main():
    
    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )
    
    nomes_empresas = ds[1:, 1] # pega a coluna do nome de empresas
    custo_coluna = ds[1:, 6]
    
    #conveter coluna de custo
    custo_float = custo_coluna.astype(float)
    
    pegando_SpaceX = np.char.find(nomes_empresas, "SpaceX") >= 0 # retorna um bool para onde encontra a empresa SpaceX
    
    
    maior_custo_SpaceX = np.max(custo_float[pegando_SpaceX]) # pega o maximo valor de custo na spaceX
    print("O maior custo da empresa SoaceX eh de: " , maior_custo_SpaceX)
    

if __name__ == '__main__':
    main()
    