def main():
    entrada = input ('Que bom ter voce aqui! Seja bem Vindo')
    nome = str(input('Para começarmos, qual eh o seu nome ?')) # usuario escreve seu nome

    x = 1 # valor aux

    while ( x != 0 ):
        opcao = int(input('Escolha uma opçao abaixo: \n' 
        '1 - Seu nome com todas as letras maiúsculas \n' 
        '2 - Seu nome com todas as letras minúsculas \n'
        '3 - Quantas letras ao todo tem seu nome \n'
        '4 - Trocar sobrenome por "do Inatel" \n'
        '0 - Sair do Programa \n'
        ))

        if opcao == 1 :
            print(nome.upper()) # todo nome com letra maiuscula ou poderia ser nome = nome.upper() e depois print(nome)
        elif opcao == 2:
            print(nome.lower()) # todo nome com letra minuscula
        elif opcao == 3:
            print(len(nome)) # retorna a quantodade de letras no nome
        elif opcao == 4:
            partes = nome.split() # divide o nome em uma lista
            partes[-1] = "do Inatel" # partes[-1] acessa o último elemento da lista
            print(" ".join(partes))  # remove espaços para contar só as letras
        elif opcao == 0:
            print("Programa encerrado!")
            x = 0
            break
        else:
            print("Opção inválida, tente novamente.")
         
if __name__ == '__main__': #para poder mostrar que esse e o programa principal
    main()




