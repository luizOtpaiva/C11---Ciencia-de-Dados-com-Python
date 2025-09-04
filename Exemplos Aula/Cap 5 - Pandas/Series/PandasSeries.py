import pandas as pd

def main():
    
    # criando uma series, usando duas listas de de inicio
    
    indices = ['a', 'b', 'c']
    valores = [10,20,30]
    
    # criando um dicionario
    
    dic = {'a':10, 'b':20, 'c':30}
    
    # series = pd.Series(data=valores, index=indices) # cria uma series
    series = pd.Series(dic) # cria uma series a partir de um dicionario
    print(series)
    print(type(series)) # mostra o tipo do objeto criado
    
    
        

if __name__ == '__main__':
    main()