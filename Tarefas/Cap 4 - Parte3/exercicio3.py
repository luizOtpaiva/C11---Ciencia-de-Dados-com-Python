import numpy as np

def main():
    
    ds = np.loadtxt(
        r"C:\Users\luizo\OneDrive\Área de Trabalho\Inatel Materias\6 semesntre\C11 - Python\C11 - Ciencia de Dados com Python\Exemplos Aula\space(in).csv", 
        delimiter=';', dtype=str, encoding='utf-8'
    )
     
    
    # pegando a coluna de missoes
    localização_missoes = ds[1:, 2]
    
    quant_missoes_eua = np.sum(np.char.find(localização_missoes, "USA"))
    print("Quantidade de missoes realizadas nos EUA: ", quant_missoes_eua)
    
  
if __name__ == '__main__':
    main()