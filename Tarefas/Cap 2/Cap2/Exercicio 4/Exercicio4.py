def main():
    entrada = input("Seja Bme vindo! \n")
    escolha = int(input("Qual a distancia da viajem que deseja fazer: \n"))

    if escolha <= 200: # caso seja menor que 200
        cobranca = 0.50*escolha 
        print("Sua viajem vai ficar R$: {}" .format(cobranca))
    elif escolha > 200: # caso seja maior que 200
        cobranca = 0.45*escolha
        print("Sua viajem vai ficar R$: {}" .format(cobranca))

if __name__ == '__main__': #para poder mostrar que esse e o programa principal
    main()