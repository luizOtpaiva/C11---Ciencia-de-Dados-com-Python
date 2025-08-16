def main():
    entrada = input('Seja Bem Vindo')

    aux = 1
    while ( aux != 0 ):
        opcao = str(input("Diga para a gente qual o seu sexo \n"
        "M - Masculino \n"
        "F - Feminino \n"
        ))

        if opcao == 'M' or opcao == 'F' : # caso escolha o masculino ou feminino
            print('Obigado por nos informar!')
            print('Encerrando o programa')
            aux = 0
        else :
            print('Digite novamente uma letra valida')
        

if __name__ == '__main__': #para poder mostrar que esse e o programa principal
    main()