def main():
    menu = input('Seja Bem vindo! \n')
    tabuada = int(input ('Escolha um numero para ver a tabuada dele: \n'))
    valores = int (input ('Agora escolha ate qual numero vai ser feito a tabuada deste numero escolhido \n'))

    for c in range ( 0, valores + 1): #valores + 1 pois começa no 0
        resultado = tabuada*c
        print(resultado)
        

if __name__ == '__main__': #para poder mostrar que esse e o programa principal
    main()