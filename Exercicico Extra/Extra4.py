import numpy as np

def main():
    
    ds = np.loadtxt(r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exercicico Extra\paises.csv", 
                    delimiter = ';', 
                    dtype=str,
                    encoding='utf-8'
    )
    
    paises = ds[1:, 1] # pega somente os paises e regiao
    
    contando_os_paises = np.sum(np.char.find(paises,'NORTHERN AMERICA' ) >= 0 )
    
    print(contando_os_paises)
    


    
    
    
    
    
    
if __name__ == '__main__':
    main()