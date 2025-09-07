import pandas as pd

def main():
    # criando uma series, usando duas listas de de inicio
    
    indices = ['a', 'b', 'c']
    valores = [10,20,30]
    
    # criando um dicionario
    
    dic = {'a':10, 'b':20, 'c':30}
    dic2 = {'a':10, 'b':20,'d':40}
    
    series = pd.Series(dic) # cria uma series a partir de um dicionario
    series2 = pd.Series(dic2)
    
    # operações entre series
    
    print('Soma das series')
    print(series + series2) # soma as series, alinhando pelos indices
    print('Subtração das series')
    print(series - series2) # subtrai as series, alinhando pelos indices
    
    # fazendo soma e subtração elemento a elemento com valor padrao
    print ('Soma com valor padrao', series.add(series2, fill_value=0))
    print ('Subtração com valor padrao', series.sub(series2, fill_value=0))
    
if __name__ == '__main__':
    main()