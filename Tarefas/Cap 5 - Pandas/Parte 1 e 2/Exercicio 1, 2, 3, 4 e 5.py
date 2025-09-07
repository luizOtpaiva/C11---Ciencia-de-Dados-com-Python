import numpy as np
import pandas as pd


def main():
    
    # Exercicio 1:
    
    # criando uma series

    seriesAno1 = {'Java': 16.25, 'C': 16.04, 'Python': 9.85}
    seriesAno2 = {'C': 16.21, 'Python': 12.12, 'Java': 11.68}
    
    series1 = pd.Series(seriesAno1)
    series2 = pd.Series(seriesAno2)
    
    print(series1)
    print(series2)
    
    
    # Exercicio 2:
    
    # somando os valores para saber a porcentagem de cada ano das linguagens
    total_ano1 = series1.sum()
    total_ano2 = series2.sum()
    print('Total Ano 1: ', total_ano1)
    print('Total Ano 2: ', total_ano2)
    
    # Exercicio 3:
    
    # crescimento:
    crescimento = series2 - series1
    print('Crescimento (%): \n', crescimento)
    
    # declinio
    declinio = (crescimento / series1) 
    print('Declínio (%): \n', declinio)
    
    #Exercicio 4:
    
    # apenas as linguagens que tiveram crescimento
    crescimento_positivo = crescimento[crescimento > 0]
    print('Crescimento Positivo (%): \n', crescimento_positivo)
    
    # Exercicio 5: 
    
    # projeção de crescimento para os próximos 2 anos, usando a mesma taxa dedeclinio
    
    crescimento_futuro = series2 * (1 + declinio) ** 2 # 2 ao quadrado
    print('Crescimento Futuro (%): \n', crescimento_futuro) 
    mais_popular = crescimento_futuro.nlargest(1)
    print('Linguagem mais popular em 2 anos: \n', mais_popular)    
    
    
if __name__ == '__main__':
    main()