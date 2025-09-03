import numpy as np 

def main():
    
    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )
    
    # mostrando apenas mostrar  apenas  o  País  (Country),  Região (Region), População (Population) e Area (Area (sq. mi.)) 
    mostrando_valores = ds[1:, [0, 1, 2, 3]] # pega do 1 para frente e le todos os outros 
    
    print("Todos os dados pedidos: ", mostrando_valores)
        
    
if __name__ == '__main__':
    main()